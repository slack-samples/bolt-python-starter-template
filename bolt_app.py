import logging
import os
from importlib import import_module
from pkgutil import walk_packages

from slack_bolt import App, BoltResponse
from slack_bolt.oauth.callback_options import CallbackOptions, FailureArgs, SuccessArgs
from slack_bolt.oauth.oauth_settings import OAuthSettings
from slack_sdk.oauth.installation_store import FileInstallationStore
from slack_sdk.oauth.state_store import FileOAuthStateStore

import listeners

logging.basicConfig(level=logging.DEBUG)


# Callback to run on successful installation
def success(args: SuccessArgs) -> BoltResponse:
    # Call default handler to return an HTTP response
    return args.default.success(args)
    # return BoltResponse(status=200, body="Installation successful!")


# Callback to run on failed installation
def failure(args: FailureArgs) -> BoltResponse:
    return args.default.failure(args)
    # return BoltResponse(status=args.suggested_status_code, body=args.reason)


def oauth_settings() -> OAuthSettings | None:
    if "SLACK_CLIENT_ID" not in os.environ:
        return None
    return OAuthSettings(
        client_id=os.environ.get("SLACK_CLIENT_ID"),
        client_secret=os.environ.get("SLACK_CLIENT_SECRET"),
        scopes=["channels:history", "chat:write", "commands"],
        user_scopes=[],
        redirect_uri=None,
        install_path="/slack/install",
        redirect_uri_path="/slack/oauth_redirect",
        state_store=FileOAuthStateStore(expiration_seconds=600),
        installation_store=FileInstallationStore(),
        callback_options=CallbackOptions(success=success, failure=failure),
    )


# Initialization
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
    oauth_settings=oauth_settings(),
    token_verification_enabled=os.environ.get("SLACK_TOKEN_VERIFICATION_ENABLED", "true") == "true",
)


def load_listeners() -> None:
    for module_info in walk_packages(listeners.__path__, f"{listeners.__name__}."):
        import_module(module_info.name)


load_listeners()

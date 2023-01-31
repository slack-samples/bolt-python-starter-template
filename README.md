
# Bolt Python Starter Template

This app contains a generic Bolt for Python template app used to build out Slack apps on Slack's
[next-generation platform](https://api.slack.com/future).

Before getting started, make sure you have a development workspace where you have permissions to install apps. If you don’t have one setup, go ahead and [create one](https://slack.com/create).

**Guide Outline**:

- [Bolt Python Starter Template ](#bolt-python-starter-template)
  - [Supported Workflows](#supported-workflows)
  - [Setup](#setup)
    - [Install the Slack CLI](#install-the-slack-cli)
    - [Clone the Sample App](#clone-the-sample-app)
      - [Linting](#linting)
  - [Create a Link Trigger](#create-a-link-trigger)
  - [Running Your Project Locally](#running-your-project-locally)
  - [Project Structure](#project-structure)
    - [`manifest.json`](#manifestjson)
    - [`/triggers`](#triggers)
    - [`slack.json`](#slackjson)
  - [Resources](#resources)

---

## Supported Workflows

- **Sample workflow**: Enter details to send a message to a channel

## Setup

Before getting started, make sure you have a development workspace where you
have permissions to install apps. If you don’t have one set up, go ahead and
[create one](https://slack.com/create). Also, please note that the workspace
requires any of [the Slack paid plans](https://slack.com/pricing).

### Install the Slack CLI

To use this sample, you first need to install and configure the Slack CLI.
Step-by-step instructions can be found in our
[Quickstart Guide](https://api.slack.com/future/quickstart).

### Clone the Sample App

Start by cloning this repository:

```zsh
# Clone this project onto your machine
$ slack create my-app -t slack-samples/bolt-python-starter-template -b future

# Change into this project directory
$ cd my-app

# Setup your python virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate

# Install the project dependencies
$ pip install -r requirements.txt
```

#### Linting

```zsh
# Run flake8 from root directory for linting
flake8 *.py && flake8 listeners/

# Run black from root directory for code formatting
black .
```

## Create a Link Trigger

[Triggers](https://api.slack.com/future/triggers) are what cause workflows to
run. These triggers can be invoked by a user, or automatically as a response to
an event within Slack.

A [link trigger](https://api.slack.com/future/triggers/link) is a type of
trigger that generates a **Shortcut URL** which, when posted in a channel or
added as a bookmark, becomes a link. When clicked, the link trigger will run the
associated workflow.

Link triggers are _unique to each installed version of your app_. This means
that Shortcut URLs will be different across each workspace, as well as between
[locally run](#running-your-project-locally). When creating a trigger, you must select
the Workspace that you'd like to create the trigger in. Each Workspace has a
development version (denoted by `(dev)`), as well as a deployed version.

To create a link trigger for the sample workflow, run the following
command:

```zsh
slack trigger create --trigger-def triggers/sample_trigger.json
```

After selecting a Workspace, the output provided will include the link trigger
Shortcut URL. Copy and paste this URL into a channel as a message, or add it as
a bookmark in a channel of the Workspace you selected.

**Note: this link won't run the workflow until the app is either running locally
or deployed!** Read on to learn how to run your app locally and eventually
deploy it to Slack hosting.

## Running Your Project Locally

While building your app, you can see your changes propagated to your workspace
in real-time with `slack run`. In both the CLI and in Slack, you'll know an app
is the development version if the name has the string `(dev)` appended.

```zsh
# Run app locally
$ slack run

⚡️ Bolt app is running! ⚡️
```

Once running, click the
[previously created Shortcut URL](#create-a-link-trigger) associated with the
`(dev)` version of your app. This should start a workflow that opens a form used
to send a message to a certain channel!

To stop running locally, press `<CTRL> + C` to end the process.

## Project Structure

### `manifest.json`

`manifest.json` is a configuration for Slack CLI apps in JSON. This file will
establish all basic configurations for your application, including app name
and description.

Within the manifest are initializations for [workflows](https://api.slack.com/future/workflows) and [functions](https://api.slack.com/future/functions) are reusable building blocks
of automation that accept inputs, perform calculations, and provide outputs.
Functions can be used independently or as steps in workflows.

### `/triggers`

All trigger configuration files live in here - for this example,
`sample_trigger.json` is the trigger config for a trigger that starts the workflow
 initialized in `/manifest/manifest.json`.

### `slack.json`

Used by the CLI to interact with the project's SDK dependencies. It contains
script hooks that are executed by the CLI and implemented by the SDK.


## Resources

To learn more about developing with the CLI, you can visit the following guides:

- [Creating a new app with the CLI](https://api.slack.com/future/create)
- [Configuring your app](https://api.slack.com/future/manifest)
- [Developing locally](https://api.slack.com/future/run)

To view all documentation and guides available, visit the
[Overview page](https://api.slack.com/future/overview).

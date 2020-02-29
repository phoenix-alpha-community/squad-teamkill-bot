# Squad Teamkill Bot
A Discord bot for the Fear and Terror Discord that tracks Teamkills made on the
Fear and Terror Squad servers and posts information about these to Discord
channels.

## Overview
- **TK tracker**.
The bot will make a post in the TK channel for each team kill that occurs on
any of the servers.

![Image](images/tk.png)

## Installation
1. Clone this repository to:
    - All server machines
2. Install dependencies via `pip`:
    - Linux: `pip install -r requirements.txt`
    - Windows: `python3.exe -m pip install -r requirements.txt`
      (You might have to navigate to wherever your python installation is)
3. In the `squad_teamkill_bot` directory, make a copy of `config-sample.py`
   called `config.py`
4. Change the config parameters.
   The default parameters are set up to match the Fear and Terror Discord and
   Squad servers.
   Settings that still need to be changed:
   - Webhook URL for each TK channel

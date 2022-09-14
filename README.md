# game-of-life-starter-pack
A starter-pack for the game of life challenge


## Setup
This repo has a container for development.  
For this, you need to ensure you have the relevant extensions installed inside of vscode, namely;
- [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Fork the repo, clone your own repo.


## Start
There are a few ways to start your container, the easiest,
- When you open the repository in VSCode, it will prompt to "Reopen in Container", select this. 
- From within VS Code, launch the Command Palette, Search for ">Remote-Containers: Reopen in Container"

You will start in a directory called `/app`, this is mounted to the directory we're in now on the host. Any changes you do in this directory should reflect on the host immediately.

To start the application, run `app.py`, e.g. `python3 app.py`


## Development
If you require any packages installed, they can be added to the Dockerfile located at `.devcontainer/Dockerfile`


## Modifying this repo
- Fork the repo
- Create a branch in your repo for this change.  
  Do not use your `main` branch.
- Create a PR from your branch to the original `main`


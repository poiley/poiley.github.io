# :page_facing_up: Personal Blog

:wave:  Hi, I'm Ben. Web development and automation are two long-held interests of mine. That interest hasn't 
always come in the form of a Github [Pages](https://pages.github.com/) & [Actions](https://github.com/features/actions) 
powered Markdown-based blog, but now it has. Let's see how long I keep this thing up.

## :computer: Installation

To use, clone the repository, set up the virtual environment, and run the Pelican development server.

```bash
# Clone the Repository
git clone git@github.com:poiley/poiley.github.io.git
cd poiley.github.io

# Set up the virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the dev server
pelican --list
```

## :iphone: Deployment

Deployment is done automatically thanks to Github Actions. Every time a commit is pushed to `master`, Github
Actions builds the site with `publishconf.py` and deploys the site by committing the output to the `gh-pages` branch.

## :mortar_board: License

This project is developed under the [MIT](https://choosealicense.com/licenses/mit/) license.

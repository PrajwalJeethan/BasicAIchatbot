# Tom Chatbot

A small ELIZA-style chatbot with a browser interface. `main.py` contains Tom's
response patterns and can still be run as a terminal chatbot. `app.py` serves
the separate web UI and sends chat messages to that same backend.

## Run locally

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`. To use the terminal version instead, run
`python main.py`.

## Host from GitHub

GitHub stores the source code, but GitHub Pages cannot run a Python backend.
Push this repository to GitHub, then create a Render Web Service connected to
the repository. Render can use the included `Procfile`; the equivalent settings
are:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

Deploy the service to get a public URL for the chatbot.
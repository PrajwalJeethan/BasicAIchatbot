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

## Deploy the web UI with GitHub Pages

GitHub Pages serves the static browser UI; it cannot run the Python chat
backend. The `Deploy to GitHub Pages` workflow publishes the page whenever you
push to `main`. In the repository settings, set **Pages → Build and deployment
→ Source** to **GitHub Actions**.

Host the Flask app as a separate web service (for example, on Render). The
included `Procfile` starts it; the equivalent settings are:

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

Set the backend service's `TOM_ALLOWED_ORIGIN` environment variable to the
GitHub Pages origin, such as `https://OWNER.github.io` (no trailing slash).
Then add a repository Actions variable named `TOM_API_URL` under **Settings →
Secrets and variables → Actions → Variables**. Set it to the backend's public
base URL, such as `https://your-service.onrender.com` (no trailing slash). The
workflow requires this variable and writes the URL into the published page. If
you change the variable, run the workflow again to publish the update.
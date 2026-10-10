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

## Deploy to Render

The `Build and deploy to Render` workflow validates the Flask app and triggers
a Render deployment whenever you push to `main`. The app serves both the page
and `/api/chat`, so it does not need a separate static-site host or
`TOM_API_URL`.

1. Create a **Web Service** on Render and connect this repository's `main`
   branch.
2. Set the build command to `pip install -r requirements.txt` and the start
   command to `gunicorn app:app --bind 0.0.0.0:$PORT`.
3. In the Render service settings, create a deploy hook and copy its URL.
4. In GitHub, open **Settings → Secrets and variables → Actions → Secrets**,
   create a repository secret named `RENDER_DEPLOY_HOOK_URL`, and paste the
   deploy hook URL as its value.
5. Disable Render's automatic deploy on push so that GitHub Actions is the
   single deployment trigger.

After setup, push to `main` or manually run the workflow from the repository's
**Actions** tab. The workflow runs a basic app smoke test before requesting a
Render deployment. You can open the service's public URL from the Render
dashboard once the first deployment completes.

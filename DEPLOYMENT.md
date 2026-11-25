# Task 12: Run, verify, and deploy

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The app expects `dataset/ted_talks_cleaned.csv` and `dataset/user_interactions.csv`.

## Verify the recommendation functions

Run from the repository root:

```powershell
python -m unittest discover -s tests -v
```

The checks cover content, collaborative, and hybrid outputs; duplicate removal and ranking; unknown users; empty seeds; invalid weights; and the Precision/Recall helper.

## Deploy with Streamlit Community Cloud

1. Commit the project to a GitHub repository. Include `app.py`, `src/`, `requirements.txt`, and the two required CSV files under `dataset/` only if their license permits redistribution.
2. Sign in to Streamlit Community Cloud and create an app from the repository.
3. Set the app's main file to `app.py` and deploy.
4. After deployment, test the live app with a known user, an alternate model mode, selected talk interests, and a user with no matching interaction history.

If the dataset cannot be redistributed, do not commit it to a public repository. Store it in an approved private location and modify the data-loading code to retrieve it securely. Deployment is not complete until the repository and data access have been configured and the live app has passed these checks.

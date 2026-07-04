# apsche_ai

A Flask web application for predicting the Human Development Index (HDI) from development indicators.

## Project structure

- `Flask/app.py` - Flask backend and prediction logic
- `Flask/templates/` - HTML templates for home, prediction, and result pages
- `Flask/static/css/style.css` - UI styling
- `Flask/templates/HDI.pkl` - trained HDI model file
- `Dataset/` - data files used for training
- `Training/` - notebook and model development files

## Run locally

1. Install dependencies:
   ```bash
   pip install flask pandas numpy scikit-learn
   ```
2. Run the app:
   ```bash
   cd Flask
   python app.py
   ```
3. Open in browser:
   - `http://127.0.0.1:5000`
   - or on other devices on the same network: `http://<your-pc-ip>:5000`

## Notes

- The app loads a pretrained model from `Flask/templates/HDI.pkl`.
- The prediction form accepts:
  - `LifeExpectancy`
  - `MeanYearsSchooling`
  - `ExpectedYearsSchooling`
  - `GNI perCapita`

## Deploy to Google Cloud Run

1. Install and authenticate Google Cloud SDK:
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```
2. Build the container and deploy from the `Flask` folder:
   ```bash
   cd Flask
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/apsche-ai
   gcloud run deploy apsche-ai --image gcr.io/YOUR_PROJECT_ID/apsche-ai --platform managed --region us-central1 --allow-unauthenticated
   ```
3. When deployment finishes, Cloud Run will give you a public URL.

### Important Cloud Run notes

- Cloud Run uses port `8080` by default, so `Flask/app.py` should run on port `8080`.
- If Cloud Run returns a URL, anyone can open it.
- Replace `YOUR_PROJECT_ID` with your actual Google Cloud project ID.

# Deployment Guide

This guide will help you deploy your Forward Trial application to various platforms.

## Prerequisites

Before deploying, make sure you have:
1. ✅ All your API keys and credentials ready
2. ✅ A GitHub account
3. ✅ The platform account you want to deploy to

## Option 1: Streamlit Cloud (Recommended)

### Step 1: Push to GitHub
1. Create a new repository on GitHub
2. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set the main file path: `main_for_stream.py`
6. Click "Deploy"

### Step 3: Configure Secrets
1. In your Streamlit Cloud app, go to "Settings" → "Secrets"
2. Add your secrets in TOML format:
   ```toml
   OPENAI_KEY = "sk-your-openai-key"
   MONGODB_URI = "your-mongodb-connection-string"
   GOOGLE_CLOUD_PROJECT = "your-google-cloud-project-id"
   GOOGLE_APPLICATION_CREDENTIALS = '{"type":"service_account","project_id":"your-project-id",...}'
   ```

## Option 2: Heroku

### Step 1: Install Heroku CLI
```bash
# Download and install from: https://devcenter.heroku.com/articles/heroku-cli
```

### Step 2: Deploy
```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set OPENAI_KEY="sk-your-openai-key"
heroku config:set MONGODB_URI="your-mongodb-connection-string"
heroku config:set GOOGLE_CLOUD_PROJECT="your-google-cloud-project-id"
heroku config:set GOOGLE_APPLICATION_CREDENTIALS='{"type":"service_account","project_id":"your-project-id",...}'

# Deploy
git push heroku main
```

## Option 3: Railway

### Step 1: Connect to Railway
1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository

### Step 2: Configure Environment Variables
1. Go to your project settings
2. Add environment variables:
   - `OPENAI_KEY`
   - `MONGODB_URI`
   - `GOOGLE_CLOUD_PROJECT`
   - `GOOGLE_APPLICATION_CREDENTIALS`

## Option 4: Render

### Step 1: Connect to Render
1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click "New" → "Web Service"
4. Connect your repository

### Step 2: Configure
- **Name**: Your app name
- **Environment**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `streamlit run main_for_stream.py --server.port=$PORT --server.address=0.0.0.0`

### Step 3: Add Environment Variables
Add the same environment variables as mentioned above.

## Environment Variables Required

For all platforms, you need these environment variables:

```bash
OPENAI_KEY=sk-your-openai-api-key
MONGODB_URI=your-mongodb-connection-string
GOOGLE_CLOUD_PROJECT=your-google-cloud-project-id
GOOGLE_APPLICATION_CREDENTIALS={"type":"service_account","project_id":"your-project-id","private_key_id":"your-private-key-id","private_key":"-----BEGIN PRIVATE KEY-----\nyour-private-key\n-----END PRIVATE KEY-----\n","client_email":"your-service@your-project.iam.gserviceaccount.com","client_id":"your-client-id","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/your-service%40your-project.iam.gserviceaccount.com"}
```

## Troubleshooting

### Common Issues:

1. **"Module not found" errors**
   - Make sure all dependencies are in `requirements.txt`

2. **"Secret not found" errors**
   - Check that environment variables are set correctly
   - For Streamlit Cloud, use TOML format in Secrets

3. **"Port already in use" errors**
   - Make sure your Procfile is correct
   - Check that the port configuration matches your platform

4. **"Google Cloud authentication failed"**
   - Verify your service account JSON is complete
   - Check that APIs are enabled in Google Cloud Console

### Getting Help:
- Check the platform's documentation
- Look at the deployment logs
- Verify your environment variables are set correctly

## Security Notes

⚠️ **Important Security Reminders:**
- Never commit your `.env` file to GitHub
- Use environment variables for all secrets
- Regularly rotate your API keys
- Monitor your usage to avoid unexpected charges 
# Local Setup

This is a Streamlit application for handling tuberculosis related queries with multilingual support and AI-powered responses.

## Prerequisites

Before running this application locally, you'll need:

1. **Python 3.8+** installed on your system
2. **OpenAI API Key** - Get one from [OpenAI Platform](https://platform.openai.com/api-keys)
3. **MongoDB Database** - Either local MongoDB or MongoDB Atlas
4. **Google Cloud Project** with the following APIs enabled:
   - Cloud Translation API
   - Cloud Text-to-Speech API
   - Cloud Speech-to-Text API (for future enhancement)
5. **Google Cloud Service Account** with appropriate permissions

## Setup Instructions

### 1. Clone and Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

### 2. Environment Configuration

1. Edit the `.env` file and fill in your credentials:

   ```env
   # OpenAI Configuration
   OPENAI_KEY=your_openai_api_key_here

   # MongoDB Configuration
   MONGODB_URI=mongodb://localhost:27017/your_database_name
   # OR for MongoDB Atlas:
   # MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/your_database_name

   # Google Cloud Configuration
   GOOGLE_CLOUD_PROJECT=your_google_cloud_project_id_here
   GOOGLE_APPLICATION_CREDENTIALS={"type":"service_account","project_id":"your_project_id","private_key_id":"your_private_key_id","private_key":"-----BEGIN PRIVATE KEY-----\nyour_private_key_here\n-----END PRIVATE KEY-----\n","client_email":"your_service_account_email@your_project.iam.gserviceaccount.com","client_id":"your_client_id","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":"https://www.googleapis.com/robot/v1/metadata/x509/your_service_account_email%40your_project.iam.gserviceaccount.com"}


   ```

### 3. Google Cloud Setup

1. Create a Google Cloud Project
2. Enable the required APIs:
   - Cloud Translation API
   - Cloud Text-to-Speech API
   - Cloud Speech-to-Text API (for future enhancement)
3. Create a Service Account with appropriate permissions
4. Download the service account key JSON file
5. Copy the contents of the JSON file to the `GOOGLE_APPLICATION_CREDENTIALS` environment variable

### 4. MongoDB Setup

#### Option A: Local MongoDB
1. Install MongoDB locally
2. Start MongoDB service
3. Create a database named `pdf_file`
4. Create a collection named `animal_bites`

#### Option B: MongoDB Atlas
1. Create a MongoDB Atlas account
2. Create a cluster
3. Get your connection string
4. Update the `MONGODB_URI` in your `.env` file

### 5. Run the Application

```bash
streamlit run main_for_stream.py
```

The application will be available at `http://localhost:8501`

## Features

- **Multilingual Support**: Supports English, Tamil, Telugu, and Hindi
- **AI-Powered Responses**: Uses OpenAI GPT models for intelligent responses
- **Translation Services**: Google Cloud Translation API integration
- **Text-to-Speech**: Google Cloud Text-to-Speech API integration
- **Speech-to-Text**: Google Cloud Speech-to-Text API integration (future enhancement)
- **Database Storage**: MongoDB integration for storing interactions
- **Forwarding System**: Print-based forwarding of unanswered questions to doctor

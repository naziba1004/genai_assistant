# AI Assistant with multiple models

A robust, Python-based Flask web application that creates an interactive AI Assistant. This application leverages LangChain to provide users with a dynamic interface to switch seamlessly between three state-of-the-art Large Language Models (LLMs):
* **Llama** (via IBM watsonx.ai)
* **Mistral** (via IBM watsonx.ai)
* **Gemini** (via Google AI Studio)

The architecture uses **Poetry** for secure, deterministic dependency management and is completely containerized via **Docker**.

---

## 🛠️ Prerequisites & Infrastructure Setup

Before configuring the software, you must set up your cloud provider infrastructure to obtain the necessary credentials.

### 1. Google AI Configuration
1. Go to the [Google AI Studio Console](https://aistudio.google.com/) (or Google Cloud Vertex AI console).
2. Generate an API Key. This will be used to authenticate your Gemini model requests.

### 2. IBM Cloud & watsonx.ai Configuration
IBM watsonx core services require API access scoped through an isolated runtime environment.
1. **Provision a Compute Instance:** Go to the [IBM Cloud Catalog](https://cloud.ibm.com/catalog) and ensure you have an active **watsonx.ai Runtime** (formerly Watson Machine Learning) instance on your account (preferably in the `Dallas (us-south)` region).
2. **Create a Deployment Space:** * Navigate to the watsonx **Deployments** dashboard.
   * Click **New deployment space +**.
   * Link it directly to your existing watsonx.ai Runtime instance.
3. **Retrieve the Space ID:** Go to your newly created Deployment Space -> **Manage** tab -> **General** settings. Copy the alphanumeric **Space ID** GUID.
4. **Generate an IAM API Key:** Go to **Manage > Access (IAM) > API keys** in your IBM Cloud dashboard and generate a fresh master platform token.

---

## ⚙️ How to Run

The application expects credentials to be securely split between system environment variables (for secrets) and a local configuration file (for environment variables and platform identifiers).

### 1. Environment Variables (`.env`)
Create a `.env` file in the root directory of your project to store your secret API keys safely. 

```env
# Google AI Studio API Key for Gemini
GOOGLE_API_KEY="your_google_gemini_api_key_here"

# IBM Cloud Platform IAM API Key for watsonx
WATSONX_APIKEY="your_ibm_cloud_iam_api_key_here"
```

### 2. Build & run docker container

Build the docker container with Dockerfile.

```
docker build -t genai_assistant .
```

Run the docker container in order to start the flask server

```
docker run -it -p 5000:5000 --env-file .env genai_assistant
```

To access the interface, open your browser and navigate to http://127.0.0.1:5000/
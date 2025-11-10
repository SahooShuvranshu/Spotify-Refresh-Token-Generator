# 🎵 Spotify Token Generator - Super Easy Edition!

<div align="center">

![Spotify](https://img.shields.io/badge/Spotify-1DB954?style=for-the-badge&logo=spotify&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### 🚀 The Easiest Way to Get Your Spotify Tokens!

**No coding skills needed! Just click, paste, and you're done in 2 minutes!**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

[Why This Rocks](#-why-youll-love-this) • [Get Started Now](#-get-started-host-your-own) • [Host Your Own](#-get-started-host-your-own) • [Use Your Tokens](#-now-what-use-your-tokens)

</div>

---

## 📚 Table of Contents

* [Wait... What Even Is This?](#-wait-what-even-is-this)
* [Why You'll Love This](#-why-youll-love-this)
* [Get Started (Host Your Own)](#-get-started-host-your-own)
    * [1-Click Deploy (Easiest)](#-1-click-deploy-easiest)
    * [Run Locally](#-run-locally)
* [How to Use It (The 3-Step Dance)](#-how-to-use-it-the-3-step-dance)
* [Now What? Use Your Tokens!](#-now-what-use-your-tokens)
* [Project Details (For Developers)](#-project-details-for-developers)
    * [Configuration](#️-configuration)
    * [Project Structure](#-project-structure)
    * [API Endpoints](#-api-endpoints)
    * [Security](#-security)
* [Troubleshooting](#-troubleshooting)
* [Need Help? Join Our Community!](#-need-help-join-our-community)
* [Contributing](#-contributing)
* [License](#-license)

---

## 🎯 Wait... What Even Is This?

Great question! Here's the deal:

You know how you want to show off what music you're listening to on your website or Discord? Or maybe build a cool Spotify widget? Well, you need something called a **"refresh token"** to make that happen.

Getting that token usually involves typing scary terminal commands and reading boring documentation. 😴

**This tool?** It gives you a pretty website where you just click a few buttons, paste some stuff, and BAM! You get your token. No headaches, no confusion!

### 🤔 Why Would I Want This?

Use your tokens to build cool stuff like:

* 🎨 **Show your current song** on your personal website
* 🤖 **Spotify Discord bots** that respond to what you're playing
* 📊 **Data dashboards** with your listening stats
* 🏠 **Smart home integrations** (Alexa, read my Spotify playlists!)
* 🎮 **Gaming overlays** showing your music during streams
* 📱 **Mobile apps** that need Spotify data

Basically, if it involves Spotify + coding, you'll need tokens!

---

## 🚀 Why You'll Love This

Here's what makes this tool awesome:

| 🎨 **Super Easy** | Just click buttons - no terminal commands or code to copy-paste! |
| :--- | :--- |
| 🔒 **100% Safe** | We don't store ANYTHING. Your secrets stay secret! |
| ⚡ **Lightning Fast** | Get your token in literally 2 minutes |
| 📱 **Works Everywhere** | Phone? Tablet? Computer? All good! |
| 🎉 **Looks Beautiful** | Spotify green theme that doesn't hurt your eyes |
| 🆓 **Free Forever** | Host it yourself for free on any platform |
| 🌍 **Host Anywhere** | Render, Railway, Heroku, Vercel - take your pick! |
| 🤖 **Auto-Magic Setup** | No config files to mess with - it just works! |

---

## 🚀 Get Started (Host Your Own)

### 🟢 1-Click Deploy (Easiest)

Pick your favorite platform and click the button.

#### Render (Recommended)
**Why Render?** Free tier, automatic HTTPS, reliable uptime.

1.  Click ➡️ [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
2.  Connect your GitHub (they'll guide you).
3.  Give it a name (e.g., `my-spotify-tokens`).
4.  Fill in the details:
    * **Build Command:** `pip install -r requirements.txt`
    * **Start Command:** `gunicorn app:app`
5.  Click "Create Web Service".
6.  Wait 2-3 minutes ☕
7.  **Important:** Go to your [Spotify Dashboard](https://developer.spotify.com/dashboard/) and add your new Render URL + `/callback` to the Redirect URIs.
    * Example: `https://my-spotify-tokens.onrender.com/callback`

#### Railway
**Why Railway?** Simple setup, automatic deployments.

1.  Click ➡️ [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)
2.  Sign in with GitHub.
3.  Click "Deploy Now".
4.  Wait 2 minutes ⏰
5.  **Important:** Go to your [Spotify Dashboard](https://developer.spotify.com/dashboard/) and add your new Railway URL + `/callback` to the Redirect URIs.
    * Example: `https://my-app.railway.app/callback`

#### Heroku
**Why Heroku?** Industry standard, robust platform.

1.  Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2.  Open your terminal and run:
    ```bash
    git clone [https://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator.git](https://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator.git)
    cd Spotify-Refresh-Token-Generator
    heroku create my-cool-token-generator
    git push heroku main
    ```
3.  **Important:** Go to your [Spotify Dashboard](https://developer.spotify.com/dashboard/) and add your new Heroku URL + `/callback` to the Redirect URIs.
    * Example: `https://my-cool-token-generator.herokuapp.com/callback`

#### Vercel
**Why Vercel?** Blazing fast, great for serverless.

1.  Install Vercel CLI: `npm i -g vercel`
2.  Run: `vercel --prod`
3.  Follow the prompts.
4.  **Important:** Go to your [Spotify Dashboard](https://developer.spotify.com/dashboard/) and add your new Vercel URL + `/callback` to the Redirect URIs.
    * Example: `https://your-app.vercel.app/callback`

---

### 🛠️ Run Locally

Want to run it on your own computer?

1.  **Get the code**
    ```bash
    git clone [https://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator.git](https://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator.git)
    cd Spotify-Refresh-Token-Generator
    ```

2.  **Set up Python stuff** (one-time thing)
    ```bash
    python -m venv venv
    
    # Windows users:
    venv\Scripts\activate
    
    # Mac/Linux users:
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run it!**
    ```bash
    python app.py
    ```

5.  **Open your browser** and go to: `http://localhost:5000`
6.  **Important:** Go to your [Spotify Dashboard](https://developer.spotify.com/dashboard/) and add `http://localhost:5000/callback` to your Redirect URIs.

---

## 🎮 How to Use It (The 3-Step Dance)

Okay, your token generator is live! Now what? Let's get those tokens!

### Step 1️⃣: Create a Spotify App
1.  **Visit your deployed URL** (the one you just created!)
2.  **Click the big green button** that says "📝 Create Spotify App".
3.  **You're now on Spotify Dashboard!** Fill this out:
    ```
    App Name: My Awesome Token Generator
    App Description: Getting tokens like a boss!
    Redirect URI: [paste your URL from the generator]/callback
    ```
    Example: `https://my-tokens.onrender.com/callback`
4.  **Click "Save"**.
5.  **Copy these two things:**
    * Client ID
    * Client Secret (click "Show Client Secret", then copy)

### Step 2️⃣: Authorize Your Spotify
1.  **Go back to your token generator** website.
2.  **Paste** your Client ID and Client Secret into the boxes.
3.  **Click "🚀 Authorize with Spotify"**.
4.  **Spotify asks permission** - Click "Agree"!

### Step 3️⃣: Get Your Refresh Token
1.  You'll be redirected back to your app.
2.  **Enter your Client Secret** again (security!).
3.  **Click "🎯 Get Refresh Token"**.
4.  **BOOM!** 💥 You now see your **REFRESH_TOKEN**.
5.  **Copy all three** (Client ID, Client Secret, Refresh Token) and save them somewhere safe!

---

## 🎨 Now What? Use Your Tokens!

Got your tokens? Awesome! Here's how to USE them in your projects!

### For the [Spotify Live Banner](https://github.com/SahooShuvranshu/Spotify-Live-Banner) Project

#### 🏠 Running Locally?
1.  Create a `.env` file in your project folder.
2.  Open `.env` and paste your tokens:
    ```env
    SPOTIFY_CLIENT_ID=paste_your_client_id_here
    SPOTIFY_CLIENT_SECRET=paste_your_client_secret_here
    SPOTIFY_REFRESH_TOKEN=paste_your_refresh_token_here
    ```
3.  Save and run your app! It'll automatically use these tokens!

#### 🌐 Deploying to the Internet?
Add these as **Environment Variables** in your hosting platform (Render, Railway, Heroku, etc.):

* `SPOTIFY_CLIENT_ID` = `paste_your_client_id_here`
* `SPOTIFY_CLIENT_SECRET` = `paste_your_client_secret_here`
* `SPOTIFY_REFRESH_TOKEN` = `paste_your_refresh_token_here`

Your app will read these variables and start working!

---

## 🔬 Project Details (For Developers)

### ⚙️ Configuration

You can use Environment Variables to configure the app.

| Variable | Description | Required | Default |
| :--- | :--- | :--- | :--- |
| `REDIRECT_URI` | OAuth callback URL | No | Auto-detected |
| `PORT` | Server port | No | `5000` |
| `FLASK_ENV` | Flask environment | No | `production` |

### 📁 Project Structure

```text
Token-Generator/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── Procfile                    # Heroku process file
├── runtime.txt                 # Python version specification
├── render.yaml                 # Render deployment config
├── vercel.json                 # Vercel deployment config
├── test_app.py                 # Unit tests
├── README.md                   # This file
│
└── templates/                  # HTML templates
├── index.html             # Home page with OAuth flow
└── callback.html          # Token display page
```


### 🔌 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET /` | Home page | Serves the main HTML page. |
| `POST /start` | Initiate Auth | Takes `client_id` and returns a Spotify `auth_url`. |
| `GET /callback` | Spotify Callback | Handles the redirect from Spotify, contains `code`. |
| `POST /exchange` | Get Token | Exchanges `code`, `client_id`, `client_secret` for tokens. |
| `GET /health` | Health Check | Returns `OK` (200 status). |

### 🔒 Security

This application is designed with security as a top priority:

| Feature | Implementation |
| :--- | :--- |
| **No Database** | Zero persistent storage of credentials. |
| **Session-Only Storage** | Credentials are cleared after the token is generated. |
| **HTTPS Enforced** | All production deployments use SSL/TLS. |
| **No Server-Side Storage** | Server only facilitates the OAuth flow. |

**Best Practices for Users:**
1.  **Never share your Client Secret** - Treat it like a password.
2.  **Use HTTPS URLs** - Always deploy with SSL.
3.  **Revoke unused apps** - Delete old apps from your Spotify Dashboard.

---

## 😅 Troubleshooting

Don't panic! Here are fixes for common issues:

#### ❌ "Invalid redirect URI" Error
* **Problem:** Spotify doesn't recognize your callback URL.
* **Solution:** Go to your [Spotify Dashboard](https://developer.spotify.com/dashboard/). Click your app -> Edit Settings. Make SURE the redirect URI is **EXACTLY** `https://your-exact-url.com/callback`. No typos! No extra `/` at the end!

#### ❌ "Invalid client" Error
* **Problem:** Wrong Client ID or Client Secret.
* **Solution:** Go back to your Spotify Dashboard and carefully copy the Client ID and Client Secret again. Ensure there are no extra spaces.

#### ❌ "Authorization code expired" Error
* **Problem:** You took too long (more than 10 minutes) to exchange the code.
* **Solution:** Just start the process over from Step 1. Be faster this time! ⚡

#### ❌ App Not Loading After Deployment
* **Problem:** Something went wrong during deployment.
* **Solution:** Check your platform's logs (Render, Railway, etc.). The error message is usually there. Make sure your `Start Command` is `gunicorn app:app`.

---

## 💬 Need Help? Join Our Community!

### 🎮 Discord Support Server

[![Discord](https://img.shields.io/badge/Discord-Join%20Server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/your-invite-link)

**Get help from the community!**

* 💡 Ask questions and get instant answers
* 🤝 Share your projects built with this tool
* 🐛 Report bugs and get support
* 🎉 Connect with other developers
* 📢 Get updates on new features

**[Click here to join our Discord server!](https://discord.gg/your-invite-link)**

---

## 🤝 Contributing

Contributions are welcome!

### Reporting Bugs
1.  Check existing [Issues](httpss://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator/issues).
2.  If it's a new bug, create a new issue with steps to reproduce.

### Submitting Pull Requests
1.  Fork the repository.
2.  Create a feature branch: `git checkout -b feature/amazing-feature`
3.  Make your changes and test them locally.
4.  Commit your changes: `git commit -m 'Add amazing feature'`
5.  Push to the branch: `git push origin feature/amazing-feature`
6.  Open a Pull Request!

---

## 📄 License

This project is licensed under the **MIT License**.
Basically, do whatever you want with this code!

---

## 🌟 Show Some Love!

If this tool helped you, consider:

* ⭐ **Starring this repo!**
* 🍴 **Forking it** to make your own version.
* 💌 **Sharing it** with other developers.

<div align="center">

**[⬆ Back to Top](#-spotify-token-generator---super-easy-edition)**

</div>

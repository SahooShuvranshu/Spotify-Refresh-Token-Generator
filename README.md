# 🎵 Spotify Token Generator - Super Easy Edition!

<div align="center">

![Spotify](https://img.shields.io/badge/Spotify-1DB954?style=for-the-badge&logo=spotify&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### � The Easiest Way to Get Your Spotify Tokens!

**No coding skills needed! Just click, paste, and you're done in 2 minutes!**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

[Why This Rocks](#-why-youll-love-this) • [Get Started Now](#-get-started-in-5-minutes) • [Host Your Own](#-host-your-own-version-free) • [Use Your Tokens](#-now-what-use-your-tokens)

</div>

---

## 🎯 Wait... What Even Is This?

Great question! Here's the deal:

You know how you want to show off what music you're listening to on your website or Discord? Or maybe build a cool Spotify widget? Well, you need something called a **"refresh token"** to make that happen.

Getting that token usually involves typing scary terminal commands and reading boring documentation. 😴

**This tool?** It gives you a pretty website where you just click a few buttons, paste some stuff, and BAM! You get your token. No headaches, no confusion!

### 🤔 Why Would I Want This?

Use your tokens to build cool stuff like:

- 🎨 **Show your current song** on your personal website
- 🤖 **Spotify Discord bots** that respond to what you're playing
- 📊 **Data dashboards** with your listening stats
- 🏠 **Smart home integrations** (Alexa, read my Spotify playlists!)
- 🎮 **Gaming overlays** showing your music during streams
- 📱 **Mobile apps** that need Spotify data

Basically, if it involves Spotify + coding, you'll need tokens!

---

## 🚀 Why You'll Love This

Here's what makes this tool awesome:

| 🎨 **Super Easy** | Just click buttons - no terminal commands or code to copy-paste! |
| 🔒 **100% Safe** | We don't store ANYTHING. Your secrets stay secret! |
| ⚡ **Lightning Fast** | Get your token in literally 2 minutes |
| 📱 **Works Everywhere** | Phone? Tablet? Computer? All good! |
| 🎉 **Looks Beautiful** | Spotify green theme that doesn't hurt your eyes |
| 🆓 **Free Forever** | Host it yourself for free on any platform |
| 🌍 **Host Anywhere** | Render, Railway, Heroku, Vercel - take your pick! |
| 🤖 **Auto-Magic Setup** | No config files to mess with - it just works! |

---

## � Get Started in 5 Minutes

### Option 1: Use Someone Else's Version (Easiest!)

If someone already hosted this tool, just use their link! They'll share something like:
```
🎵 Need Spotify tokens? Use my generator:
👉 https://spotify-tokens.onrender.com
```

**That's it!** Go there, follow the steps on screen, get your tokens!

### Option 2: Host Your Own Version (Also Easy!)

Want to be the hero who helps everyone get tokens? Host your own copy! Here's how:

#### 🎯 The "I Want It Now" Method (1-Click Deploy)

Pick your favorite platform and click the button:

**🟢 Render (Recommended - It's Free!)**
1. Click ➡️ [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
2. Connect your GitHub (they'll guide you)
3. Click "Create Web Service"
4. Wait 2-3 minutes ☕
5. Done! You get a URL like `https://your-awesome-token-generator.onrender.com`

**🟣 Railway (Also Great & Free!)**
1. Click ➡️ [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)
2. Sign in with GitHub
3. Click "Deploy Now"
4. Wait 2 minutes ⏰
5. Done! Get your URL and share it!

**💜 Heroku (Classic Choice)**
```bash
# Install Heroku CLI first, then:
git clone https://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator.git
cd Spotify-Refresh-Token-Generator
heroku create my-cool-token-generator
git push heroku main
# Your app is live! 🎉
```

#### 🛠️ The "I Like to Tinker" Method (Run Locally)

Want to run it on your computer first? Sure!

1. **Get the code**
   ```bash
   git clone https://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator.git
   cd Spotify-Refresh-Token-Generator
   ```

2. **Set up Python stuff** (one-time thing)
   ```bash
   python -m venv venv
   
   # Windows users:
   venv\Scripts\activate
   
   # Mac/Linux users:
   source venv/bin/activate
   ```

3. **Install dependencies** (fancy word for "needed stuff")
   ```bash
   pip install -r requirements.txt
   ```

4. **Run it!**
   ```bash
   python app.py
   ```

5. **Open your browser** and go to: `http://localhost:5000`

   🎉 **Boom!** Your token generator is running!

> **⚠️ Important:** If running locally, add `http://localhost:5000/callback` to your Spotify app settings!

---

## 📝 Table of Contents

**Quick Links:**
- [Why You'll Love This](#-why-youll-love-this)
- [Get Started in 5 Minutes](#-get-started-in-5-minutes)
- [Host Your Own Version (FREE!)](#-host-your-own-version-free)
- [How to Actually Use It](#-how-to-actually-use-it)
- [Now What? Use Your Tokens!](#-now-what-use-your-tokens)
- [Oops! Something Broke](#-oops-something-broke)
- [Want to Help?](#-want-to-help-make-this-better)

---

## 🎪 Host Your Own Version (FREE!)

Okay, so you want to host your own copy? Smart move! Here's a super detailed guide for each platform:

### 🟢 Render - The Easiest Option

**Why Render?** Free, automatic HTTPS, no credit card needed, stays awake!

**Step-by-Step:**

1. **Fork this repo** (top right on GitHub, click the Fork button 🍴)

2. **Go to** [Render.com](https://render.com) and sign up (free!)

3. **Click "New +"** at the top → Choose **"Web Service"**

4. **Connect your GitHub** 
   - Render will ask permission (click yes)
   - Find your forked repo in the list

5. **Fill in the details:**
   - **Name:** `spotify-token-generator` (or anything cool!)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Free Plan:** YES! (it's free forever)

6. **Click "Create Web Service"**

7. **Wait 2-3 minutes** ⏰ (Render is building your app!)

8. **Get your URL!** It'll look like: `https://spotify-token-generator-abc123.onrender.com`

9. **ONE MORE THING!** 🚨 
   - Go to [Spotify Dashboard](https://developer.spotify.com/dashboard)
   - Open your Spotify app settings
   - Add this Redirect URI: `https://your-render-url.onrender.com/callback`
   - Click Save!

🎉 **DONE!** Share your URL with friends!

🎉 **DONE!** Share your URL with friends!

### 🟣 Railway - Super Simple Too!

**Why Railway?** Auto-detects everything, no config needed, also free!

**Step-by-Step:**

1. **Fork this repo** on GitHub

2. **Go to** [Railway.app](https://railway.app) → Sign in with GitHub

3. **Click "New Project"** → **"Deploy from GitHub repo"**

4. **Select your fork** of this repo

5. **Railway auto-magically detects** it's a Python app! 🎩✨

6. **Click "Deploy"** 

7. **Wait 2 minutes** ⏰

8. **Click on your deployment** → Find the URL (looks like `https://your-app.railway.app`)

9. **Add to Spotify:**
   - Go to [Spotify Dashboard](https://developer.spotify.com/dashboard)
   - Add redirect URI: `https://your-app.railway.app/callback`

🚀 **You're live!** Tell everyone!

### 💜 Heroku - The Classic

**Why Heroku?** Been around forever, super reliable, tons of tutorials online!

**Step-by-Step:**

1. **Install Heroku CLI:** Download from [heroku.com/cli](https://devcenter.heroku.com/articles/heroku-cli)

2. **Open terminal** and login:
   ```bash
   heroku login
   ```
   (This opens a browser window - click login)

3. **Clone and deploy:**
   ```bash
   git clone https://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator.git
   cd Spotify-Refresh-Token-Generator
   heroku create my-token-generator
   git push heroku main
   ```

4. **Get your URL:**
   ```bash
   heroku open
   ```

5. **Add to Spotify** as redirect URI: `https://my-token-generator.herokuapp.com/callback`

🎊 **Live and ready!**

### ▲ Vercel - For the Speedsters

**Why Vercel?** Blazing fast, great for serverless!

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy!
cd Spotify-Refresh-Token-Generator
vercel --prod
```

Follow the prompts, get your URL, add `/callback` to Spotify settings! ✅

---

## 🎮 How to Actually Use It

Okay, your token generator is live! Now what? Let's get those tokens!

### 🎯 The 3-Step Dance

**Step 1️⃣: Create a Spotify App** (Don't worry, it's not real coding!)

1. **Visit your deployed URL** (the one you just created!)

2. **Click the big green button** that says "📝 Create Spotify App"

3. **You're now on Spotify Dashboard!** Fill this out:
   ```
   App Name: My Awesome Token Generator
   App Description: Getting tokens like a boss!
   Redirect URI: [paste your URL from the generator]/callback
   ```
   Example: `https://my-tokens.onrender.com/callback`

4. **Click "Save"** 

5. **Copy these two things:**
   - Client ID (long string of letters and numbers)
   - Client Secret (click "Show Client Secret", then copy)

**Step 2️⃣: Authorize Your Spotify** (This is where the magic happens!)

1. **Go back to your token generator** website

2. **Paste** your Client ID and Client Secret into the boxes

3. **Click "🚀 Authorize with Spotify"**

4. **Spotify asks permission** - Click "Agree"!
   - It wants to see what you're listening to
   - This is normal and safe! ✅

5. **You'll be redirected back** - See that code? That's step 1 done!

**Step 3️⃣: Get Your Refresh Token** (The finale!)

1. **Enter your Client Secret** again (security!)

2. **Click "🎯 Get Refresh Token"**

3. **BOOM!** 💥 You now see THREE things:
   ```
   CLIENT_ID: abcd1234...
   CLIENT_SECRET: xyz789...
   REFRESH_TOKEN: BQD7x8...
   ```

4. **Copy all three** - you'll need them!

5. **Don't share these** with anyone! They're like your Spotify password!

🎉 **Congratulations!** You just got your Spotify tokens!

---

## 🎨 Now What? Use Your Tokens!

Got your tokens? Awesome! Here's how to actually USE them in your projects!

### 🚀 For the [Spotify Live Banner](https://github.com/SahooShuvranshu/Spotify-Live-Banner) Project

Want to show what you're listening to on your website? Here's how:

#### � Running Locally?

1. **Create a `.env` file** in your project folder:

   ```bash
   # Windows PowerShell:
   New-Item -Path .env -ItemType File
   
   # Mac/Linux:
   touch .env
   ```

2. **Open `.env` and paste** your tokens:

   ```env
   SPOTIFY_CLIENT_ID=paste_your_client_id_here
   SPOTIFY_CLIENT_SECRET=paste_your_client_secret_here
   SPOTIFY_REFRESH_TOKEN=paste_your_refresh_token_here
   ```

3. **Save** and run your app! It'll automatically use these tokens!

#### 🌐 Deploying to the Internet?

Add these as **Environment Variables** in your hosting platform:

**🟢 On Render:**
1. Open your web service dashboard
2. Click "Environment" on the left
3. Click "Add Environment Variable"
4. Add each one:
   ```
   Key: SPOTIFY_CLIENT_ID
   Value: [paste your client ID]
   
   Key: SPOTIFY_CLIENT_SECRET  
   Value: [paste your client secret]
   
   Key: SPOTIFY_REFRESH_TOKEN
   Value: [paste your refresh token]
   ```
5. Click "Save Changes"
6. App auto-restarts! 🔄

**🟣 On Railway:**
1. Go to your project
2. Click "Variables" tab
3. Click "New Variable"
4. Add all three (same names as above)
5. Deploy automatically happens! ✨

**💜 On Heroku:**
1. Go to your app dashboard
2. Click "Settings" → "Reveal Config Vars"
3. Add all three variables
4. Done!

Or use terminal:
```bash
heroku config:set SPOTIFY_CLIENT_ID="your_id"
heroku config:set SPOTIFY_CLIENT_SECRET="your_secret"
heroku config:set SPOTIFY_REFRESH_TOKEN="your_token"
```

### 🎯 What Do These Tokens Actually Do?

Here's the magic behind the scenes:

```python
# Your app uses the tokens like this:

1. 🔑 Takes your REFRESH_TOKEN
2. 🤝 Asks Spotify: "Hey, can I get an access token?"
3. ✅ Spotify says: "Sure! Here's one (valid for 1 hour)"
4. 📱 App uses ACCESS_TOKEN to fetch your current song
5. ⏰ After 1 hour, it automatically refreshes using REFRESH_TOKEN
6. � Repeat forever!
```

**Translation:** Your tokens let your app check what you're listening to on Spotify, automatically, forever! 🎵

### ✅ How to Know It's Working

After adding your tokens:

1. **Start playing a song** on Spotify (any device!)
2. **Open your app** in a browser
3. **You should see:**
   - 🎵 Song name
   - 🎤 Artist name  
   - � Album art
   - ▶️ Play button animation

4. **Not working?** Check:
   - ✅ All three tokens are set correctly
   - ✅ No extra spaces when you copied them
   - ✅ You're actually playing music on Spotify
   - ✅ Check the app logs for error messages

---

## � Is This Safe? (Yes!)

**Your tokens are secure because:**

✅ **Nothing Gets Stored** - The generator processes tokens in memory only
✅ **No Database** - We don't save anything, ever
✅ **HTTPS Only** - All communication is encrypted (when deployed)
✅ **You Control Everything** - Host it yourself, see all the code
✅ **Open Source** - Anyone can audit the code for security issues

**To Stay Safe:**

- 🚫 **Never** share your Client Secret or Refresh Token publicly
- 🚫 **Never** commit `.env` files to GitHub (add to `.gitignore`!)
- ✅ **DO** use environment variables for tokens
- ✅ **DO** regenerate tokens if you think they're compromised
- ✅ **DO** delete old Spotify apps you're not using

**Think of tokens like this:**
- Client ID = Your username (okay to share)
- Client Secret = Your password (NEVER share!)
- Refresh Token = Your session cookie (NEVER share!)

---

## 😅 Oops! Something Broke?

**Don't panic!** Here are fixes for common issues:

### ❌ "Invalid redirect URI"

**What happened:** Spotify doesn't recognize your callback URL

**Fix it:**
1. Go to [Spotify Dashboard](https://developer.spotify.com/dashboard)
2. Click your app → Edit Settings
3. Make SURE the redirect URI is **EXACTLY**:
   ```
   https://your-exact-url.com/callback
   ```
   (No typos! No trailing slashes! Case matters!)
4. Click Save

### ❌ "Invalid client"

**What happened:** Wrong Client ID or Client Secret

**Fix it:**
1. Go back to Spotify Dashboard
2. Copy Client ID again (fresh copy!)
3. Click "Show Client Secret" → Copy it
4. Try again with new copies
5. Still broken? Create a brand new Spotify app!

### ❌ "App not loading" after deployment

**What happened:** Something went wrong during deployment

**Fix it:**
1. Check your platform's logs:
   - **Render:** Dashboard → Logs tab
   - **Railway:** Click deployment → View logs
   - **Heroku:** `heroku logs --tail`

2. Common issues:
   - Missing `requirements.txt`? Download from this repo
   - Wrong Python version? Check `runtime.txt`
   - Wrong start command? Should be `gunicorn app:app`

### ❌ "Token expired" error

**What happened:** You took too long! Auth codes expire in 10 minutes

**Fix it:**
- Just start over from Step 1
- Be faster this time! ⚡

### ❌ "Can't find my deployed URL"

**Find it here:**
- **Render:** Dashboard → Your service → URL at top
- **Railway:** Project → Deployments → Domain
- **Heroku:** `heroku info` or check dashboard
- **Vercel:** After deploy, they show you the URL

### 🆘 Still Stuck?

1. **Read the error message carefully** - it usually tells you what's wrong!
2. **Google the error** - someone else probably had the same issue
3. **Check GitHub Issues** - maybe it's a known bug
4. **Ask for help** - open an issue on this repo!

---

## 🎨 Want to Customize It?

This tool is open source - make it your own!

### Change the Colors

Edit `templates/index.html` and `templates/callback.html`:

```html
<!-- Find this line in the <style> section: -->
<style>
    body {
        background: linear-gradient(135deg, #1DB954 0%, #191414 100%);
        /* Change #1DB954 to YOUR color! */
        /* Try: #FF6B6B (red), #4ECDC4 (teal), #FFE66D (yellow) */
    }
</style>
```

### Add More Permissions

Want more than just "currently playing"? Edit `app.py`:

```python
# Find this line:
scopes = "user-read-currently-playing user-read-recently-played"

# Add more scopes:
scopes = "user-read-currently-playing user-read-recently-played user-top-read playlist-read-private"
```

[See all possible scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes)

### Change the App Name

Look cool! Edit the titles in `templates/index.html`:

```html
<title>YOUR AWESOME NAME HERE - Spotify Token Generator</title>
<h1>🎵 YOUR BRANDING HERE</h1>
```

---

## 🤝 Want to Help Make This Better?

**Contributions welcome!** Here's how you can help:

### 🐛 Found a Bug?

1. Check if someone already reported it
2. If not, [open an issue](https://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator/issues)
3. Tell us:
   - What you tried to do
   - What happened instead
   - Screenshots help A LOT!

### 💡 Have an Idea?

Open an issue with `[IDEA]` in the title and tell us your brilliant idea!

### 🛠️ Want to Code?

1. Fork this repo
2. Create a branch: `git checkout -b my-cool-feature`
3. Make your changes
4. Test it locally!
5. Commit: `git commit -m "Added cool feature"`
6. Push: `git push origin my-cool-feature`
7. Open a Pull Request!

**We love:**
- 🐛 Bug fixes
- 📝 Better documentation
- 🎨 UI improvements
- 🌍 Translations to other languages
- ⚡ Performance improvements

---

## 📄 License

**MIT License** - basically, do whatever you want with this code!

```
Free to use ✅
Free to modify ✅  
Free to distribute ✅
Free to sell ✅
Just keep the license file ✅
```

Full license in the [LICENSE](LICENSE) file.

---

## 🙌 Credits & Thanks

**Built with:**
- 🐍 Python & Flask - The backend magic
- 🎨 Pure CSS - No frameworks, just vibes
- 💚 Spotify API - The data source
- ❤️ Love - For the developer community!

**Special thanks to:**
- Spotify for their awesome API
- Everyone who starred this repo ⭐
- All contributors who made this better
- YOU for reading this far! 🎉

---

## 🎉 You Did It!
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   - Navigate to `http://localhost:5000`
   - Add `http://localhost:5000/callback` to your Spotify app's redirect URIs

---

## 🌐 Deployment Options

### Option 1: Render (⭐ Recommended)

**Why Render?** Free tier, automatic HTTPS, easy deployment, reliable uptime.

1. Fork this repository to your GitHub account
2. Sign up at [Render.com](https://render.com)
3. Click **"New +" → "Web Service"**
4. Connect your GitHub repository
5. Configure:
   - **Name:** `spotify-token-generator` (or any name)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
6. Click **"Create Web Service"**
7. Wait 2-3 minutes for deployment
8. Get your URL: `https://your-app-name.onrender.com`
9. **Important:** Add `https://your-app-name.onrender.com/callback` to Spotify app redirect URIs

### Option 2: Railway

**Why Railway?** Simple setup, automatic deployments, great developer experience.

1. Sign up at [Railway.app](https://railway.app)
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Connect your repository
4. Railway auto-detects configuration
5. Deploy and get your URL
6. Add `https://your-app.railway.app/callback` to Spotify redirect URIs

### Option 3: Heroku

**Why Heroku?** Industry standard, robust platform, extensive documentation.

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login to Heroku:
   ```bash
   heroku login
   ```
3. Create app:
   ```bash
   heroku create your-app-name
   ```
4. Deploy:
   ```bash
   git push heroku main
   ```
5. Add `https://your-app-name.herokuapp.com/callback` to Spotify redirect URIs

### Option 4: Vercel

**Why Vercel?** Lightning-fast deployment, optimized for serverless.

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```
2. Deploy:
   ```bash
   vercel --prod
   ```
3. Follow prompts and get your URL
4. Add `https://your-app.vercel.app/callback` to Spotify redirect URIs

### Option 5: Docker (Any Platform)

**Why Docker?** Consistent environment, works anywhere, easy scaling.

1. Build image:
   ```bash
   docker build -t spotify-token-generator .
   ```
2. Run container:
   ```bash
   docker run -p 5000:5000 spotify-token-generator
   ```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Default | Example |
|----------|-------------|----------|---------|---------|
| `REDIRECT_URI` | OAuth callback URL | No | Auto-detected | `https://myapp.com/callback` |
| `PORT` | Server port | No | `5000` | `8080` |
| `FLASK_ENV` | Flask environment | No | `production` | `development` |

### Setting Environment Variables

**Render:**
```
Dashboard → Environment → Add Environment Variable
```

**Railway:**
```
Project → Variables → New Variable
```

**Heroku:**
```bash
heroku config:set REDIRECT_URI=https://yourapp.com/callback
```

**Local (.env file):**
```bash
REDIRECT_URI=http://localhost:5000/callback
PORT=5000
FLASK_ENV=development
```

---

## 📁 Project Structure

```
Token-Generator/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── Procfile                    # Heroku process file
├── runtime.txt                 # Python version specification
├── render.yaml                 # Render deployment config
├── railway.json                # Railway deployment config
├── app.json                    # Heroku app manifest
├── vercel.json                 # Vercel deployment config
├── test_app.py                 # Unit tests
├── README.md                   # This file
│
├── templates/                  # HTML templates
│   ├── index.html             # Home page with OAuth flow
│   └── callback.html          # Token display page
│
└── __pycache__/               # Python cache (auto-generated)
```

### Key Files Explained

- **`app.py`** - Core Flask application with OAuth routes
- **`templates/index.html`** - User-facing interface for initiating OAuth
- **`templates/callback.html`** - Success page displaying refresh token
- **`requirements.txt`** - Flask, Requests, Gunicorn dependencies
- **Deployment configs** - Platform-specific configuration files

---

## 🔒 Security

This application is designed with security as a top priority:

### ✅ Security Features

| Feature | Implementation |
|---------|---------------|
| **No Database** | Zero persistent storage of credentials |
| **Session-Only Storage** | Credentials cleared after token generation |
| **HTTPS Enforced** | All production deployments use SSL/TLS |
| **No Logging** | Sensitive data never written to logs |
| **Client-Side Processing** | Credentials stored in sessionStorage (temporary) |
| **Direct API Calls** | Browser communicates directly with Spotify |
| **No Server-Side Storage** | Server only facilitates OAuth flow |
| **Automatic Cleanup** | SessionStorage cleared after token retrieval |

### 🔐 Best Practices for Users

1. **Never share your Client Secret** - Treat it like a password
2. **Use HTTPS URLs** - Always deploy with SSL certificates
3. **Revoke unused apps** - Delete old apps from Spotify Dashboard
4. **Regenerate tokens** - If compromised, create new credentials
5. **Limit permissions** - Only request necessary OAuth scopes

### 🛡️ For Developers

```python
# Credentials are never stored
# They're processed in memory and discarded immediately
@app.route('/exchange', methods=['POST'])
def exchange_token():
    data = request.get_json()
    # Process credentials
    # Return token
    # Data is garbage collected
```

---

## 🔌 API Endpoints

### `GET /`
**Description:** Home page with OAuth flow interface  
**Response:** HTML page

### `POST /start`
**Description:** Initiates OAuth flow  
**Request Body:**
```json
{
  "client_id": "your_spotify_client_id"
}
```
**Response:**
```json
{
  "auth_url": "https://accounts.spotify.com/authorize?..."
}
```

### `GET /callback`
**Description:** OAuth callback handler  
**Query Parameters:**
- `code` - Authorization code from Spotify
- `error` - Error message (if authorization failed)  
**Response:** HTML page with authorization code

### `POST /exchange`
**Description:** Exchanges authorization code for refresh token  
**Request Body:**
```json
{
  "client_id": "your_client_id",
  "client_secret": "your_client_secret",
  "code": "authorization_code"
}
```
**Response:**
```json
{
  "success": true,
  "refresh_token": "your_refresh_token",
  "access_token": "your_access_token",
  "expires_in": 3600
}
```

### `GET /health`
**Description:** Health check endpoint  
**Response:** `OK` (200 status)

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### ❌ "Invalid redirect URI" Error

**Problem:** Spotify doesn't recognize your callback URL

**Solution:**
1. Go to [Spotify Dashboard](https://developer.spotify.com/dashboard)
2. Select your app
3. Click "Edit Settings"
4. Add your exact callback URL: `https://your-app.com/callback`
5. Make sure there are no typos or extra slashes
6. Save changes

#### ❌ "Invalid client" Error

**Problem:** Wrong Client ID or Client Secret

**Solution:**
1. Double-check credentials from Spotify Dashboard
2. Ensure no extra spaces when copying
3. Regenerate Client Secret if needed
4. Try creating a new Spotify app

#### ❌ App Not Loading After Deployment

**Problem:** Deployment failed or misconfigured

**Solution:**
1. Check platform logs (Render/Railway/Heroku dashboard)
2. Verify `requirements.txt` has all dependencies
3. Ensure `Procfile` or start command is correct
4. Check Python version in `runtime.txt`

#### ❌ "Authorization code expired" Error

**Problem:** Took too long to exchange code for token

**Solution:**
1. Authorization codes expire after 10 minutes
2. Complete the flow faster
3. Start over if code expired

#### ❌ CORS Errors in Browser

**Problem:** Cross-origin request blocked

**Solution:**
1. Ensure you're accessing via the correct domain
2. Check that HTTPS is enabled in production
3. Verify redirect URI matches exactly

---

## 🎨 Customization

### Changing the UI Theme

Edit `templates/index.html` and `templates/callback.html`:

```html
<!-- Change primary color from Spotify green -->
<style>
    body {
        background: linear-gradient(135deg, #1DB954 0%, #191414 100%);
        /* Change to your brand colors */
    }
</style>
```

### Adding More OAuth Scopes

Edit `app.py`:

```python
scopes = "user-read-currently-playing user-read-recently-played user-top-read playlist-read-private"
```

[View all Spotify scopes](https://developer.spotify.com/documentation/web-api/concepts/scopes)

### Custom Domain

1. Deploy to your platform
2. Add custom domain in platform settings
3. Update DNS records
4. Update Spotify redirect URI with new domain

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Bugs

1. Check existing [Issues](https://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator/issues)
2. Create new issue with:
   - Clear title
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable

### Suggesting Features

1. Open an issue with `[Feature Request]` prefix
2. Describe the feature and use case
3. Explain why it would be useful

### Submitting Pull Requests

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Test locally: `python app.py`
5. Commit: `git commit -m 'Add amazing feature'`
6. Push: `git push origin feature/amazing-feature`
7. Open Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🌟 Show Some Love!

If this tool helped you (and saved you hours of frustration!), consider:

- ⭐ **Star this repo** - It makes us happy and helps others find it!
- 🍴 **Fork it** - Make your own version with your colors and style!
- � **Share it** - Tweet about it, post it on Reddit, tell your friends!
- � **Give feedback** - Open an issue with ideas or just to say thanks!

```
Hey devs! � Need Spotify tokens?
Check out this super easy generator:
👉 https://github.com/SahooShuvranshu/Spotify-Refresh-Token-Generator
No terminal commands needed! 🎉
```

---

## � Need Help? Join Our Community!

<div align="center">

### 🎮 Discord Support Server

[![Discord](https://img.shields.io/badge/Discord-Join%20Server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/your-invite-link)

**Get help from the community!**

- 💡 Ask questions and get instant answers
- 🤝 Share your projects built with this tool
- 🐛 Report bugs and get support
- 🎉 Connect with other developers
- 📢 Get updates on new features

**[Click here to join our Discord server!](https://discord.gg/your-invite-link)**

</div>

---

## �📊 Project Stats

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)
![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=flat-square)

---

<div align="center">

### 🎵 Made with ❤️ and Way Too Much Coffee ☕

**By developers, for developers!**

**[⬆ Back to Top](#-spotify-token-generator---super-easy-edition)**

---

### 🔗 Part of the Spotify Projects Ecosystem

🎨 **[Spotify Live Banner](https://github.com/SahooShuvranshu/Spotify-Live-Banner)** - Show your now playing on your website!

📊 **[Spotify Stats Dashboard](#)** - Coming soon!

🤖 **[Spotify Discord Bot](#)** - Coming soon!

---

### 💭 Final Thoughts

Remember: The hardest part isn't getting the tokens - it's deciding what cool project to build with them! 

Now go forth and make something awesome! 🚀

**Need help?** Open an issue - we're friendly, we promise! 😊

**Made something cool?** Share it with us! We love seeing what you build!

---

### 🎉 You're Awesome for Making It This Far!

Seriously, who reads entire README files anymore? You're a legend! 🏆

Now stop reading and start building! 💪

</div>

```

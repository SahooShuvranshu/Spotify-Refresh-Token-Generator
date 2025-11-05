from flask import Flask, render_template, request, jsonify, redirect
import requests
from base64 import b64encode
from urllib.parse import quote
import os

app = Flask(__name__)

# Spotify OAuth endpoints
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
REDIRECT_URI = os.environ.get("REDIRECT_URI", "http://localhost:5000/callback")

@app.route('/')
def index():
    """Home page with instructions"""
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_auth():
    """Start the OAuth flow"""
    data = request.get_json()
    client_id = data.get('client_id')
    
    if not client_id:
        return jsonify({'error': 'Client ID is required'}), 400
    
    # Store client_id in session (for demo, using URL params - in production use sessions)
    scopes = "user-read-currently-playing user-read-recently-played"
    
    auth_url = (
        f"{SPOTIFY_AUTH_URL}"
        f"?client_id={client_id}"
        f"&response_type=code"
        f"&redirect_uri={quote(REDIRECT_URI)}"
        f"&scope={quote(scopes)}"
    )
    
    return jsonify({'auth_url': auth_url})

@app.route('/callback')
def callback():
    """OAuth callback handler"""
    code = request.args.get('code')
    error = request.args.get('error')
    
    if error:
        return render_template('result.html', error=f"Authorization failed: {error}")
    
    if not code:
        return render_template('result.html', error="No authorization code received")
    
    # Show the code and instructions for manual token exchange
    return render_template('callback.html', code=code, redirect_uri=REDIRECT_URI)

@app.route('/exchange', methods=['POST'])
def exchange_token():
    """Exchange authorization code for tokens"""
    data = request.get_json()
    client_id = data.get('client_id')
    client_secret = data.get('client_secret')
    code = data.get('code')
    
    if not all([client_id, client_secret, code]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Encode credentials
    credentials = f"{client_id}:{client_secret}"
    credentials_b64 = b64encode(credentials.encode()).decode()
    
    # Request tokens
    headers = {
        "Authorization": f"Basic {credentials_b64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI
    }
    
    try:
        response = requests.post(SPOTIFY_TOKEN_URL, headers=headers, data=payload)
        response.raise_for_status()
        token_data = response.json()
        
        return jsonify({
            'success': True,
            'refresh_token': token_data.get('refresh_token'),
            'access_token': token_data.get('access_token'),
            'expires_in': token_data.get('expires_in')
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'details': response.text if 'response' in locals() else 'No response'
        }), 400

@app.route('/health')
def health():
    """Health check endpoint"""
    return 'OK', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

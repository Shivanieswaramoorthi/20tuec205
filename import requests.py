import requests


client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
authorization_url = "https://example.com/oauth2/authorize"
token_url = "https://example.com/oauth2/token"
redirect_uri = "https://your-redirect-url.com/callback"  
authorization_params = {
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "response_type": "code",
    "scope": "desired_scope"  
}
authorization_response = requests.get(authorization_url, params=authorization_params)
authorization_code = "RECEIVED_AUTHORIZATION_CODE" 
token_params = {
    "client_id": client_id,
    "client_secret": client_secret,
    "code": authorization_code,
    "redirect_uri": redirect_uri,
    "grant_type": "authorization_code"
}

token_response = requests.post(token_url, data=token_params)
access_token = token_response.json().get("access_token")

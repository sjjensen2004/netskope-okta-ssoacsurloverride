# The detailed documentation for this script are internal to Netskope

## Basic

Modify the environmental variables in `.env/acsurl.env` to reflect your environment:

- TOKEN="your-token-from-okta-here"
- ENDPOINT="your-okta-url-here"
- NETSKOPE_ACS_URL="your-netskope-SAML-PROXY-ACS-URL-here"
- OKTA_APP="your-okta-app-id-here"

Run `docker-compose up`

Check `/logs/request.log` for results and/or any errors

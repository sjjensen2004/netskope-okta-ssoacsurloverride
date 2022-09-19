from _config import *
import requests
import logging
import json

# Setup the logger
logging.basicConfig(format='%(asctime)s - %(message)s', filename='request.log', level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger().addHandler(console)
logger = logging.getLogger()

URL = f"{ENDPOINT}/api/v1/apps/{OKTA_APP}"

HEADERS = {
    "Authorization": f"SSWS {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}


def okta_get_payload():
    """Grabs teh current Okta app configuraiton and returns the json payload """
    response = requests.get(url=URL, headers=HEADERS)
    if response.status_code != 200:
        logger.error(f"Failed: Check the URL and/or TOKEN in _config.py\n\n{response.content}")
        exit()
    else:
        return response.json()


def okta_ssoacsurloverride(data):
    """Updates the Okta app configuration with the data payload"""
    okta_replace = requests.put(
        url=URL, headers=HEADERS, data=json.dumps(data))
    if okta_replace.status_code != 200:
        logger.error(f"The ssoacsurl could not be updated in Okta.\n\n{okta_replace.content}")
        exit()


def okta_validate():
    """Validates that the Okta app configuration was successfully updated by 
    comparing the existing app parameters with the expected updated parameters"""
    data = okta_get_payload()
    logger.debug(f"Updated Okta Payload:\n{data}")
    return(data[
        'settings']["signOn"]['ssoAcsUrlOverride'] == NETSKOPE_ACS_URL)


if __name__ == "__main__":
    logger.info("Getting Okta configuration")
    data = okta_get_payload()
    logger.debug(f"Original Okta payload: \n{data}")
    data['settings']["signOn"]['ssoAcsUrlOverride'] = NETSKOPE_ACS_URL
    logger.info("Updating Okta ssoAcsUrlOverride with NETSKPE_ACS_URL")
    okta_ssoacsurloverride(data)
    # Validate a successful update
    if okta_validate() is True:
        logger.info("Okta successfully updated.")
    else:
        logger.error("Error: Okta was not updated. Check your URL and Token.")

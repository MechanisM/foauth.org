import foauth.providers
from foauth import OAuthDenied


class LinkedIn(foauth.providers.OAuth1):
    # General info about the provider
    provider_url = 'http://www.linkedin.com/'
    favicon_url = 'https://developer.linkedin.com/sites/all/themes/dlc/favicon.ico'
    docs_url = 'https://developer.linkedin.com/documents/linkedin-api-resource-map'

    # URLs to interact with the API
    request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
    authorize_url = 'https://www.linkedin.com/uas/oauth/authorize'
    access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
    api_domain = 'api.linkedin.com'

    available_permissions = [
        (None, 'read and write to your employment information'),
    ]

    def callback(self, data):
        if data.get('oauth_problem', '') == 'user_refused':
            raise OAuthDenied('Denied access to LinkedIn')

        return super(LinkedIn, self).callback(data)

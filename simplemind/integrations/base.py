# import logging


class BaseClientProvider:

    def __init__(self, *, api_key=None):
        # self.logger = logging.getLogger(self.__class__.__name__)
        self.client = None

        # Load API key from environment if not provided
        self._api_key = api_key

    def login(self):
        """Initializes the AI provider client."""

        msg = "This method must be implemented by the AI provider client."
        raise NotImplementedError(msg)

    def test_connection(self):
        """Tests the connection to the AI provider client."""

        msg = "This method must be implemented by the AI provider client."
        raise NotImplementedError(msg)

    def generate_response(self, request):
        """Generates a response from the AI provider client."""

        msg = "This method must be implemented by the AI provider client."
        raise NotImplementedError(msg)

    def health_check(self):
        """Checks the health of the AI provider client."""

        msg = "This method must be implemented by the AI provider client."
        raise NotImplementedError(msg)

    def available_models(self):
        """Returns the available models from the AI provider client."""

        msg = "This method must be implemented by the AI provider client."

        raise NotImplementedError(msg)

    def features(self):
        """Returns the features of the AI provider client."""

        msg = "This method must be implemented by the AI provider client."
        raise NotImplementedError(msg)

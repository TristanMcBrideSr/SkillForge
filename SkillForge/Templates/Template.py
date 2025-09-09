
import threading
import inspect
import logging
import os
from HoloAI import HoloLink, HoloViro

logger = logging.getLogger(__name__)


class Research:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Research, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super().__init__()
        if hasattr(self, 'initialized'):
            return
        self._initComponents()
        self.initialized = True

    def _initComponents(self):
        self.holoLink = HoloLink()
        self.holoViro = HoloViro()
        self.installList = [
            "python-dotenv", "openai", "google-genai"
        ]
        self.holoViro.pipInstall(self.installList) # Installs to a dedicated venv if not already present

        # External: dotenv
        dotenv = self.holoViro.importFromVenv("dotenv")
        dotenv.load_dotenv()

        # Stdlib env read
        self.provider = os.getenv("PROVIDER", "openai")

        # External: OpenAI client
        openai = self.holoViro.importFromVenv("openai")
        self.gptClient = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # External: Google GenAI + types
        genai = self.holoViro.importFromVenv("google.genai")
        types = self.holoViro.importFromVenv("google.genai.types")
        self.genClient = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.genTypes = types

        self.actionMap = {
            "research": self._research
        }

    def _metaData(self):
        return {
            "className": f"{self.__class__.__name__}",
            "description": "Provides research capabilities using web search via OpenAI or Google GenAI."
        }

    def researchSkill(self, action: str, *args):
        self.holoLink.calledActions(self, locals())
        name = inspect.currentframe().f_code.co_name
        return self.holoLink.executeSkill('system', name, self.actionMap, action, *args)

    def _research(self, instructions: str):
        """
        Description: Research a topic using web search capabilities.
        """
        if self.provider == "openai":
            return self._research_openai(instructions)
        elif self.provider == "google":
            return self._research_google(instructions)
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

    def _research_openai(self, instructions: str):
        return self.gptClient.responses.create(
            model="gpt-4.1-mini",
            tools=[{"type": "web_search_preview"}],
            input=instructions
        ).output_text

    def _research_google(self, instructions: str):
        types = self.genTypes
        return self.genClient.models.generate_content(
            model="gemini-2.0-flash",
            contents=[types.Content(role="user", parts=[types.Part.from_text(text=instructions)])],
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                response_mime_type="text/plain"
            )
        ).text

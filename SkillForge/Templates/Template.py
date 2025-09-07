
from HoloAI import HoloLink, HoloViro

##------------- Skip This Section If You Are Not Using Any External Packages -------------##

# Only list packages that are not part of the standard library
REQUIRES = [
    ("dotenv",       "python-dotenv"), # "python-dotenv==1.0.1" if using a specific version
    ("openai",       "openai>=1.40.0"), # "openai>=1.40.0" if using a specific version or higher
    ("google.genai", "google-genai>=0.3.0"), # "google-genai>=0.3.0" if using a specific version or higher
]

HoloViro.ensurePackages(REQUIRES, quiet=True) # Ensure required packages are installed so imports work

##------------- End of External Packages Section -------------##

import inspect
import logging
import os
import threading
from dotenv import load_dotenv
from openai import OpenAI
from google import genai
from google.genai import types


logger = logging.getLogger(__name__)
load_dotenv()

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
        if hasattr(self, 'initialized'):
            return
        self._initComponents()
        self.initialized = True

    def _initComponents(self):
        self.holoLink  = HoloLink()
        self.provider  = os.getenv("PROVIDER", "openai")
        self.gptClient = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.genClient = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        self.actionMap = {
            "research": self._research
        }

    def researchSkill(self, action: str, *args):
        self.holoLink.calledActions(self, locals())
        name = inspect.currentframe().f_code.co_name
        return self.holoLink.executeSkill('system', name, self.actionMap, action, *args)

    def _research(self, instructions: str):
        """
        Description: "Research a topic using web search capabilities."
        Additional Information: "Uses web search capabilities to gather information on a given topic based on the provided instructions."
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
        return self.genClient.models.generate_content(
            model="gemini-2.0-flash",
            contents=[types.Content(role="user", parts=[types.Part.from_text(text=instructions)])],
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                response_mime_type="text/plain"
            )
        ).text

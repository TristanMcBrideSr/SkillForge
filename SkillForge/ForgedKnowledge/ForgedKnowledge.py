
import os
from dotenv import load_dotenv

load_dotenv()

# ---------- BASE CLASS ----------
class Base:
    def __init__(self):
        pass

    def getUserName(self, user):
        users = {
            "current":  "Tristan",
            "previous": "Sybil"
        }
        return users.get(user, os.getenv("DEFAULT_USER_NAME", "User"))

    def _collectData(self, prefix):
        return [
            item
            for attr in dir(self)
            if attr.startswith(prefix)
            for item in getattr(self, attr)()
        ]

    def thinkingData(self):
        return self._collectData("_thinking")

    def clarifyingData(self):
        return self._collectData("_clarifying")

    def gatheringData(self):
        return self._collectData("_gathering")

    def definingData(self):
        return self._collectData("_defining")

    def refiningData(self):
        return self._collectData("_refining")

    def reflectingData(self):
        return self._collectData("_reflecting")

    def decisionData(self):
        return self._collectData("_decision")

# ---------- COMPONENTS ----------

class Interaction(Base):
    def _thinking(self):
        return [
            # Research
            f"user:\nResearch the benefits of electric vehicles.\n\nassistant:\n{self.getUserName('current')} asked me to research the benefits of electric vehicles. I can use my web search capabilities to gather the latest information and summarize the key advantages.",
            f"user:\nFind recent news about AI breakthroughs.\n\nassistant:\n{self.getUserName('current')} requested the latest news on AI breakthroughs. I can perform a web search to collect and present recent articles and discoveries.",
            f"user:\nLook up statistics on global internet usage.\n\nassistant:\n{self.getUserName('current')} wants me to look up statistics about global internet usage. I can search for reliable sources and provide up-to-date figures.",
            f"user:\nSummarize current trends in renewable energy.\n\nassistant:\n{self.getUserName('current')} asked me to summarize current trends in renewable energy. I will research and compile an overview of the latest industry developments.",

        ]

    def _clarifying(self):
        return [
            # Research
            "user:\nResearch the benefits of electric vehicles.\n\nassistant:\n['researchSkill(\"research\", \"benefits of electric vehicles\")']",
            "user:\nFind recent news about AI breakthroughs.\n\nassistant:\n['researchSkill(\"research\", \"recent news about AI breakthroughs\")']",
            "user:\nLook up statistics on global internet usage.\n\nassistant:\n['researchSkill(\"research\", \"statistics on global internet usage\")']",
            "user:\nSummarize current trends in renewable energy.\n\nassistant:\n['researchSkill(\"research\", \"current trends in renewable energy\")']",

        ]


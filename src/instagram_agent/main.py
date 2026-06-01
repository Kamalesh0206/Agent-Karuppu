import sys
import warnings
import traceback
import logging

from datetime import datetime
from instagram_agent.crew import InstagramAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

logging.basicConfig(level=logging.INFO)

def run():
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        logging.info("Starting InstagramAgent...")
        result = InstagramAgent().crew().kickoff(inputs=inputs)
        logging.info(f"Result: {result}")

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        logging.error(traceback.format_exc())
        raise

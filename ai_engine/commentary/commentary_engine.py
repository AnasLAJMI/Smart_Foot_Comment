
from ai_engine.commentary.prompt_manager import build_commentary_prompt
from ai_engine.commentary.llm_client import generate_commentary


def generate_match_commentary(event, language="ar"):

    # Build the prompt
    prompt = build_commentary_prompt(event, language)

    # Generate AI commentary
    commentary = generate_commentary(prompt)

    return commentary

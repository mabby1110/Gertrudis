import anthropic

class Claude():
    def __init__(self) -> None:
        self.client = anthropic.Anthropic(
            api_key="",
            # defaults to os.environ.get("ANTHROPIC_API_KEY")
        )

    def message(self, user_input):
        message = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            temperature=0.0,
            system="Please convert the following instructions into structured pseudocode, so that it can be easily adapted to programming languages like Python or JavaScript. The pseudocode should be clear, concise, and follow best practices for structured programming",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        return message
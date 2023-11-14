import json
from datetime import datetime

# Define the necessary mock classes
class ChatCompletionMessage:
    def __init__(self, content):
        self.content = content

class Choice:
    def __init__(self, message):
        self.message = message

class MockResponse:
    def __init__(self, choices):
        self.choices = choices

# Mock response function
def get_openai_mock_response_dream(question):
    # Simulate a response from OpenAI's API with a mock JSON content
    mock_json_content = json.dumps({
        "Freudian_Interpretation": "Your dream seems to denote a desire for something deep and profound, represented by the grand oak tree and the starry night. The ethereal deer and the melody leading to lost memories could signify forgotten or repressed desires from your past, finally resurfacing. \'Standing at the forest\'s edge\' might embody your hesitation or fear about facing these needs or wishes.","Jungian_Interpretation": "The grand oak tree in your dream is a potent symbol of life, wisdom and strength, while the ethereal deer could represent gentleness and spirituality. The melody tugging at lost memories may symbolize your inner self trying to communicate crucial aspects of your personality or life experiences. Your ascension towards the starry sky can be seen as a spiritual journey, expressing your unconscious craving for transcendence and understanding.",
        "Cognitive_Behavioral_Interpretation": "From a cognitive behavioral perspective, your dream may reflect your current emotional state or beliefs about your life. The forest at dusk could signify feelings of ambiguity and the anticipation of something to occur. The dream could also illustrate your adjusting, reportedly marked by \'world tilting\', to new experiences which are symbolized by the journey from twilight to velvet night. Recognize your dream as a neutral event and examine any emotional response it evokes."
    })

    # Create a mock response object
    message = ChatCompletionMessage(content=mock_json_content)
    choice = Choice(message=message)
    mock_response = MockResponse(choices=[choice])
    return mock_response

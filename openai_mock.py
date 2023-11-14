# The response from OpenAI will be formatted as a mock response object in Python.
# Please note that this is a representation of a Python object, not a JSON object.

from datetime import datetime

# Define the mock response object
class ChatCompletionMessage:
    def __init__(self, content, role, function_call, tool_calls):
        self.content = content
        self.role = role
        self.function_call = function_call
        self.tool_calls = tool_calls

class Choice:
    def __init__(self, finish_reason, index, message):
        self.finish_reason = finish_reason
        self.index = index
        self.message = message

class CompletionUsage:
    def __init__(self, completion_tokens, prompt_tokens, total_tokens):
        self.completion_tokens = completion_tokens
        self.prompt_tokens = prompt_tokens
        self.total_tokens = total_tokens

class ChatCompletion:
    def __init__(self, id, choices, model, object, system_fingerprint, usage):
        self.id = id
        self.choices = choices
        # self.created = created
        self.model = model
        self.object = object
        self.system_fingerprint = system_fingerprint
        self.usage = usage

# Create the mock response object with the provided data
mock_response = ChatCompletion(
    id='chatcmpl-8J4aew0FwQsplZ1YRJUu9uhgLJBAs',
    choices=[
        Choice(
            finish_reason='stop',
            index=0,
            message=ChatCompletionMessage(
                content='{\n "Numerical_Score": 90,\n "Categories": {\n "Thesis": {\n "Max_Score": 15,\n "Score": 13,\n \
"Comments": "Well-defined thesis, but could provide more specific points to be argued or discussed."\n },\n "Organization": {\n "Max_Score": 25,\n "Score": 23,\n "Comments": "Logical order is well maintained. Transitions could be \
smoother."\n },\n "Evidence": {\n "Max_Score": 20,\n \
"Score": 18,\n "Comments": "Good use of example and argument. More concrete data or statistics could be used."\n },\n "Analysis": {\n "Max_Score": 20,\n "Score": 17,\n "Comments": "Sound analysis overall, however, some arguments need further development."\n },\n "Style": {\n "Max_Score": 10,\n "Score": 10,\n "Comments": "Excellent style. Good use of language that\'s clear, concise, and engaging."\n },\n "Convention": {\n "Max_Score": 10,\n \
"Score": 9,\n "Comments": "Minimal spelling and grammar mistakes."\n }\n },\n "Overall_Feedback": "The essay presents \
a clear and coherent argument on the role and impact of technology, backed by relevant examples. To improve, provide more specific points in your thesis and include more concrete data or statistics in your evidence. Keep working on enriching your analysis \
and transition between points."\n}',
                role='assistant',
                function_call=None,
                tool_calls=None
            )
        )
    ],
    model='gpt-4-0613',
    object='chat.completion',
    system_fingerprint=None,
    usage=CompletionUsage(
        completion_tokens=328,
        prompt_tokens=654,
        total_tokens=982
    )
)

from flask import Flask, render_template, request
from dotenv import load_dotenv
import json
import openai
import asyncio
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

def get_openai_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {
                "role": "user",
                "content":f"""
                    Grade the following essay and provide feedback in JSON format with the following structure:
                    - Numerical score out of 100. The key should be "Numerical_Score" and the value should be an integer. The essay must be a minimum of 400 words to be eligible for a score above 70. If the essay is under 200 words, reduce the score significantly.
                    - Comments object with comments on thesis, organization, evidence, analysis, style, and convention. Keys should be capitalized and values should be strings. Each comment should be no more than two sentences.
                    - Provide overall feedback that summarizes the essay's strengths and areas for improvement in no more than three sentences. The key should be "Overall_Feedback" and the value should be a string.

                    The length of the essay is a critical factor in the grading. Essays that do not meet the minimum word count of 400 words should receive a lower score, as this indicates an incomplete development of ideas. Deduct points accordingly for essays falling short of this requirement, with substantial deductions for essays under 200 words, reflecting an insufficiently developed argument.

                    Here is the essay: {prompt}

                    Provide only the JSON data and no other comments outside the JSON data.
                """
            }
        ]
    )
    return response

def get_mock_openai_response(prompt):
    """
    Returns a mock OpenAI API response for development purposes.
    """
    return {
        "choices": [
            {
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": "{\n    \"Numerical_Score\": 75,\n    \"Comments\": {\n        \"Thesis\": \"The thesis statement is clear and demonstrates a deep understanding of the topic, but can use more refinement to make it precise.\",\n        \"Organization\": \"The essay structure is organized, making it easy for readers to comprehend. However, some ideas abruptly transit, which may confuse the readers.\",\n        \"Evidence\": \"The author provides adequate evidence to support the argument. But, there is room for incorporating diverse sources to enhance credibility.\",\n        \"Analysis\": \"The analysis of each concept reflects the author's understanding, but the conclusions can be more comprehensive and relate back to the thesis statement more effectively.\",\n        \"Style\": \"The language usage and stylistic devices add value to the essay, but need to be more consistent to keep the readers engaged.\",\n        \"Convention\": \"There are minor grammatical and punctuation errors noticed, proofreading can certainly help improve the quality.\"\n    },\n    \"Overall_Feedback\": \"Overall, the essay demonstrates a good understanding of the topic and presents its argument effectively. Improvement can be made in refining the thesis statement and incorporating various sources of evidence. A careful proofread will also help in rectifying minor mistakes and ensure consistency.\"\n}"
                }
            }
        ],
        "created": 1677664795,
        "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
        "model": "gpt-3.5-turbo-0613",
        "object": "chat.completion",
        "usage": {
            "completion_tokens": 17,
            "prompt_tokens": 57,
            "total_tokens": 74
        }
    }
    

@app.route('/', methods=['GET', 'POST'])
def index():
    parsed_response = None
    user_question = None
    if request.method == 'POST':
        user_question = request.form['user_question']
        # Use the mock response in development instead of making an actual API call
        response = get_openai_response(user_question)
        # print(response)
        inner_json_string = response.choices[0].message.content
        inner_json_string = inner_json_string.strip()
        parsed_response = json.loads(inner_json_string) if inner_json_string else None
    return render_template('index.html', response=parsed_response, prompt=user_question)

if __name__ == '__main__':
    app.run(debug=True)
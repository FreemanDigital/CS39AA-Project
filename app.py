from flask import Flask, render_template, request, url_for, redirect
from dotenv import load_dotenv
import json
import openai
from openai_mock_dream import get_openai_mock_response_dream
import asyncio
import os
import datetime

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

def get_openai_response_mark(prompt):
    response = openai.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {
                "role": "system",
                "content": "You are an English teacher. A student has submitted the following essay for grading."
            },
            {
                "role": "user",
                "content":f"""
                    Grade the following essay and provide feedback in JSON format with the following structure:
                    - Numerical score out of 100. The numerical score should be a total of the category scores. The key should be "Numerical_Score" and the value should be an integer. The essay must be a minimum of 400 words to be eligible for a score above 70. If the essay is under 200 words, reduce the score significantly.
                    - Categories object with Max_Score, Score, and Comments on Thesis, Organization, Evidence, Analysis, Style, and Convention. Keys should be capitalized. Each comment should be no more than two sentences. The max score for each category is: 15 for Thesis, 25 for Organization, 20 for Evidence, 20 for Analysis, 10 for Style, and 10 for Convention. 
                    - Provide overall feedback that summarizes the essay's strengths and areas for improvement in no more than three sentences. The key should be "Overall_Feedback" and the value should be a string.

                    The length of the essay is a critical factor in the grading. Essays that do not meet the minimum word count of 400 words should receive a lower score, as this indicates an incomplete development of ideas. Deduct points accordingly for essays falling short of this requirement, with substantial deductions for essays under 200 words, reflecting an insufficiently developed argument.

                    Here is the essay: {prompt}

                    Provide only the JSON data and no other comments outside the JSON data.
                """
            }
        ]
    )
    return response

def get_openai_response_dream(prompt):
    response = openai.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {
                "role": "system",
                "content": "You are an expert psychologist specializing in dream interpretation. A patient has submitted the following dream for analysis."
            },
            {
                "role": "user",
                "content":f"""
                    Interpret the following dream and provide feedback in JSON format with the following structure:
                    - Freudian_Interpretation: Provide a Freudian interpretation of the dream in no more than three sentences. The key should be "Freudian_Interpretation" and the value should be a string.
                    - Jungian_Interpretation: Provide a Jungian interpretation of the dream in no more than three sentences. The key should be "Jungian_Interpretation" and the value should be a string.
                    - Cognitive_Behavioral_Interpretation: Provide a Cognitive Behavioral interpretation of the dream in no more than three sentences. The key should be "Cognitive_Behavioral_Interpretation" and the value should be a string.
                    
                    In all of the above interpretations, provide a brief explanation of the dream's meaning and how it could relate to the patient's life. Speak in the second person, as if you are speaking directly to the patient.

                    Here is the dream: {prompt}

                    Provide only the JSON data and no other comments outside the JSON data.
                """
            }
        ]
    )
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mark', methods=['GET', 'POST'])
def mark():
    parsed_response = None
    user_question = None
    if request.method == 'POST':
        user_question = request.form['user_question']
        # Use the mock response in development instead of making an actual API call
        # response = get_mock_openai_response_mark(user_question)
        response = get_openai_response_mark(user_question)
        print(response)
        inner_json_string = response.choices[0].message.content if response.choices else None
        inner_json_string = inner_json_string.strip()
        parsed_response = json.loads(inner_json_string) if inner_json_string else None
    return render_template('mark.html', response=parsed_response, prompt=user_question)

@app.route('/dream', methods=['GET', 'POST'])
def dream():
    parsed_response = None
    user_question = None
    if request.method == 'POST':
        user_question = request.form['user_question']
        # Use the mock response in development instead of making an actual API call
        response = get_openai_response_dream(user_question)
        # response = get_openai_mock_response_dream(user_question)
        print(response)
        inner_json_string = response.choices[0].message.content if response.choices else None
        inner_json_string = inner_json_string.strip()
        parsed_response = json.loads(inner_json_string) if inner_json_string else None
    return render_template('dream.html', response=parsed_response, prompt=user_question)

if __name__ == '__main__':
    app.run(debug=True)
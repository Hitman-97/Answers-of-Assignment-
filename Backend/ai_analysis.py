import openai
import json


openai.api_key = "write the api key"

def analyze_data(data):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Or use GPT-4 if available
        prompt=f"Summarize the following content and analyze its sentiment and category:\n{data}",
        max_tokens=500
    )
    return response.choices[0].text.strip()

def process_data():
    with open('../extracted_data.json', 'r') as f:
        lines = f.readlines()
    
    analyzed_data = []
    for line in lines:
        page = json.loads(line)
        content = page.get('article_content', '')
        analysis_result = analyze_data(content)
        page['ai_analysis'] = analysis_result
        analyzed_data.append(page)
    
    # Save analyzed data
    with open('../analyzed_data.json', 'w') as f:
        json.dump(analyzed_data, f, indent=4)

if __name__ == "__main__":
    process_data()

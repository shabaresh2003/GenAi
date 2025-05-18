import re
from groq import Groq

# Directly assign the API key (not recommended for production or version control)
groq = Groq(api_key="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")

def classify_with_llm(log_msg):
    """
    Classify log message into:
    (1) Workflow Error, (2) Deprecation Warning, or "Unclassified".
    Category is returned from within <category> tags.
    """
    prompt = f'''Classify the log message into one of these categories: 
    (1) Workflow Error, (2) Deprecation Warning.
    If you can't figure out a category, use "Unclassified".
    Put the category inside <category> </category> tags. 
    Log message: {log_msg}'''

    chat_completion = groq.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="deepseek-r1-distill-llama-70b",  # You can switch to llama3 here
        temperature=0.5
    )

    content = chat_completion.choices[0].message.content
    match = re.search(r'<category>(.*?)</category>', content, flags=re.DOTALL)
    category = "Unclassified"
    if match:
        category = match.group(1).strip()

    return category


if __name__ == "__main__":
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))

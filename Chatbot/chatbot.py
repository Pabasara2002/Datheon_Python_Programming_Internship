import json
import re
import os

def load_faq_dataset(filename="sample_faq.json"):
    """Loads greetings and FAQs from the JSON dataset."""
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Error reading {filename}: {e}")
    
    # Fallback default dataset if file is missing
    return {
        "greetings": ["hello", "hi", "hey", "good morning", "good afternoon"],
        "faqs": [
            {
                "question": "What are your hours of operation?",
                "answer": "We operate Monday through Friday from 9:00 AM to 6:00 PM IST."
            },
            {
                "question": "How do I submit my internship project?",
                "answer": "You can submit your public GitHub repository link through your Student Workspace."
            },
            {
                "question": "When will I receive my certificate?",
                "answer": "Certificates are reviewed and issued within 3-5 business days after your code review."
            }
        ]
    }

def normalize_input(user_input):
    """Normalizes user input by converting to lowercase and stripping whitespace/special chars."""
    return re.sub(r'[^\w\s]', '', user_input.lower()).strip()

def run_chatbot():
    print("==================================================")
    print("   DATHEON RULE-BASED SUPPORT ASSISTANT CHATBOT   ")
    print("==================================================")
    
    dataset = load_faq_dataset()
    greetings = dataset.get("greetings", [])
    faqs = dataset.get("faqs", [])

    print("Bot: Hello! Welcome to Datheon Support. How can I help you today?")
    print("     (Type 'exit', 'quit', or 'bye' to end the conversation)\n")

    while True:
        try:
            raw_input_text = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye! Have a great day!")
            break

        if not raw_input_text:
            continue

        cleaned_input = normalize_input(raw_input_text)

        # 1. Check for clean exit commands
        exit_commands = ["exit", "quit", "bye", "goodbye"]
        if cleaned_input in exit_commands or any(ex in cleaned_input.split() for ex in exit_commands):
            print("Bot: Thank you for reaching out to Datheon Support. Goodbye and good luck with your internship! 👋")
            break

        # 2. Check for greetings using regex/substring matching
        is_greeting = False
        for greet in greetings:
            if re.search(r"\b" + re.escape(greet) + r"\b", cleaned_input) or cleaned_input == greet:
                is_greeting = True
                break

        if is_greeting:
            print("Bot: Hello there! Feel free to ask me about our hours, project submissions, or certificates.\n")
            continue

        # 3. Intent Matching against FAQs using Keyword Overlap / Regex
        best_match_answer = None
        highest_keyword_matches = 0

        for faq in faqs:
            q_text = normalize_input(faq["question"])
            # Extract significant keywords (ignoring short common words)
            keywords = [word for word in q_text.split() if len(word) > 2]
            
            match_count = sum(1 for kw in keywords if re.search(r'\b' + re.escape(kw) + r'\b', cleaned_input))
            
            if match_count > highest_keyword_matches:
                highest_keyword_matches = match_count
                best_match_answer = faq["answer"]

        # 4. Response with fallback handling if confidence/matches are low
        if highest_keyword_matches > 0 and best_match_answer:
            print(f"Bot: {best_match_answer}\n")
        else:
            # Graceful fallback for unrecognized queries
            print("Bot: I'm sorry, I didn't quite catch that. Could you please rephrase your question? You can ask about business hours, project submissions, or certificates.\n")

if __name__ == "__main__":
    run_chatbot()
import ollama
from langdetect import detect

# Role-specific system prompts
ROLE_PROMPTS = {
    "legal": (
        "You are LexiAI Legal Advisor. You specialize in interpreting laws, regulations, and policies. "
        "Always provide precise, well-referenced responses using legal terminology. "
        "If the question is not legal, reply briefly and state that your expertise is in legal matters."
    ),
    "hr": (
        "You are LexiAI HR Assistant. You help with HR policies, hiring, employee relations, and compliance. "
        "Keep responses professional, accurate, and people-focused."
    ),
    "tech": (
        "You are LexiAI Technical Expert. You assist with software, cloud, APIs, system design, and engineering. "
        "Use examples, explain clearly, and be concise but thorough."
    ),
    "general": (
        "You are LexiAI General Assistant. You help with a broad range of everyday questions using clear, helpful, and accurate answers."
    )
}

def ask_question_with_context(question, context_text, model_name="llama3", role="general"):
    try:
        # 🌍 Detect the question's language
        language = detect(question)

        # 🧠 Role-specific instructions
        system_role_prompt = ROLE_PROMPTS.get(role, ROLE_PROMPTS["general"])

        # 📝 Combined prompt
        prompt = f"""
{system_role_prompt}

You are a multilingual, helpful document assistant. Your tasks:
• If the question is about the documents, answer using only the document.
• If the question is not about the document, answer from your general or role knowledge, and say: "Note: This answer is not based on the documents."
• Always reply in the same language as the user.

### Documents:
\"\"\"{context_text}\"\"\"

### Question:
{question}

Answer:
"""
        print(f"⚙️ Loading model: {model_name}")
        print(f"[🧠 PROMPT SENT TO '{model_name}']\n{prompt[:1000]}...\n")
        ollama.pull(model_name)

        response = ollama.chat(
            model=model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        if "message" not in response or "content" not in response["message"]:
            print(f"[❌ ERROR] No message content returned from model '{model_name}'. Raw response:\n{response}")
            return "⚠️ The model did not return a valid response. Try using a different model or check the logs."

        return response['message']['content'].strip()

    except Exception as e:
        return f"Error: {e}"

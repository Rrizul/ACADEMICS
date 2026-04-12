import requests

# =========================
# CONFIG
# =========================
MODEL = "gemma:2b"
OLLAMA_URL = "http://localhost:11434/api/generate"


# =========================
# FUNCTION TO TALK TO MODEL
# =========================
def ask_agent(role, question, context=""):
    prompt = f"""
You are a {role}.

Question:
{question}

Previous Discussion:
{context}

Instructions:
- Stay true to your role.
- Give a clear and useful answer.
- Keep it concise (4 to 6 lines).
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 150,
                    "temperature": 0.7
                }
            },
            timeout=120
        )

        data = response.json()

        if "response" in data:
            return data["response"].strip()
        elif "error" in data:
            return f"ERROR: {data['error']}"
        else:
            return "ERROR: Unexpected response from model."

    except requests.exceptions.ConnectionError:
        return "ERROR: Cannot connect to Ollama. Make sure Ollama is running."

    except requests.exceptions.Timeout:
        return "ERROR: Request timed out."

    except Exception as e:
        return f"ERROR: {str(e)}"


# =========================
# MAIN PROGRAM
# =========================
def main():
    print("====================================")
    print("   MULTI-AGENT AI DECISION SYSTEM   ")
    print("         Model: gemma:2b            ")
    print("====================================")

    question = input("\nEnter your question: ").strip()

    if not question:
        print("Please enter a valid question.")
        return

    print("\nThinking...\n")

    # Agent 1
    logical = ask_agent("Logical Thinker", question)

    # Agent 2
    emotional = ask_agent("Emotional Advisor", question, logical)

    # Agent 3
    critical = ask_agent(
        "Critical Analyst",
        question,
        logical + "\n" + emotional
    )

    # Final Synthesizer
    final_context = f"""
Logical Thinker:
{logical}

Emotional Advisor:
{emotional}

Critical Analyst:
{critical}
"""

    final = ask_agent(
        "Final Decision Maker",
        "Combine all viewpoints and give one balanced final answer.",
        final_context
    )

    # =========================
    # OUTPUT
    # =========================
    print("----------- Logical Thinker -----------")
    print(logical)

    print("\n---------- Emotional Advisor ----------")
    print(emotional)

    print("\n----------- Critical Analyst ----------")
    print(critical)

    print("\n============= FINAL ANSWER =============")
    print(final)


# =========================
# RUN
# =========================
if __name__ == "__main__":
    main()
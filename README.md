Mental Wellness Journal Companion (PS 57)

A GenAI-powered journaling application designed for students. Users can write daily journal entries, receive supportive AI-generated reflections, view an approximate mood label, manage saved entries locally, and see helpline information when distress-related language is detected.

# Features
* Journal entry form with date selection
* Supportive AI-generated responses using Groq API
* Local keyword-based mood estimation
* Distress-language detection with India support resources (**Tele-MANAS: 14416**; **Emergency: 112**)
* Local journal history with delete option
* Safe fallback response if the API key is missing or the API is unavailable

<img width="795" height="747" alt="Screenshot 2026-11-23 234823" src="https://github.com/user-attachments/assets/e101cb3f-287d-43b3-9e79-f5dc290bd3a3" />


# Technology Stack
* **Programming Language:** Python
* **User Interface:** Streamlit
* **LLM Provider:** Groq API
* **Model:** GPT-OSS 20B
* **Libraries:** `groq`, `python-dotenv`, `streamlit`, `pandas`
* **Storage:** Local JSON file (`journal_entries.json`)

# Setup and Installation
1. Install Python 3.10 or newer.
2. Clone this repository or open the project folder in VS Code.
3. Create and activate a virtual environment (recommended).
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Get a Groq API key from the Groq Console.
6. Create a `.env` file in the project folder and add your API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```
7. Run the application:
   ```bash
   streamlit run app.py
   ```
   *(A fallback response is also included when the API key is missing or unavailable so you can test the interface.)*

## Project Structure
* `app.py` – Streamlit user interface
* `ai_helper.py` – Groq API integration and fallback response
* `journal.py` – Mood estimation, distress detection, and local journal storage (`journal_entries.json`)
* `requirements.txt` – Project dependencies
* `.env.example` – Example environment configuration

<img width="1920" height="1140" alt="Screenshot 2026-11-23 235759" src="https://github.com/user-attachments/assets/13197725-41ca-47be-84df-cf2f28efd9ee" />


# Problem Statement
*PS 57 – Mental Wellness Journal Companion*

Students often experience stress but may not take time to reflect on their feelings. The objective is to build a journaling application that responds supportively to journal entries and shares helpline information when distress-related language is detected.

# Safety and Privacy
This project is an educational prototype, not medical advice, a medical device, a diagnostic tool, a therapy service, or a crisis service.

Mood labels and distress flags are approximate keyword-based checks and may miss context. Users should avoid entering highly sensitive personal information. Journal entries are stored locally in `journal_entries.json` on the machine running the application.

The application displays India-specific support contacts (**Tele-MANAS: 14416**; *Emergency: 112*) when selected distress-related terms are detected. In an immediate emergency, contact local emergency services.

<img width="1920" height="1140" alt="Screenshot 2026-11-23 235851" src="https://github.com/user-attachments/assets/1ef4d311-f4b2-4792-b1f0-0cd832fad877" />


# Developer
Name: Harsh Patel 

Roll No.:57

Class:LY CORE 4

<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/9a880d64-082a-4d48-a186-92b1cd8ac241" />

# 📚 Language Questions Generator

Generate language learning questions and answers in PDF format, based on your own CSV resources.

---

## Index

- [How to use](#-how-to-use)
- [Supported Questions](#-supported-question-types)
- [Supported Languages](#-supported-languages)
- [CSV Format](#-csv-format)
- [LLMs Tried](#-llms-tried)

---

## 🚀 How to Use

1. **Requirements:**
   - Python 3.x
   - Place your CSV resource files in the `resources` folder.

2. **Run the program:**
   ```bash
   python jpq.py
   ```

3. **Follow the prompts:**
   - Select the main reading language (preferably a language you are fluent in).
   - Choose the target translation language (preferably the language you are learning).
   - Select the difficulty level (for Japanese: JLPT N5–N1).
   - Choose the types of questions.
   - Enter the number of questions to generate.

4. **Output:**
   - The program will generate two PDF files in the `output` folder:
     - `questions.pdf` (with date)
     - `answers.pdf` (with date)

---

## 📝 Supported Question Types

- Multiple Choice (WIP)
- Fill in the Blank (WIP)
- Fill in the Blank (with options) (WIP)
- Short Answer
- Long Answer (WIP)
- Meaning (WIP)
- Pronunciation (WIP)

---

## 🌐 Supported Languages

**Main Reading Languages:**
- English

**Target Translation Languages:**
- Portuguese (WIP)
- English (WIP)
- Spanish (WIP)
- French (WIP)
- Japanese (with JLPT levels)

---

## 📄 CSV Format

Your CSV file should contain the following columns:

- word
- pronounciation
- translation

---

## 🤖 LLMs Tried

- devstral:24b
- qwen3:8b

You can use your own LLM if you want! This can be achieved by changing the model defined in the `src\questions` folder.
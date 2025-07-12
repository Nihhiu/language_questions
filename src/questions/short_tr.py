import re
import subprocess


def short_tr_QA(idioma_pergunta: str,
                   idioma_resposta: str,
                   palavra: str,
                   dificuldade: str) -> dict:
    """
    Gera uma questão e resposta via LLM local (Ollama).
    Retorna um dict: {'questao': str, 'resposta': str}
    """

    # 1. Monta o prompt
    prompt = (
        f"You are an experienced {idioma_pergunta} teacher, specialized in translation-based teaching.\n"
        f"Create ONE SINGLE SENTENCE in {idioma_resposta} translated into {idioma_pergunta}, "
        f"using the word “{palavra}” mandatorily. The sentence must match the JLPT {dificuldade} level, "
        "meaning it should reflect vocabulary, grammar, and complexity typical of that level.\n"
        "Avoid overly long or advanced sentences.\n"
        "Use the word in a natural context.\n"
        "For example: (\"Today, I will drink water\", \"I like action movies\", \"I saw a movie this weekend with Ann\")\n\n"
        "⚠️ Strictly follow this format (no explanations or notes):\n"
        f"Sentence: <sentence text in {idioma_pergunta}>\n"
        f"Translation: <sentence translation in {idioma_resposta}>\n"
    )


    # 2. Chama o Ollama
    proc = subprocess.run(
        [r"ollama", "run", "qwen3:8b", prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    )
    
    output = proc.stdout.strip()
    stderr = proc.stderr.strip()

    if proc.returncode != 0:
        raise RuntimeError(f"Ollama devolveu código {proc.returncode}:\n{stderr}")

    # Debug: imprime o que realmente veio
    if not output:
        raise ValueError(f"Modelo não devolveu output.\nstderr:\n{stderr}")

    # 3. Extrai 'Frase' e 'Resposta' com regex
    resposta_match = re.search(r"Frase:\s*(.+?)(?=\s*Resposta:)", output, re.DOTALL)
    pergunta_match = re.search(r"Resposta:\s*(.+)", output, re.DOTALL)

    if not pergunta_match or not resposta_match:
        raise ValueError(f"Falha a extrair Q/A:\nOUTPUT:\n{output}\nSTDERR:\n{stderr}")

    return {
        "question": pergunta_match.group(1).strip(),
        "answer": resposta_match.group(1).strip()
    }
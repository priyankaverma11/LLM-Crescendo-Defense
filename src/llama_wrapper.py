import subprocess

def query_llama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3.2:3b", prompt],
        capture_output=True,
        text=True
    )

    return result.stdout.strip()
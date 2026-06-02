import subprocess

def query_llama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3.2:3b", prompt],
        capture_output=True,
        text=True
    )

    print("STDOUT:")
    print(result.stdout)

    print("STDERR:")
    print(result.stderr)

    print("RETURN CODE:")
    print(result.returncode)

    return result.stdout.strip()
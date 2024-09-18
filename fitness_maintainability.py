import subprocess


def run_radon_cc():
    try:
        result = subprocess.run(['radon', 'cc', 'server.py'], capture_output=True, text=True, check=True)

        print("Radon Cyclomatic Complexity Analysis:")
        print(result.stdout)

        if result.stderr:
            print("Error Output:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


run_radon_cc()

import re

with open("file_to_read.txt", "r") as f:
    text = f.read()

count_terrible = len(re.findall(r"\bterrible\b", text))
print(f"The word 'terrible' appears {count_terrible} times.")

new_text = re.sub(r"\bterrible\b", lambda match: "pathetic" if match.start() % 2 == 0 else "marvellous", text)

with open("result.txt", "w") as f:
    f.write(new_text)
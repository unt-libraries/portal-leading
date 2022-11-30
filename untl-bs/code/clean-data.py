import re
import fileinput

for line in fileinput.input():
    line = line.strip()
    
    cleaned = line
    
    cleaned = cleaned.lower()
    cleaned = re.sub(r"[-]|[—]|[_]", " ", cleaned)
    cleaned = re.sub(r"[,]", " ", cleaned)
    cleaned = re.sub(r"[^\w\s]", "", cleaned)
    cleaned = re.sub(r"[0-9]", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    
    print(cleaned)
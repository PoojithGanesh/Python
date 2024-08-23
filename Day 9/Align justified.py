#Take the sentence as input align justified
sentence = input("Enter a sentence: ")
width = int(input("Enter the width: "))

words = sentence.split()
lines = []
line = ""

for word in words:
    if len(line) + len(word) + 1 > width:
        lines.append(line.ljust(width))
        line = word
    else:
        line += " " + word

lines.append(line.ljust(width))

print("\n".join(lines))

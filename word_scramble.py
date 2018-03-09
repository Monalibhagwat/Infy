import random;
try:
    in_text = open("MyFile.txt", "r")
    out_text = open("MyFileScrambled.txt", "w")
except IOError:
    print("File in.txt does not exist creating default one.")
    in_file = open("MyFile.txt", "w")

in_text = open("MyFile.txt", "r")
out_text = open("MyFileScrambled.txt", "w")

def shuffle(word):
    if(len(word)==1):
        return word;
    else:
        half = int(len(word) / 2)
        # First half in reverse
        first = word[:half][::-1]
        # Last half in reverse
        last = word[half:len(word)][::-1]

        # First + Last in reverse
        return str(first+last)[::-1]
     

def scramble(word):
    if(len(word)<=3):
        return word;
    first = word[:1];
    last = word[-1:];
    mid = word[1:-1];
    
    if(last == '.' or last == ','):
        last = word[-2:];
        mid = word[1:-2];
    
    return str(first) + str(shuffle(mid)) + str(last);

for line in in_text:
    line = line.strip()
    new_line = [];

    for word in line.split(" "):
        new_line.append(scramble(word));
        new_line.append(" ");
    out_text.writelines(new_line);
    #print new_line;




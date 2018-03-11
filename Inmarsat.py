input="Thisisanexampleteststring."
words=[]
def isAWord(word):
    if word.lower() in words: # Check lowercase version of word so capitalised words e.g. "This" still match the word list
        return True
    else:
        return False
with open("OxfordEnglishDictionary.txt") as OED: # List of English words separated by a \n (return)
    for line in OED:
        words.append(line[:-1].lower()) # Remove \n from word string and make word lowercase so that proper nouns and capitalised words at the start of sentences will still be picked up in isAWord()
output=""
start=0
end=1 # Word needs to be at least one letter long
while end<len(input): # Iterate over length of test string
    if isAWord(input[start:end]): # Check if string is a word
        output+=input[start:end] # Add matched word to output string, outputs the original word so it will be capitalised if it was capitalised in the input string even though the lowercase version was used for the check
        if input[end]==".": # Python's index numbering is non-inclusive so in this case when input[start:end]=="string", input[end]=="."
            output+="." # If word is immediately followed by a full stop in the input string this is to be preserved for the output string as well rather just than adding a space
            end+=1 # Skip over full stop for next word check (applicable if test string contains multiple sentences)
        output+=" " # Add a space after the latest word (or add a space after the full stop)
        start=end # Set starting point for next word
    end+=1 # Move end point to the right by one character on each iteration. Once a word is found, the search will recommence from the next character
print(output)
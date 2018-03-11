input="Thisisanexampleteststring.Multiplesentencesarehandledperfectly.Theremaybesomeinstanceswherespacesareaddedinthewrongplaceasthereareseveraldifferentvalidcombinationsofwords."
words=[]
def isAWord(word):
    if word.lower() in words: # Check lowercase version of word so capitalised words e.g. "This" still match the word list
        return True
    else:
        return False
with open("OED.txt") as OED: # List of English words separated by a \n (return)
    for line in OED:
        words.append(line[:-1].lower()) # Remove \n from word string and make word lowercase so that proper nouns and capitalised words at the start of sentences will still be picked up in isAWord()
output=""
start=0
end=1 # Word needs to be at least one letter long
candidates=[] # Could have written these as a 2D matrix instead of 3 separate lists but this way makes referring to them a bit easier
starts=[]
ends=[0] # Needs initial 0 for if start in ends check, removed later
while end<=len(input): # Iterate over length of test string not including full stop
    n=0
    while n<=len(max(words,key=len)): # Checks for all possible words in the string up to the length of the longest word in the dictionary
        if isAWord(input[start:end+n]): # Checks for words with given starting point, increasing end point by one on each iteration
            if start in ends: # To make sure words which do not follow from previous possible words, e.g. "sane", are discarded
                starts.append(start)
                if input[end+n]==".":
                    candidates.append(input[start:end+n]+".") # If word is immediately followed by a full stop in the input string this is to be preserved for the output string as well
                    ends.append(end+n+1) # Use end value inclusive of full stop
                    break # Full stops mean the end of the word has been found so there is no point checking for longer words than this
                else:
                    candidates.append(input[start:end+n])
                    ends.append(end+n)
        n+=1
    start=end # Set starting point for next set of possible words
    end+=1 # Move end point to the right by one character on each iteration so that word is at least one character long
ends.pop(0) # Remove placeholder 0 value from start of ends list
discard=[]
while candidates[-1][-1]!=input[-1]: # Discard final word candidate if it does not end in a full stop as it therefore can't be the final word in the sentence
        candidates.pop(-1)
        starts.pop(-1)
        ends.pop(-1)
x=len(candidates)-1
starts.append(ends[-1]) # Add final ends value to starts for following check, removed later
while x>=0:
    if ends[x] not in starts: # Check if there is a possible route from each word to the previous one to avoid dead ends and remove words which don't have a possible predecessor
        candidates.pop(x)
        starts.pop(x)
        ends.pop(x)
    x-=1
starts.pop(-1)
i=0
while i<len(candidates):
    output=output+candidates[i]+" " # Adds words from candidates to output string in order from first to last, only adding words that follow directly from the previous one
    if ends[i] not in starts: # This is the case where the final word in the input string has been reached as other cases have already been accounted for
        break
    i=starts.index(ends[i]) # Set i to the index of the start of the next word which is the same position the end of the previous word
print(output)
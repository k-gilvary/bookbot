# counts amt of words in string
def word_count(words):
    words_list = words.split()
    return len(words_list)

# counts how many times each char appears in text
def count_chars(text):
    chars_obj = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0, 
        "f": 0, 
        "g": 0, 
        "h": 0, 
        "i": 0, 
        "j": 0, 
        "k": 0, 
        "l": 0, 
        "m": 0, 
        "n": 0, 
        "o": 0, 
        "p": 0, 
        "q": 0, 
        "r": 0, 
        "s": 0, 
        "t": 0, 
        "u": 0, 
        "v": 0, 
        "w": 0, 
        "x": 0, 
        "y": 0, 
        "z": 0,
        " ": 0
    }

    for c in list(text.lower()):
        for l in chars_obj:
            if c == l:
                chars_obj[l] += 1
    
    return chars_obj

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

        print("--- Begin report of books/frankenstein.txt ---")

        w_count = word_count(file_contents)
        print(f"{w_count} words found in the document \n")

        c_count = count_chars(file_contents)
        sorted_c = sorted(c_count, key=c_count.get, reverse=True)[1:]
        
        for c in sorted_c:
            print(f"The letter '{c}' was found {c_count[c]} times")
        
        print("--- End report ---")

main()

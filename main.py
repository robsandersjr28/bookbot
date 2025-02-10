def main():
    word_count_result = word_count(file_contents)
    character_count_result = character_count(file_contents)
    sorted_counts = sorting(character_count_result)
    for item in sorted_counts:
        char = item["character"]
        count = item["count"]
        print(f"The '{char}' character was found {count} times")
    

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def word_count(file_contents):
    words = file_contents.split()
    word_counter = 0
    return len(words)

def character_count(file_contents):
    counted = {}
    lowered_string = file_contents.lower()
    for char in lowered_string:
        if char in counted:
            counted[char] += 1
        else:
            counted[char] = 1
    return counted

def sorting(character_count_result):
    listed_dictionary = []
    for char, value in character_count_result.items():
        if char.isalpha() and char.lower() in "abcdefghijklmnopqrstuvwxyz":
            listed_dictionary.append({"character": char, "count": value})
    listed_dictionary.sort(key=lambda item: item["count"], reverse=True)
    return listed_dictionary

main()    

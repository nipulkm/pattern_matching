def pattern_check(text_index):
    cnt = 0
    for index in range(text_index+1, text_index+len_of_pattern):
        cnt = cnt + 1
        if given_text[index] == pattern[cnt]:
            continue
        else:
            return False
    return True


given_text = "tadadattaetadadadafa"
pattern = "dada"

first_letter_of_pattern = pattern[0]

len_of_text = len(given_text)
len_of_pattern = len(pattern)

total_match = 0

for index in range(len_of_text):
    if given_text[index] == first_letter_of_pattern:
        value = pattern_check(index)
        if value == True:
            total_match = total_match + 1

print("RESULT: ", total_match)
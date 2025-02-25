def get_suffixs(n):
    prepared_input = [0] * n
    for i in range(n):
        text = input()
        temp = [0] * (len(text) + 1)
        for j in range(len(text)):
            temp[j] = text[:j] + text[j + 1:]
        temp[len(text)] = text
        prepared_input[i] = temp
    return prepared_input

def find_int_pairs(prepared_input):
    answer = 0
    for seg in range(len(prepared_input[0])):
        suffixs = {}
        words_dict = {}
       
        for suff in prepared_input:
            suffix = suff[seg]
            word = suff[-1]
            if suffix in suffixs:
                repeats = 0
                if word in words_dict:
                  repeats = words_dict[word]
                answer += (suffixs[suffix] - repeats)
            else:
              suffixs[suffix] = 0
           
            suffixs[suffix] += 1
            words_dict[word] = words_dict.get(word, 0) + 1
    print(answer)
    
def main():
    n = int(input())
    find_int_pairs(get_suffixs(n))

if __name__ == "__main__":
    main()
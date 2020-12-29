s = "try hello wOrld"

def solution(s):
    string_list = s.split(" ")
    answer_part = []
    for i in range(len(string_list)):
        string_list_part = list(map(str, string_list[i]))
        for j in range(len(string_list_part)):
            if j%2 != 1:
                string_list_part[j] = string_list_part[j].upper()
            else:
                string_list_part[j] = string_list_part[j].lower()
        word = "".join(string_list_part)
        answer_part.append(word)
    answer = " ".join(answer_part)
    print(answer)
    return answer

solution(s)

# enumerate 익히기?
def palindrome_permutation(in_str):
    # t=O(n);s=O(n)
    arr = []
    in_str = in_str.lower()
    for char in in_str:
        if char == " ":
            continue
        if char in arr:
            arr.remove(char)
            continue
        arr.append(char)
        # print(array)
    if len(arr)<=1:
        return True
    return False

in_str1 = "Tacta Coa"
in_str2 = "Tact Coa"

result1 = palindrome_permutation(in_str1)
result2 = palindrome_permutation(in_str2)

print(in_str1, ": ", result1)
print(in_str2, ": ", result2)

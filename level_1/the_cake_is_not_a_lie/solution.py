def solution(s):
  for mm_count in range(1, len(s)+1):
    if len(s) % mm_count  != 0:
      continue

    seq = s[:mm_count]
    seq_index = 0
    success = True
    for i in range(mm_count, len(s)):
      if seq_index >= mm_count:
        seq_index = 0
      if seq[seq_index] != s[i]:
        success = False
        break
      seq_index += 1

    if success == True:
      return int(len(s) / mm_count)


print(solution("abcabcabcabc")) # expect 4
print(solution("abccbaabccba")) # expect 2
print(solution("abcabcabcabc")) # expect 4
print(solution("abccbaabccba")) # expect 2

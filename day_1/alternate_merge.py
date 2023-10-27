w1 = 'devesh'
w2 = '123'
new_w = []

leng = len(w1) + len(w2)

w1 += ' '
w2 += ' '

len1 = True
len2 = True

pw1 = 0
pw2 = 0

for i in range(1, leng+2):
  if i % 2 == 0 and len2:
    print(w2[pw2])
    len2 = w2[pw2] != ' '
    if len2:
      new_w.append(w2[pw2])
      pw2 += 1
  elif len1:
    len1 = w1[pw1] != ' '
    if len1:
      print(w1[pw1])
      new_w.append(w1[pw1])
      pw1 += 1

  print(len1, len2)
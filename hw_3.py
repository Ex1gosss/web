####1 
m = "грымнвмнмнннмвынмнннымвнмныынннннннннннннаспа"
s = 1
l = 0
for i in range(len(m)-1):
  if m[i] == "н" and m[i+1] == "н":
    s += 1
  else:
    s = 1
  if s > l:
    l = s
print(l, m.replace("н"*l, "!"*l))



####2
s = 'ыьмшкошыфжсфсф(ннннн)отвромаснежинск'
print(((s.split("("))[1].split(")"))[0])


####3
s = "shcuiehvhsvu акрия аллея фтугрмгфмшо аграгара"
lst = s.split(" ")
for i in lst:
  if (i[0] == "а" or i[0] == "А") and i[-1] == "я":
    if i == lst[-1]:
      print(i, end=".")
    else:
      print(i, end=", ")
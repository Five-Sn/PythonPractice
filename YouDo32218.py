#You Do Round 1
print "Round 1:"
def goBananas(x):
  print x + " is bananas"

goBananas("w356dr4yfutigybuhnijok")

#You Do Round 2
print "Round 2:"
def speak_spanish(m):
  if len(m) > 0:
    m[0] = "hola"

words = ["hello", "amigo"]
speak_spanish(words)
print words

# You Do Round 3
print "Round 3:"
listy_list = ["raindrops", "roses", "kittens", "kettle", "comet"]

listy_list.pop(3)
listy_list.append("mittens")
print listy_list

# You Do Round 4
print "Round 4:"
last_list = [3, 1, 4]
for x in last_list:
  print x * 2

print last_list

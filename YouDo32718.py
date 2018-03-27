# "for loop" review
x = [1, 2, 3]
for i in x:
  y = i + 1
  print "%d + 1 = %d" % (i , y)
  

# "while loop" example
count = 0
while count < 5:
  print "Hello! Count is %d" % (count)
  count += 1
  
print "Round 1:"
# Do Now Round 1
condition = True
while condition:
  print "Hey we looped!"
  condition = False

x = 0
while x < 4:
  print "Loop: %d" % (x)
  x += 1

print "Round 2:"
# Do Now Round 2
count = 0
while True:
  print "We're looping! Count: %d" % (count)
  count += 1
  if count == 10:
    break

# "for loop" example 1
#x = "hello"
#for i in x:
#  print i

print "Round 4:"
# Do Now Round 4 (write your code below)
my_string = "stringy"
for i in my_string:
  if i == "a" or i == "e" or i == "i"or i == "o"or i == "u":
    print "X"
  else:
    print i

print "Round 5:"
# Do Now Round 5
fruits_dictionary = {'b': 'berry','a': 'apple', 'c': 'cherry'}
for key in fruits_dictionary:
  if fruits_dictionary[key] == "apple":
    print "Found an apple!"
  else:
    print "Not an apple...."

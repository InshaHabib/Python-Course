# using time modules
# Example1
import time
# strftime is a function which provides minutes and hours
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

# Important link for time = https://docs.python.org/3/library/time.html#time.strftime

# Example2
""" from time import gmtime, strftime
timestamp = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
print(timestamp) """

# Example3
""" import time
timestamp = time.strptime("30 Nov 00", "%d %b %y") 
print(timestamp) """


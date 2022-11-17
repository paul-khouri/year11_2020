import sys
for i in range(0, 3):
    print(i)
##c=0
##print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
##contents = []
##while True:
##    try:
##        line = input()
##        print(repr(line))
##    except EOFError:
##        break
##    contents.append(line)
##    print(contents)
##print(contents)

inputlist = []
while True:
    line = input("In")
    if line:
        print(line)
    else:
        break
    inputlist.append(line)

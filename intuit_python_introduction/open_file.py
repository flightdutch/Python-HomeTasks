fhand = open('mbox.txt')
print(fhand)
count = 0
for line in fhand:
    count = count + 1

print('Line Count:', count)
print()

fhand = open('mbox-short.txt')
# inp = fhand.read()
# print(fhand)
# print(len(inp))
# print(inp[:20])
#print(inp)
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From '):
#         print(line)

print()
print(7%2 + 8/5)

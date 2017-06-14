"""Initialize your list (L = []) and follow the  commands given over  lines.

insert i e - Insert e at i-th position
print - Print the list
remove e - Delete first occurance of e
append e - Insert e at the end of list
sort - Sort the list
pop - Pop the last element
reverse - Reverse the list
Each command will be  of the  commands given above. Each command will have its own value(s) separated by a space (See example below).

Input Format

The first line contains an integer,  (the number of commands).
The  subsequent lines each contain one of the  commands described above."""

n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        eval("l."+cmd)
    else:
        print l


# This program generates 20 terms of a sequence by a recurrence relation.
Un = 100                    # Un = each term of the sequence. Initially = U0
x=0
while n>0:
    print(Un)
    Un = 1.01*Un - 1.01     # Set Un to the next term of the sequence
    x += 1

print ("Foram gerados", x, "valores")

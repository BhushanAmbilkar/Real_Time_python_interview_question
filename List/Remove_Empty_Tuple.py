l1 = [(), ('ram', '15', '8'), (), ('laxman', 'sita'),
      ('krishna', 'akbar', '45'), ('', ''), ()]

for i in l1:
    if i == ():
        l1.remove(i)
print(l1)

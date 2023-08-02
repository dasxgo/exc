## Counter stop 

counter = 0
while counter < 30:
    counter += 1
    if counter == 20:
        break
    print(counter)

print('='*64)

## Counter continue

counter = 0
while counter < 20:
  counter += 1
  if counter <= 15:
    continue
  print(counter)

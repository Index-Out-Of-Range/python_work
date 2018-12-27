def average():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum / count


avg_g = average()
avg_g.__next__()
avg1 = avg_g.send(10)
avg1 = avg_g.send(20)
print(avg1)

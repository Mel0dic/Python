def median(alist):
    new = []
    counter = []
    for i in range(0, 1000):
        counter.append(0)
    for i in range(0, len(alist)):
        counter[alist[i]] += 1
    for i in range(0, 1000):
        if counter[i] > 0:
            for k in range(0, counter[i]):
                new.append(i)
    print(new)
    if (len(new) % 2) == 0:
        return (float(new[int((len(new)/2)-1)]) + float(new[int((len(new)/2))])) / 2.0
    else:
        return new[int(len(new)/2)] 
    
alist = [-1, 2, 6, -5, 4, 2, 9]
print(median(alist))

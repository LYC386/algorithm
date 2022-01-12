def maxsubarray(array):
    cur_max=0
    global_max=-9999999
    for i in range(len(array)):
        cur_max = max(array[i],cur_max+array[i])
        if cur_max > global_max:
            global_max = cur_max
        
    return global_max

if __name__ == "__main__":
    print(maxsubarray([100,-40,299,300,500,-100000]))
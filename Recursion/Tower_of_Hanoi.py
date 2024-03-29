
def hanoi(disk, source, middle, destination):
    if disk == 0:
        print("Disk %s from %s to %s" % (disk, source, destination))
        return
    hanoi(disk-1, source, destination, middle)
    # This is not necessarily the largest plate, and it is not the smallest one.
    print("Disk %s from %s to %s" % (disk, source, destination))
    hanoi(disk-1, middle, source, destination)


hanoi(3, 'A', 'B', 'C')
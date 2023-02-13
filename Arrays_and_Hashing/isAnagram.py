def isAnagram(s, t):
    if len(s) != len(t):
        return False

    elif sorted(s.lower()) == sorted(t.lower()):
        return True

    else:
        return False


print(isAnagram('Ship', 'Hips'))

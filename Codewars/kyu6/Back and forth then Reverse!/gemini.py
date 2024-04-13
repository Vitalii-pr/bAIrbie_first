def arrange(s):
    T = []
    left = 0
    right = len(s) - 1
    work_list = s.copy()

    while left <= right:
        T.append(work_list[left])
        if left != right:
            T.append(work_list[right])
        left += 1
        right -= 1
        work_list[left:right + 1] = work_list[left:right + 1][::-1]
    return T

    def arrange_helper(s, T):
        if not s:
            return T
        T.append(s[0])
        if len(s) > 1:
            T.append(s[-1])
        return arrange_helper(s[1:-1][::-1], T)

    return arrange_helper(s.copy(), [])  

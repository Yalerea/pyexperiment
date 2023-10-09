def bouncing_ball(h, bounce, window):
    m = h
    t = 1
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    else:
        while m*bounce > window:
            m = m*bounce
            t+=2
    return t
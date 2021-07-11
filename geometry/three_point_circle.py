# center_x, center_y, radius
def three_point_circle(x1, y1, x2, y2, x3, y3):
    i = 2 * (x1-x2)
    j = 2 * (y1-y2)
    k = 2 * (x1-x3)
    l = 2 * (y1-y3)
    c = x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2
    d = x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2
    deno = k * j - i * l 
    if deno == 0: return [INF, INF], 0
    y = (c*k-d*i) / deno
    x = (d*j-c*l) / deno
    r = (x1-x) ** 2 + (y1-y) ** 2
    return [x, y], r ** 0.5
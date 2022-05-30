x,y,w,h = map(int, input().split())

x_to_w = w - x
y_to_h = h - y

data = [x, y, x_to_w, y_to_h]

print(min(data))

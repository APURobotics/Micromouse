// Let's test this file here
def get_map(n):
  matrix = []
  for i in range(n):
    row = [0] * n
    matrix.append(row)
  return matrix

size = 8
mouse_map = get_map(size)

for i in range (size)
  for j in range (size)
    if (i % j = 1):
      mouse_map[i][j] = 1;
print(f"Matrix where i modulo j = 1\n{mouse_map}");

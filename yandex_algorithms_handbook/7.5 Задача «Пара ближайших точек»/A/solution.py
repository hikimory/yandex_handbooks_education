def distance(p1, p2):
  return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

def closest_pair(points):
  # Base case: for a small number of points we use a simple algorithm
  if len(points) <= 3:
    distances = []
    for i, p1 in enumerate(points):
      for p2 in points[i+1:]:
        distances.append(distance(p1, p2))
    return min(distances)

  # Sort the points by x and find the midpoint
  points.sort(key=lambda p: p[0])
  mid = len(points) // 2
  left = points[:mid]
  right = points[mid:]

  # Recursively find the closest pairs in the left and right subsets
  dl = closest_pair(left)
  dr = closest_pair(right)

  # Find the minimum distance from two subsets
  min_dist = min(dl, dr)

  # Create a 2d wide strip around the dividing line
  mid_x = (left[-1][0] + right[0][0]) / 2
  strip = [p for p in points if abs(p[0] - mid_x) < min_dist]

  # Sort the points in the strip by y
  strip.sort(key=lambda p: p[1])

  # Checking the distances between points in the strip
  for i in range(len(strip) - 1):
    for j in range(i+1, min(i+8, len(strip))):
      dist = distance(strip[i], strip[j])
      if dist > min_dist:
        break
      if dist < min_dist:
          min_dist = dist
  return min_dist
    
def main():
  n = int(input())
  points = []
  for _ in range(n):
    (x, y) = map(int, input().split())
    points.append((x, y))
  
  print(round(closest_pair(points), 6))

if __name__ == "__main__":
  main()
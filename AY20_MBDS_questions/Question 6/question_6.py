vertices  = []
points  = []

file = open('input_question_6_polygon', 'r') 
for each in file: 
  vertex = []
  x, y = each.strip().split(" ")
  vertex.append(x)
  vertex.append(y)
  vertices.append(vertex)

file = open('input_question_6_points', 'r') 
for each in file: 
  point = []
  x, y = each.strip().split(" ")
  point.append(x)
  point.append(y)
  points.append(point)

for point in points:
	point.append(point[0])
	point.append(0)  #Creating vertical line coordinates by extrapolating each point perpendicular to the x-axis

for i in range(-1,len(vertices)-1):
	vertices[i].append(vertices[i+1][0])
	vertices[i].append(vertices[i+1][1])  #Creating edges from polyon vertices

print(points)





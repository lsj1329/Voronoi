from PIL import Image
import random
import math

Rt = [(50,250),(200,100),(200,200),(200,300),(200,400),(260,100),(260,200),(260,300),(260,400),(320,200),(320,300),(380,200),(380,300),(440,100),(440,200),(440,300),(440,400),(500,100),(500,200),(500,300),(500,400),(650,250)]

def generate_voronoi_diagram(width, height, num_cells):
  image = Image.new("RGBA", (width, height))
  putpixel = image.putpixel
  imgx, imgy = image.size
  nx = []
  ny = []
  nr = []
  ng = []
  nb = []
  for i in range(num_cells):
    nr.append(random.randrange(256))
    ng.append(random.randrange(256))
    nb.append(random.randrange(256))

  for y in range(imgy):
    for x in range(imgx):
      dmin = math.hypot(imgx, imgy)

      j=-1
      for i in range(num_cells):
        d = math.hypot(Rt[i][0]-x, Rt[i][1]-y)
        if d < dmin:
          dmin = d
          j = i
      putpixel((x, y), (nr[j], ng[j], nb[j]))

  image.save("VoronoiDiagram.png", "PNG")
  image.show()


generate_voronoi_diagram(700, 500, len(Rt))
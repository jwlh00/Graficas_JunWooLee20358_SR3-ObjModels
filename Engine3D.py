from gl import Renderer, color, V3, V2
from obj import Obj

width = 1000
height = 2000

rend = Renderer(width, height)

rend.glLoadModel("body.obj",
                 translate = V3(width/2, height/4, 0),
                 scale = V3(200,200,200))

rend.glFinish("output.bmp")
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

grass_texture = load_texture('assets/grass.png')
sky_texture = load_texture('assets/sky.png')


brick_texture= load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
oak_texture = load_texture('assets/oak.png')
stone_texture = load_texture('assets/stone_block.png')
wood_texture = load_texture('assets/wood.png')

current_texture = grass_texture

def update():
    global current_texture

    if held_keys['1']:
        current_texture = grass_texture
    if held_keys['2']:
        current_texture = dirt_texture
    if held_keys['3']:
        current_texture = oak_texture
    if held_keys['4']:
        current_texture = brick_texture
    if held_keys['5']:
        current_texture = stone_texture
    if held_keys['6']:
        current_texture = wood_texture


    if  held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive
    


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            scale = 150,
            texture = sky_texture,
            double_sided = True
        )

class Hand(Entity):

    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            scale = (0.2, 0.3),
            color = color.white,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.4)
            )
        
    def active(self):
        self.position = Vec2(0.1, -0.5),
        self.rotation = Vec3(90, -10, 0)

    def passive(self):
        self.rotation = Vec3(150, -10, 0),
        self.position = Vec2(0.4, -0.4)

class Voxel(Button):
    def __init__(self, position = (0, 0, 0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = texture,
            color=color.color(0, 0, 255),
            highlight_color=color.lime
        )


    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position = self.position  + mouse.normal, texture = current_texture)

            if key == 'left mouse down':
                destroy(self)


# генерация ладшафта плоский квадрат
for z in range(15):
     for x in range(15):
         voxel = Voxel((x, 0, z))


# все превращается в куб и даже персонаж появляется в кубе/чтобы выйти нужно подпрыгнуть
# for z in range(8):
#     for x in range(8):
#         for y in range(8):
#             voxel = Voxel((x, y, z))


player = FirstPersonController()
sky = Sky()
hand = Hand()
app.run()

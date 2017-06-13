import cocos
from cocos.actions import *
import os


class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        # blueish color
        super( HelloWorld, self ).__init__( 64,64,224,255)

        label = cocos.text.Label('Hello Youngster!',
                                font_name='Times New Roman',
                                font_size=32,
                                anchor_x='center', anchor_y='center')

        # set the label in the center of the screen
        label.position = 320,240
        self.add( label )

        sprite = cocos.sprite.Sprite('fish.png')
        sprite.position = 320,240
        sprite.scale = 0.2
        self.add( sprite, z=1 )

        scale = ScaleBy(3, duration=2)

        label.do( Repeat( scale + Reverse( scale) ) )
        sprite.do( Repeat( Reverse(scale) + scale ) )

os.system("start music.mp3")

cocos.director.director.init()
hello_layer = HelloWorld ()
hello_layer.do( RotateBy(360, duration=10) )

# A scene that contains the layer hello_layer
main_scene = cocos.scene.Scene (hello_layer)

# And now, start the application, starting with main_scene
cocos.director.director.run (main_scene)







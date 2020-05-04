face = TextSprite("😃", fontSize = 40, x = 200, y = 175)

frame = 0

@loop_animation

graphics.clear()
if frame == 0:
    face.image.text = "😃"
if frame == 10:
    face.image.text = "😄"
if frame == 20:
    face.image.text = "😁"
if frame == 30:
    face.image.text = "😄"
if frame == 40:
    frame = -1
    
frame = frame + 1
    
graphics.drawSprite(face)
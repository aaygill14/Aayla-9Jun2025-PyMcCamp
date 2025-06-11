# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER



def teleport():
    agent.teleport_to_player()
player.on_chat("tp", teleport)

def turnleft():
    agent.turn(LEFT)
player.on_chat("tl", turnleft)

def on_right():
    agent.turn(RIGHT)
player.on_chat("tr",on_right)

def forward(steps):
    agent.move(FORWARD, steps)
player.on_chat("front", forward)

def back(steps):
    agent.move(BACK, steps)
player.on_chat("back", back)

def up(steps):
   agent.move(UP, steps)
player.on_chat("up", up)

def down(steps):
    agent.move(DOWN, steps)
player.on_chat("down", down)

def move1():
    agent.move(FORWARD, 4)
    agent.turn(LEFT)
    agent.move(FORWARD, 4)
    agent.turn(RIGHT)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(FORWARD, 2)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
player.on_chat("obby1", move1)

def move2():
    agent.move(UP, 1)
    agent.move(BACK, 1)
    agent.move(UP, 1)
    agent.move(BACK, 1)
    agent.move(UP, 1)
    agent.move(BACK, 2)
    agent.move(BACK, 1)
    agent.move(DOWN, 1)
    agent.move(BACK, 1)
    agent.move(DOWN, 1)
    agent.move(BACK, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
player.on_chat("obby2", move2)

def choptree(height):
    for count in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, height)
    agent.collect_all()
player.on_chat("chop", choptree)

def mining():
    for count in range (10):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)
player.on_chat("mine", mining)

def build():
    for count in range(6):
        for outer in range (5):
            agent.place(FORWARD)
            agent.move(RIGHT, 1)
            
        agent.move(LEFT, 5)
        agent.move(UP, 1)
player.on_chat("build", build)

def pillar():
    for ouuter in range (6):
        agent.place(FORWARD)
        agent.move(UP, 1)
player.on_chat("pillar", pillar)
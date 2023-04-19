import random

def generate_story():
    story = ""
    story_parts = ["Der Knecht ist im Schacht erwacht", "Haha, a Frosch!", "Und dann fand der Knecht endlich den Ausgang, und doch war er traurig, denn soviele Abenteuer wie in diesem Schacht hatte er noch nie erlebt!", "Und dann traf er an einer Weggabelung einen Goblin, der ihn aber Freundlich begrüte \"He, bist du neu hier im Schacht?!?\""]
    story_parts_capitalism = ["Der Knecht war im Schacht gefangen, aber dort war er freier als an der Oberwelt.", "Er traf viele interessante Gestalten, die alle ganz aberwitzige Geschichten erzählten."]
    rooms = ["Er kam eine Etage hoch", "Er ging durch einen dunklen Tunnel", "Er betrat eine große Halle"]
    encounters = ["da traf er auf einen Oger der einen Wurststand hatte", "da sah er eine Gruppe von Zwergen die ein Lied sangen", "da begegnete er einem Einhorn das ihm den Weg wies"]
    
    story += random.choice(story_parts) + " "
    story += random.choice(story_parts_capitalism) + " "
    
    for i in range(3):
        story += random.choice(rooms) + ", "
        story += random.choice(encounters) + ". "
    
    return story

print(generate_story())

from typing import List

from entity import Entity
from game_map import GameMap
from camera import Camera

def render_all(entities: List[Entity], game_map: GameMap, colors, camera: Camera):
    # Draw the map
    game_map.render(colors=colors, camera=camera)

    # Draw all entities in the list
    for entity in entities:
        if game_map.fov[entity.x, entity.y]:
            entity.draw(camera)

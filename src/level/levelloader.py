from level.tile import TileType, Tile


def load_level(level):
    file = open("level/files/" + level.get_level_name(), "r")
    y = 0
    for line in file:
        x = 0
        x_tiles = []
        for char in line:
            tile_type = None
            if char == "0":
                tile_type = TileType.AIR
            elif char == "1":
                tile_type = TileType.GROUND
            elif char == "2":
                tile_type = TileType.SPIKE
            else:
                break
            x_tiles.append(Tile(tile_type, x, y))
            x += 1
        level.get_tiles().append(x_tiles)
        y += 1
    file.close()

    file = open("level/files/" + level.get_level_name(), "r")
    y = 0
    for line in file:
        x = len(line) - 2
        """
            Pourquoi -2 ?
            len(line) renvoie le nombre de caractères sur une ligne mais nous on veut compter à partir de 0 donc cela fait déjà -1
            Ensuite on a le \n à la fin qu'il faut supprimer donc encore -1

            Donc -1 - 1 = -2
        """
        x_tiles = []
        for char in line:
            tile_type = None
            if char == "0":
                tile_type = TileType.AIR
            elif char == "1":
                tile_type = TileType.GROUND
            elif char == "2":
                tile_type = TileType.SPIKE
            else:
                break
            x_tiles.append(Tile(tile_type, x, y + 9))
            x -= 1
        level.get_tiles().append(x_tiles)
        y += 1
    file.close()

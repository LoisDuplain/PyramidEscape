from level.tile import Tile, TileType


def load_tiles(level):
    file = open("level/files/" + level.get_level_name(), "r")
    rows = file.read().split("\n")
    for y in range(len(rows)):
        row = rows[y]
        columns = row.split("-")

        tile_row = []

        for x in range(len(columns)):
            column = columns[x].replace("(", "").replace(")", "").replace(" ", "").replace("\"", "")

            params = column.split(",")

            tile_type = None
            if params[0] == "air":
                tile_type = TileType.AIR
            elif params[0] == "ground":
                tile_type = TileType.GROUND
            elif params[0] == "spike":
                tile_type = TileType.SPIKE
            else:
                break

            tile = Tile(tile_type, x, y)

            if len(params) > 1:
                for param_index in range(1, len(params)):
                    param_value_by_key = params[param_index].split(":")
                    tile.get_params()[param_value_by_key[0]] = param_value_by_key[1]

            tile_row.append(tile)

        level.get_tiles().append(tile_row)

    file = open("level/files/" + level.get_level_name(), "r")
    rows = file.read().split("\n")
    for y in range(len(rows)):
        if y <= 0:
            continue

        row = rows[y]
        columns = row.split("-")
        columns.reverse()

        tile_row = []

        for x in range(len(columns)):
            column = columns[x].replace("(", "").replace(")", "").replace(" ", "").replace("\"", "")

            params = column.split(",")

            tile_type = None
            if params[0] == "air":
                tile_type = TileType.AIR
            elif params[0] == "ground":
                tile_type = TileType.GROUND
            elif params[0] == "spike":
                tile_type = TileType.SPIKE
            else:
                break

            tile = Tile(tile_type, x, y + len(rows) - 1)

            if len(params) > 1:
                for param_index in range(1, len(params)):
                    param_value_by_key = params[param_index].split(":")
                    tile.get_params()[param_value_by_key[0]] = param_value_by_key[1]

            tile_row.append(tile)

        level.get_tiles().append(tile_row)

    file.close()
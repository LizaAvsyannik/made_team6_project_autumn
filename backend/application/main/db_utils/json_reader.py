import json
import math
import re


def publications_reader(file, limit=None):
    if limit is None:
        limit = math.inf
    publications_read = 0

    with open(file, "r") as json_file:
        line = json_file.readline()
        lines = []
        while publications_read <= limit and (not line.startswith("]")):
            line = json_file.readline()
            lines.append(line)
            if line.startswith("},"):
                lines[-1] = "}"
                json_string = "".join(lines)
                lines.clear()
                json_string = re.sub(r"NumberInt\((\d*)\)", r"\1", json_string)
                publication = json.loads(json_string)
                publications_read += 1
                yield publication


def value_or_None(json_dict: dict, key, cast=None):
    if key in json_dict:
        if cast is None:
            return json_dict[key]
        return cast(json_dict[key])
    return None

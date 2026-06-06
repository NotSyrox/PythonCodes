# First code of the day so written by ai

def merge_grouped(d1, d2):
    result = {}

    all_keys = set(d1) | set(d2)

    for key in all_keys:
        values = []   # ← this creates an empty list

        if key in d1:
            values.append(d1[key])

        if key in d2:
            values.append(d2[key])

        result[key] = values

    return result


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

print(merge_grouped(d1, d2))

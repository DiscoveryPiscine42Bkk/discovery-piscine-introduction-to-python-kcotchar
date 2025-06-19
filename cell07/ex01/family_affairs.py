def dummo(family):
    return list(filter(lambda name: family[name]== "dummo", family.keys()))

dupont_family = {
    "mo": "mo",
    "dum": "dum",
    "mairu": "tem",
    "khemika": "mo",
    "cotcharit": "mo"
}

print(dummo(dupont_family))
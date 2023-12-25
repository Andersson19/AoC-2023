import helper as h
from itertools import combinations

seed_to_soil   = {}
soil_to_fert   = {}
fert_to_water  = {}
water_to_light = {}
light_to_temp  = {}
temp_to_humid  = {}
humid_to_loc   = {}

mappings = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]

def get_mapping(name):
    match name:
        case "seed-to-soil map:":
            return seed_to_soil
        case "soil-to-fertilizer map:":
            return soil_to_fert
        case "fertilizer-to-water map:":
            return fert_to_water
        case "water-to-light map:":
            return water_to_light
        case "light-to-temperature map:":
            return light_to_temp
        case "temperature-to-humidity map:":
            return temp_to_humid
        case "humidity-to-location map:":
            return humid_to_loc

def init_mappings(lines):
    curr_map = seed_to_soil

    for line in lines:
        if line.strip():
            if 'map' in line:
                curr_map = dict(sorted(curr_map.items()))
                curr_map = get_mapping(line)
            else:
                values = line.split(" ")
                destination_start = int(values[0])
                source_start = int(values[1])
                value_range = int(values[2])
                
                curr_map[destination_start] = {"start": source_start, "count": value_range}

    # print(f"{curr_map}\n")

def get_source(location, mapping):
    print(mapping)
    new_location = location
    for destination in mapping:
        if location >= destination:
            dest_max = destination + mapping[destination]["count"]
            if location < dest_max:
                tmp = location - destination
                new_location = tmp + mapping[destination]["start"]
                break

    print(f"{location} -> {new_location}")
    return new_location

    destination = start
    for source in mapping:
        # print("Restarting")
        # print(f"{start} > {source} (greater than source?)")
        if start >= source:
            # print(f"{start} < {source+mapping[source]['count']} (less than source + count?)")
            if start < source+mapping[source]["count"]:
                diff = start - source
                # print(f"{start} - {source} = {diff} (diff)")
                destination = mapping[source]["start"] + diff
                # print(f"{mapping[source]['start']} + diff = {destination} (destination)")
                # print(f"Returning: {destination}")
                break
    
    return destination

def get_mapping_by_id(idx):
    match idx:
        case 0:
            return "soil"
        case 1:
            return "fertilizer"
        case 2:
            return "water"
        case 3:
            return "light"
        case 4:
            return "temp"
        case 5:
            return "humidity"
        case 6:
            return "location"
    
def find_seed(location):
    curr_location = location
    mappings.reverse()
    for idx, map in enumerate(mappings):
        curr_map = get_mapping(map)

        curr_location = get_source(curr_location, curr_map)

    return curr_location

def found_seed(location, seed_ranges):
    seed = find_seed(location)

    print(f"Location {location} gave seed {seed}..")
    for range in seed_ranges:
        print(f" > Checking if seed {seed} is in {range}..")
        if seed in range:
            return True
    return False
    

if __name__ == "__main__":
    path = './inputs/5.txt'
    test = './inputs/5-test.txt'

    lines = h.read_file(path)
    
    tmp_seeds = lines[0].split(": ")[1].split(" ")
    seeds = []

    for i in range(0, len(tmp_seeds), 2):
        r = [int(tmp_seeds[i]), int(tmp_seeds[i]) + int(tmp_seeds[i+1])]
        seeds.append(r)

    lines = lines[2:]

    init_mappings(lines)

    location = 0
    done = False
    while not done:  
        if found_seed(location, seeds):
            print(f"Lowest location: {location}")
            done = True
        else:
            location += 3
            continue


        



import helper as h

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
                
                curr_map[source_start] = {"start": destination_start, "count": value_range}

    # print(f"{curr_map}\n")

def get_destination(start, mapping):
    destination = start
    for source in mapping:
        print("Restarting")
        print(f"{start} > {source} (greater than source?)")
        if start > source:
            print(f"{start} < {source+mapping[source]['count']} (less than source + count?)")
            if start < source+mapping[source]["count"]:
                diff = start - source
                print(f"{start} - {source} = {diff} (diff)")
                destination = mapping[source]["start"] + diff
                print(f"{mapping[source]['start']} + diff = {destination} (destination)")
                print(f"Returning: {destination}")
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
        
def find_location(seed):
    curr_location = seed

    st = "\nSeed " + str(seed) + ", "
    for idx, map in enumerate(mappings):
        st += get_mapping_by_id(idx) + " "

        curr_map = get_mapping(map)

        curr_location = get_destination(curr_location,curr_map)

        st += str(curr_location) + ", "

    print(st[:-1])
    return curr_location
    

if __name__ == "__main__":
    path = './inputs/5.txt'
    test = './inputs/5-test.txt'

    lines = h.read_file(path)
    
    seeds = lines[0].split(": ")[1].split(" ")

    for i in range(len(seeds), step=2):
        print(seeds)

    lines = lines[2:]

    init_mappings(lines)

    lowest = -1
    location = 0
    for id, seed in enumerate(seeds):
        print(f"Current seed: {seed}")
        print(f"Remaining seeds: {seeds[id+1:]}")
        seed = int(seed)
        if lowest == -1:
            lowest = find_location(seed)
            print(f"\n\n----------------NEW LOW------------------\n\tprevious: (none)\n\tnew: {lowest}\n-----------------------------------------")
        else:
            location = find_location(seed)

            if location < lowest:
                print(f"\n\n----------------NEW LOW------------------\n\tprevious: {lowest}\n\tnew: {location}\n-----------------------------------------")
                lowest = location

    print(f"Lowest location: {lowest}")

        



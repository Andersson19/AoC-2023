import helper as h

def update_scratchcards(winning, numbers, card_id, scratchcards_instances):
    next_scratchcard = card_id + 1
    
    # Count how many items in numbers are in winning
    arr = [1 for item in set(numbers) if item in set(winning)]
    count = sum(arr)

    instances = scratchcards_instances[card_id]

    # for every instance of this card, add the right amount of copies to the following cards
    for c in range(next_scratchcard, next_scratchcard+count):
        scratchcards_instances[c] += 1*instances

    return scratchcards_instances

def sum_scratchcard_instances(scratchcards):
    sum = 0
    for card in scratchcards:
        sum += scratchcards[card]
    return sum

if __name__ == "__main__":
    path = "./inputs/4.txt"
    test = "./inputs/4-test.txt"

    lines = h.read_file(path)
    total = 0
    scratchcards_instances = {}

    # Initialize scratchcards_instances with the first card
    for i in range(1,len(lines)+1):
        scratchcards_instances[i] = 1
   
    for idx, line in enumerate(lines):
        card_instance_number = idx+1

        # add original card to the existing copies

        card_numbers = line.split(": ")[1]
        winning = list(filter(lambda x: x.isdigit(), card_numbers.split(" | ")[0].split(" ")))
        numbers = list(filter(lambda x: x.isdigit(), card_numbers.split(" | ")[1].split(" ")))

        scratchcards_instances = update_scratchcards(winning, numbers, card_instance_number, scratchcards_instances)
    print("Sum of scratchcards: {}".format(sum_scratchcard_instances(scratchcards_instances)))
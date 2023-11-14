import pandas


def calculate_dice_probabilities_multiple_rolls(rolls):
    # Define the dice
    dice = [4, 6, 8, 12, 20]

    # Prior probability for each die (equal probability of picking any die)
    prior_prob = 1 / len(dice)

    # Initialize dictionary to hold combined probabilities for each die
    combined_probs = {die: prior_prob for die in dice}

    # Calculate probabilities for each roll
    for roll in rolls:
        # Calculate the likelihood of rolling the number with each die
        likelihoods = [1 / die if roll <= die else 0 for die in dice]

        # Calculate the total probability of rolling the number (evidence)
        total_prob = sum(likelihoods) * prior_prob

        # Update combined probabilities for each die
        for i, die in enumerate(dice):
            combined_probs[die] *= (likelihoods[i] * prior_prob) / total_prob if total_prob else 0

    # Normalize the probabilities so they sum to 1
    total = sum(combined_probs.values())
    normalized_probs = {die: prob / total for die, prob in combined_probs.items()}

    # Convert to DataFrame for better visualization
    df = pandas.DataFrame(list(normalized_probs.items()), columns=['Die', 'Probability'])
    return df


rolls = []

number_of_rolls = int(input("How many times do you wish to roll the dice? "))
for n in range(number_of_rolls):
    value = int(input("Enter value of die rolled: "))
    rolls.append(value)

print(calculate_dice_probabilities_multiple_rolls(rolls))

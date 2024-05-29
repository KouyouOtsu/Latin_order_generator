import numpy as np
import pandas as pd

def generate_latin_square(n):
    """
    Generate a standard Latin square of size n.
    """
    base = np.array(range(n))
    latin_square = np.array([np.roll(base, -i) for i in range(n)])
    return latin_square

def shuffle_rows_and_columns(square):
    """
    Shuffle rows and columns of the Latin square independently.
    """
    rng = np.random.default_rng()
    print(square)
    matrix2d = rng.permutation(square, axis=0)
    print(matrix2d)
    matrix2d = rng.permutation(matrix2d, axis=1)
    print(matrix2d)
    return matrix2d

def generate_experiment_order(latin_square, participants):
    """
    Generate experiment orders for participants using the standard and shuffled Latin squares.
    """
    n = len(latin_square)
    orders = []

    # First 4 participants use the standard Latin square
    for i in range(min(participants, n)):
        orders.append(latin_square[i])

    # Remaining participants use shuffled Latin squares
    shuffled_square=[]
    for i in range(n, participants):
        if i%n==0:
            shuffled_square = shuffle_rows_and_columns(np.copy(latin_square))
        order = shuffled_square[i % n]
        orders.append(order)
    
    return orders

def save_orders_to_csv(orders, filename):
    """
    Save the generated orders to a CSV file.
    """
    df = pd.DataFrame(orders, columns=[f"Condition {i+1}" for i in range(len(orders[0]))])
    df.index = [f"Participant {i+1}" for i in range(len(orders))]
    df.to_csv(filename, index_label="Participant")

# Parameters
n = 4  # Number of conditions (4-levels)
participants = 40  # Number of participants (adjust as needed)

# Generate a standard Latin square
latin_square = generate_latin_square(n)

# Generate experiment orders for participants
orders = generate_experiment_order(latin_square, participants)

# Save the generated orders to a CSV file
filename = 'experiment_orders.csv'
save_orders_to_csv(orders, filename)

print(f"Experiment orders saved to {filename}")

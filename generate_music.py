import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

print("Loading music model...")

# Load trained model
model = load_model("music_model.keras")

# Load notes
with open("notes.json", "r") as f:
    notes = json.load(f)

# Get unique notes
unique_notes = sorted(set(notes))

# Convert notes to numbers
note_to_int = {
    note: i for i, note in enumerate(unique_notes)
}

int_to_note = {
    i: note for note, i in note_to_int.items()
}

# Sequence length used during training
sequence_length = 20

# Choose a starting sequence
start = np.random.randint(
    0,
    len(notes) - sequence_length
)

pattern = [
    note_to_int[note]
    for note in notes[start:start + sequence_length]
]

# Number of notes to generate
prediction_length = 100

generated_notes = []

print("Generating music...")

for _ in range(prediction_length):

    # Prepare input
    prediction_input = np.reshape(
        pattern,
        (1, sequence_length, 1)
    )

    # Normalize
    prediction_input = prediction_input / float(len(unique_notes))

    # Predict next note
    prediction = model.predict(
        prediction_input,
        verbose=0
    )

    # Choose the note with highest probability
    index = np.random.choice(
    len(prediction[0]),
    p=prediction[0]
)

    result = int_to_note[index]

    # Add generated note
    generated_notes.append(result)

    # Update pattern
    pattern.append(index)
    pattern = pattern[1:]

# Save generated notes
with open("generated_notes.json", "w") as f:
    json.dump(generated_notes, f)

print()
print("Music generation completed!")
print("Generated notes:", len(generated_notes))
print("Saved as generated_notes.json")
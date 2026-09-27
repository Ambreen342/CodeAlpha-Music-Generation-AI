import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

print("Loading notes...")

# Load notes
with open("notes.json", "r") as f:
    notes = json.load(f)

print("Total notes:", len(notes))

# Unique notes
unique_notes = sorted(set(notes))

print("Unique notes:", len(unique_notes))

# Convert notes to numbers
note_to_int = {
    note: i for i, note in enumerate(unique_notes)
}

# Sequence length
sequence_length = 20

network_input = []
network_output = []

# Create training sequences
for i in range(len(notes) - sequence_length):
    sequence = notes[i:i + sequence_length]
    next_note = notes[i + sequence_length]

    network_input.append(
        [note_to_int[note] for note in sequence]
    )

    network_output.append(
        note_to_int[next_note]
    )

print("Training sequences:", len(network_input))

# Convert to NumPy
network_input = np.array(network_input)

# Reshape for LSTM
network_input = np.reshape(
    network_input,
    (len(network_input), sequence_length, 1)
)

# Normalize
network_input = network_input / float(len(unique_notes))

# Convert output to categories
network_output = to_categorical(
    network_output,
    num_classes=len(unique_notes)
)

# Create model
model = Sequential()

model.add(
    LSTM(
        128,
        input_shape=(sequence_length, 1),
        return_sequences=True
    )
)

model.add(Dropout(0.3))

model.add(LSTM(128))

model.add(Dropout(0.3))

model.add(
    Dense(
        len(unique_notes),
        activation="softmax"
    )
)

# Compile
model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)

print("Model created!")
print("Starting training...")

# Train
model.fit(
    network_input,
    network_output,
    epochs=10,
    batch_size=32
)

# Save model
model.save("music_model.keras")

print()
print("Training completed!")
print("Model saved as music_model.keras")
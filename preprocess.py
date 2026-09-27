from music21 import converter
import os
import json

dataset_folder = "dataset"
notes = []

midi_files = [
    file for file in os.listdir(dataset_folder)
    if file.lower().endswith((".mid", ".midi"))
]

print("MIDI files found:", len(midi_files))

# Process only the first 2 files
for file in midi_files[:2]:

    file_path = os.path.join(dataset_folder, file)

    print("Processing:", file)

    try:
        song = converter.parse(file_path)

        count = 0

        for element in song.flatten().notes:
            if element.isNote:
                notes.append(str(element.pitch))
                count += 1

            elif element.isChord:
                notes.append(".".join(str(n) for n in element.normalOrder))
                count += 1

        print("Notes extracted:", count)

    except Exception as e:
        print("Skipped:", file)
        print("Reason:", e)

# Save notes
with open("notes.json", "w") as f:
    json.dump(notes, f)

print()
print("Total notes extracted:", len(notes))
print("Saved to notes.json")
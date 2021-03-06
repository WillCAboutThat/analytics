import matplotlib.pyplot as plt

# Our data
labels = ["Javascript", "Java", "Python", "C#"]
usage = [69.8, 45.3, 38.8, 34.4]

# Generating the y positions. Later, we'll use them to replace them with labels.
y_positions = range(len(labels))

#Creating our bar plot
plt.bar(y_positions, usage)
plt.xticks(y_positions, labels)
plt.ylabel("Usage (%)")
plt.title("Programming Language Usage")
plt.show()

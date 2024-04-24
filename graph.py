# Write a Python programming to display a bar chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
# Define colors for each bar
colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow']
plt.bar(x_pos, popularity, color=colors)
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
plt.show()




# Write a Python programming to create a pie chart with a title of the popularity of programming Languages.
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
import matplotlib.pyplot as plt
# Plot data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# Define colors for each slice
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# Explode 1st slice
explode = (0.1, 0, 0, 0, 0, 0)
# Plot pie chart
plt.pie(popularity, explode=explode, labels=languages, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Popularity of Programming Language Worldwide, Oct 2022 compared to a year ago",
          bbox={'facecolor':'0.8', 'pad':5})
plt.show()

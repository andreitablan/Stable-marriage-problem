# Stable marriage problem
- [Wikipedia](https://en.wikipedia.org/wiki/Stable_marriage_problem  "Wikipedia")
- Implement a solution to the matching problem using a state-based model and at least two different strategies from the list: Backtracking, Greedy, Hillclimbing, A*.
- The application should have a graphical interface where we can view and configure participants' preferences, as well as the resulting matches.
### How to run the application from the command line:
```
# Start the graphic interface
python Project/app/main.py
# -I for input, input for men, input for women, and the type of algorithm
pyhton Project/app/main.py -I <input_men.txt> <input_women.txt> greedy
python Project/app/main.py -I <input_men.txt> <input_women.txt> bkt
# -R for generating a random input, number of people, the type of algorithm used
python Project/app/main.py -R <number_of_people greedy
python Project/app/main.py -R <number_of_people> bkt
```
#### Relevant links:
- [The Stable Marriage Problem](https://community.wvu.edu/~krsubramani/courses/fa01/random/lecnotes/lecture5.pdf "The Stable Marriage Problem")
- [Stable Matching: Video](https://www.youtube.com/watch?v=RE5PmdGNgj0 "Stable Matching: Video")
- [App Demo](https://youtu.be/iXtSYavHh7U)
## Authors
###### [Andrei Tablan](https://github.com/andreitablan "Andrei Tablan")
###### [Andrei Ciuta](https://github.com/ciuta)
###### [Dan Leagan](https://github.com/leagan-dan)
###### [Alexandra Volentir](https://github.com/AlexandraVolentir)

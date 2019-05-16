"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:
quizz_file = open('questions.txt', 'r')
quizz = [tuple(line.strip().split('=')) for line in quizz_file.readlines()]
quizz_file.close()

correct_answer_count = 0
for item in quizz:
    answer = input(f'{item[0]}=')
    if answer == item[1]:
        correct_answer_count += 1

result_file = open('result.txt', 'w')
result_file.write(f'Your final score is {correct_answer_count}/{len(quizz)}.')
result_file.close()

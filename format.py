

team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print("В команде Мастера кода участников: %(team1_num)s ! " % {'team1_num': 5})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s" % {'team1_num': 5, 'team2_num': 6})
print('Команда Волшебники данных решила задач: {num} !'.format(num='42'))
print('Волшебники данных решили задачи за {team1_time} с !'.format(team1_time='18015.2'))


print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
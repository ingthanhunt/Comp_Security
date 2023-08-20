import hashlib
import pandas as pd
import time

substitution = { 'o' : '0', 'l' : '1', 'i' : '1'}
rainbow_table = [['word', 'hash_value']]
target = 'd54cc1fe76f5186380a0939d2fc1723c44e8a5f7'
timer = {'total_time': 0, 'count' : 0}

def substitute(word, i, n, tmp):
  if i == n:
    start_time = time.time()
    hash_value = hashlib.sha1(bytes(tmp, 'utf-8')).hexdigest()
    end_time = time.time()
    timer['total_time'] += end_time - start_time
    timer['count'] += 1
    rainbow_table.append([tmp, hash_value])
    if hash_value == target:
      print('Answer#1 -> original value is', tmp)
    return

  tmp_char = word[i]
  variation = []
  if tmp_char.isalpha():
    variation = [tmp_char.lower(), tmp_char.upper()]
    if tmp_char.lower() in substitution:
      variation.append(substitution[tmp_char.lower()])
  
  for case in variation:
    substitute(word, i+1, n, tmp + case)

start_time = time.time()
f = open('activity-1/10k-most-common.txt', 'r')
for word in f.read().split('\n'):
  substitute(word, 0, len(word), '')
df = pd.DataFrame(rainbow_table)
df.to_csv('activity-1/rainbow_table.csv', index=False)
end_time = time.time()
total_time = end_time - start_time
print('Answer#2 -> time for create a rainbow table :', total_time)
print('Answer#3 -> average time for perform hash on a password string :', timer['total_time'] / timer['count'])



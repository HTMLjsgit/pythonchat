with open('dictionaly.txt') as open_file:
  all_data = open_file.read()

line_list = all_data.splitlines()

bot_dict = {}

for line in line_list:
  orig,trans = line.split(':')
  bot_dict[orig] = trans

while True:
  command = input('メッセージを入力: ')

  responce = ""

  for key in bot_dict:
    if key in command:
      responce = bot_dict[key]
      print(responce)
      break
    # else:
    #   print('なんていいましたか')

if not responce:
  responce = "あなたとはなしがしたい"

print(responce)

# if 'さようなら' in command:
#   print("じゃあね！")
#   break

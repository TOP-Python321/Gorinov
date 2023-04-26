text = input('Введите текст: ')

out_text = ''

for i in range(len(text)):

    if text[i] == ' ':
        out_text += ''
        
    else:
        out_text += text[i]
        
total = len(out_text) * 30

print(f'{total // 100} руб. {total % 100} коп.')

# Введите текст: грузите апельсины бочках братья карамазовы      грузите апельсины бочках братья карамазовы

# 22 руб. 80 коп.

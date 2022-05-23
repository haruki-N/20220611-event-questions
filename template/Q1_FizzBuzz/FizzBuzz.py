for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 5 == 0 and num % 3 == 0:   # 15の倍数の場合
        string = 'FizzBuzz'
    elif num % 5 == 0:   # 5の倍数かつ3の倍数でない場合
        string = 'Buzz'
    elif num % 3 == 0:   # 3の倍数かつ5の倍数でない場合
        string = 'Fizz'
    else:
        string = str(num)
    # ここまで記述

    print(string)

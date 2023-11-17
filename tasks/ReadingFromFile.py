with open('demo.txt', mode='r') as account:
    print(f'{"Joy":<10}{"Joseph":<10}{"Peace":<10}{"Udeme":>10}')
    for record in account:
        Joy, Joseph, Peace, Udeme = record.split()
        print(f'{Joy:<10}{Joseph:<10}{Peace:<10}{Udeme:>10}')


with open('accounts.txt', mode='r') as accounts:
    print(f'{"Account":< 10}{"Name":< 10}{"Balance":>10}')
    for record in accounts:
        accounts, name, balance = record.split()
        print(f'{accounts:<10}{name:<10}{balance:>10}')

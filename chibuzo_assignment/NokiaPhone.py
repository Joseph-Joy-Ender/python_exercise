def main_menu():
    menu = """
     ============================
     Welcome to your nokia phone
     *****************************
     1 -> phoneBook
     2 -> messages
     3 -> chat
     4 -> callRegister
     5 -> tones
     6 -> settings
     7 -> callDivert
     8 -> games
     9 -> calculator
     10 -> reminders
     11 -> clock
     12 -> profiles
     13 -> simServices
     14 -> exit
    """
    print(menu)


def user_prompt():
    main_menu()
    userInput = int(input())
    match userInput:
        case 1:
            phone_book()
        case 2:
            messages()
        case 3:
            chat()
        case 4:
            call_register()
        case 5:
            tones()
        case 6:
            settings()
        case 7:
            call_divert()
        case 8:
            games()
        case 9:
            calculator()
        case 10:
            remainders()
        case 11:
            clock()
        case 12:
            profiles()
        case 13:
            sim_services()
        case 14:
            exit()


def menu_map():
    print("""
    ============================
     Welcome to your nokia phone
     *****************************
     1 -> phoneBook
     2 -> messages
     3 -> chat
     4 -> callRegister
     5 -> tones
     6 -> settings
     7 -> callDivert
     8 -> games
     9 -> calculator
     10 -> reminders
     11 -> clock
     12 -> profiles
     13 -> simServices
     14 -> exit
    """)


def phone_book():
    print("PhoneBook")
    print("""
    press
    1 -> Search
    2 -> Service Nos
    3 -> Add Name
    4 -> Erase
    5 -> Edit
    6 -> Assign Tone
    7 -> Send b'Card
    8 -> Options
    9 -> Speed dials
    10 -> Voice tags
    11 -> Back
    12 -> Exit
    """)
    phone = int(input())
    match phone:
        case 1:
            print("Search")
        case 2:
            print("Service nos")
        case 3:
            print("Add Name")
        case 4:
            print("Erase")
        case 5:
            print("Edit")
        case 6:
            print("Assign Tone")
        case 7:
            print("Send b'Card")
        case 8:
            options()
        case 9:
            print("Speed dials")
        case 10:
            print('Voice tags')
        case 11:
            user_prompt()
        case 12:
            end_program()


def options():
    print('Options')
    print(""" 
        1. Type of view
        2. Memory Status
        3. Back
        4. Exit
        """)
    option = int(input())
    match option:
        case 1:
            mobile("Type of view")
        case 2:
            mobile("Memory Status")
        case 3:
            phone_book()
        case 4:
            end_program()


def messages():
    mobile("Messages")
    mobile("""
    press
    1 -> Write Messages
    2 -> Inbox
    3 -> Outbox
    4 -> Picture Messages
    5 -> Templates
    6 -> Smileys
    7 -> message settings
    8 -> Info Service
    9 -> Voice MailBox Number
    10 -> Service Command Editor
    11 -> Back
    12 -> Exit
    """)
    message = int(input())
    match message:
        case 1:
            mobile("Write messages")
        case 2:
            mobile("Inbox")
        case 3:
            mobile("Outbox")
        case 4:
            mobile('picture messages')
        case 5:
            mobile("Templates")
        case 6:
            mobile('Smileys')
        case 7:
            message_settings()
        case 8:
            mobile('Info Service')
        case 9:
            mobile('Voice MailBox Number')
        case 10:
            mobile('Service Command Editor')
        case 11:
            user_prompt()
        case 12:
            end_program()


def message_settings():
    mobile("Message settings")
    mobile("""
    1. set 1
    2. common
    3. Back
    4. exit
    """)
    message_setting = int(input())
    match message_setting:
        case 1:
            set_1()
        case 2:
            common()
        case 3:
            messages()
        case 4:
            end_program()


def set_1():
    mobile("Set 1")
    mobile("""
    1. Message center number
    2. Message sent as
    3. Message validity
    4. Back
    5. exit
    """)
    set1 = int(input())
    match set1:
        case 1:
            mobile("Message center number")
        case 2:
            mobile('Message sent as')
        case 3:
            mobile('Message validity')
        case 4:
            message_settings()
        case 5:
            end_program()


def common():
    mobile("Common")
    mobile("""
    1. Delivery reports
    2. Reply via same center
    3. Character support
    4. Back
    5. exit
    """)
    common3 = int(input())
    match common3:
        case 1:
            mobile('Delivery reports')
        case 2:
            mobile('Reply via same center')
        case 3:
            mobile('Character support')
        case 4:
            message_settings()
        case 5:
            end_program()


def chat():
    mobile("Chat")


def call_register():
    mobile('Call register')
    mobile("""
    1. Missed calls
    2. Received calls
    3. Dialled numbers
    4. Erase recent call lists
    5. Show call duration
    6. Show call costs
    7. Call cost settings
    8. Prepaid credit
    9. Back
    """)
    callRegister = int(input())
    match callRegister:
        case 1:
            mobile('Missed calls')
        case 2:
            mobile('Received calls')
        case 3:
            mobile('Dialled numbers')
        case 4:
            mobile('Erase recent call lists')
        case 5:
            call_duration()
        case 6:
            call_cost()
        case 7:
            call_cost_setting()
        case 8:
            mobile("Prepaid credits")
        case 9:
            user_prompt()


def call_cost_setting():
    mobile('Call cost settings')
    mobile("""
    1: Call cost limit
    2: Show costs in
    3: back
    4: exit
    """)
    callCostSetting = int(input())
    match callCostSetting:
        case 1:
            mobile('Call cost limit')
        case 2:
            mobile('Show costs in')
        case 3:
            call_register()
        case 4:
            end_program()


def call_cost():
    mobile('Last call')
    mobile("""
    1: Call cost limit
    2: Show costs in
    3: back
    4: exit
    """)
    callCost = int(input())
    match callCost:
        case 1:
            mobile('Call cost limit')
        case 2:
            mobile('Show costs in')
        case 3:
            call_register()
        case 4:
            end_program()


def call_duration():
    mobile('Show call duration')
    mobile("""
    1: Last call duration
    2: All call's duration
    3: Received calls duration
    4: Dialled call's duration
    5: Clear timers
    6: Back
    7: exit
    """)
    callDuration = int(input())
    match callDuration:
        case 1:
            mobile('Last call duration')
        case 2:
            mobile("All call's duration")
        case 3:
            mobile('Received calls duration')
        case 4:
            mobile("Dialled call's duration")
        case 5:
            mobile('Clear timers')
        case 6:
            call_register()
        case 7:
            end_program()


def tones():
    mobile("Tones")
    mobile('''
    1. Ringing tone
    2. Ringing volume
    3. Incoming call divert
    4. Composer
    5. Message alert tone
    6. Keypad tones
    7. warning and game tones
    8. Vibrating alert
    9. Screen saver
    10. Back
    11. Exit
    ''')
    tone = int(input())
    match tone:
        case 1:
            mobile('Ringing tone')
        case 2:
            mobile('Ringing volume')
        case 3:
            mobile('Incoming call divert')
        case 4:
            mobile('Composer')
        case 5:
            mobile('Message alert tone')
        case 6:
            mobile('Keypad tones')
        case 7:
            mobile('warning and game tones')
        case 8:
            mobile('Vibrating alert')
        case 9:
            mobile('Screen saver')
        case 10:
            user_prompt()
        case 11:
            end_program()


def settings():
    mobile("Settings")
    mobile("""
    1 -> Call settings
    2 -> Phone settings
    3 -> Security settings
    4 -> Restore factory settings
    5 -> Back
    6 -> Exit
    """)
    setting = int(input())
    match setting:
        case 1:
            call_setting()
        case 2:
            phone_setting()
        case 3:
            security_settings()
        case 4:
            mobile('Restore factory setting')
        case 5:
            user_prompt()
        case 6:
            end_program()


def security_settings():
    mobile('Security settings')
    mobile("""
    1. PIN code request
    2. Call barring service
    3. Fixed dialling
    4. Closed user group
    5. phone security
    6. Change access codes
    7. Back
    8. Exit
    """)
    securitySettings = int(input())
    match securitySettings:
        case 1:
            mobile('PIN code request')
        case 2:
            mobile('Call barring service')
        case 3:
            mobile('Fixed dialling')
        case 4:
            mobile('Closed user group')
        case 5:
            mobile('phone security')
        case 6:
            mobile('Change access codes')
        case 7:
            settings()
        case 8:
            end_program()


def phone_setting():
    mobile("Phone setting")
    mobile("""
    1. Language
    2. Cell Info display
    3. Welcome note
    4. Network selection
    5. Lights
    6. Confirm SIM service actions
    7. Back
    8. Exit
    """)
    phoneSetting = int(input())
    match phoneSetting:
        case 1:
            mobile('Language')
        case 2:
            mobile('Cell Info display')
        case 3:
            mobile('Welcome note')
        case 4:
            mobile('Network selection')
        case 5:
            mobile('Lights')
        case 6:
            mobile('Confirm SIM service actions')
        case 7:
            settings()
        case 8:
            end_program()


def call_setting():
    mobile('Call setting')
    mobile("""
    1. Automatic redial
    2. Speed dialling
    3. Call waiting options
    4. Own number sending
    5. Phone line in use
    6. Automatic answer
    7. Back
    8. Exit
    """)
    callSetting = int(input())
    match callSetting:
        case 1:
            mobile('Automatic redial')
        case 2:
            mobile('Speed dialling')
        case 3:
            mobile('Call waiting options')
        case 4:
            mobile('Own number sending')
        case 5:
            mobile('Phone line in use')
        case 6:
            mobile('Automatic answer')
        case 7:
            settings()
        case 8:
            end_program()


def call_divert():
    mobile("Call divert")


def games():
    mobile("Games")


def calculator():
    mobile('Calculator')


def remainders():
    mobile('Remainders')


def clock():
    mobile("Clock")
    mobile("""
    1. Alarm clock
    2. Clock setting
    3. Date setting
    4. StopWatch
    5. Countdown timer
    6. Auto update of time and date 
    7. Back
    8. Exit
    """)
    clocks = int(input())
    match clocks:
        case 1:
            mobile("Alarm clock")
        case 2:
            mobile("Clock setting")
        case 3:
            mobile("Date setting")
        case 4:
            mobile("StopWatch")
        case 5:
            mobile("Countdown timer")
        case 6:
            mobile("Auto update of time and date")
        case 7:
            user_prompt()
        case 8:
            end_program()


def profiles():
    mobile("Profiles")


def sim_services():
    mobile("Sim services")


def end_program():
    mobile("Good Bye!")
    exit()


def mobile(prompt: str):
    print(prompt)


user_prompt()

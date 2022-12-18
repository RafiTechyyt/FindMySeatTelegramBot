
from telegram.ext import *

import keys

print('Starting up bot...')



def start_command(update, context):
    update.message.reply_text('Hello there! I\'m the Find My Seat Bot . Enter your register number to get your assigned seat details!')



def help_command(update, context):
    update.message.reply_text('Try typing your register number and i will respond to you with your seating details! Type /developer to contact the developer')



def developer_command(update, context):
    update.message.reply_text('Hello There! \n My name is Muhammed Rafi ! I\'m a Tech Enthusiast \n if you are facing any errors or have any questions feel free to contact me at rafitechyonline@gmail.com \n Instagram : https://instagram.com/rafi_techy \n LinkedIn : https://in.linkedin.com/in/muhammed-rafi-943529220 \n Git Hub : https://github.com/RafiTechyyt' )


def handle_response(text) -> str:
    

    if 'hello' in text:
        return 'Hey there!'

    if 'how are you' in text:
        return 'I\'m good!'

    if '20130745' in text:
        return 'Name : Muhammed Rafi \n Roll No : 39 \n Assigned Seat : CT-S5 - D2'

    if '20130755' in text:
        return 'Name : Vishnu N.K \n Roll No : 59 \n Assigned Seat : CT-S5 - A2'

    if '20130760' in text:
        return 'Name : Muhammed Razan \n Roll No : 40 \n Assigned Seat : CT-S3 - A1'

    return 'Please Double Check Your Register Number And Enter Again!'


def handle_message(update, context):
    
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    
    if message_type == 'group':
        
        if '@FindMySeatBot' in text:
            new_text = text.replace('@FindMySeatBot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    
    update.message.reply_text(response)



def error(update, context):
    print(f'Update {update} caused error {context.error}')



if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('developer', developer_command))


    dp.add_handler(MessageHandler(Filters.text, handle_message))


    dp.add_error_handler(error)


    updater.start_polling(1.0)
    updater.idle()

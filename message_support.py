from models import User, Messages
from clcrypto import check_password


def message_support_message_list(username, password):
    users = User.load_all_users()
    user = None
    for elem in users:
        if elem.username == username:
            user = elem
            break
    if not user:
        return "Wrong username"
    if not check_password(password, user.hashed_password):
        return "Wrong password"
    all_messages = Messages.load_all_messages()
    messages = """Your messages:\n"""
    for elem in all_messages:
        if elem.from_id == user.id or elem.to_id == user.id:
            messages += f"Message from: {elem.from_id}(user id) to {elem.to_id}(user id) Message content: '{elem.text}'" \
                        f" Date: {elem.creation_data}\n"
    return messages


def message_support_send_message(username, password, to, text):
    users = User.load_all_users()
    user = None
    receiver = None
    for elem in users:
        if elem.username == username:
            user = elem
            break
    if not user:
        return "Wrong username"
    if not check_password(password, user.hashed_password):
        return "Wrong password"
    for elem in users:
        if elem.username == to:
            receiver = elem
    if not receiver:
        return "Wrong receiver"
    if len(text) > 255:
        return "Text was too long"
    message = Messages(user.id, receiver.id, text)
    message.save_to_db()
    return "Message sent"


if __name__ == '__main__':

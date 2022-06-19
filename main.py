alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?!' "


def decoder(message, offset):
    translated_message = ""

    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message


def coder(message, offset):
    translated_message = ""

    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message


message_one = "jxu evviuj veh jxu iusedt cuiiqwu " \
              "yi vekhjuud."

print(decoder(message_one, 10))

message_two = "bqdradyuzs ygxfubxq omqemd " \
              "oubtqde fa oapq kagd yqeemsqe ue qhqz " \
              "yadq eqogdq!"

print(coder(message_one, 14))

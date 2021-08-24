from mycroft import MycroftSkill, intent_file_handler


class YoBro(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('bro.yo.intent')
    def handle_bro_yo(self, message):
        self.speak_dialog('bro.yo')


def create_skill():
    return YoBro()


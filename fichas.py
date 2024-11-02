import random

class Ficha:
    tematicas = {
        'animales': ["🐶", "🐱", "🐭", "🐹", "🐰", "🐸", "🐯", "🐨", "🐵", "🐔", "🐧", "🐦", "🐍", "🐢"],
        'frutas': ["🍎", "🍌", "🍇", "🍓", "🍍", "🍑", "🍉", "🍊", "🍒", "🍋", "🥭", "🥥", "🍈", "🍐"],
        'emojis': ["😀", "😎", "😭", "😡", "🤖", "👻", "🎃", "🌟", "🎉", "💖", "✨", "💯", "🔥", "💀"],
        'objetos': ["🚗", "🚲", "🛵", "🛴", "🚀", "🛳️", "🚁", "⛵", "⚽", "🏀", "🎮", "📱", "💻", "⌚"],
    }

    def __init__(self, tematica='animales'):
        self.tematica = self.tematicas.get(tematica, self.tematicas['animales'])
        self.fichas = self.generar_fichas()

    def generar_fichas(self):
        
        fichas = self.tematica * 2
        random.shuffle(fichas)
        return fichas


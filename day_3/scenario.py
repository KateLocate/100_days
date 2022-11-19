GREETING = 'Welcome to the Treasure Hunter Quest! \n' \
           'Only the bravest will overcome all the obstacles! \nGood luck, adventurer!'

SCENARIO = {
    '': {
        'text': 'You stopped in a small town, that you stumbled upon while travelling. \n'
                'You meet a man, who swears to you '
                'that he can tell you treasure whereabouts. \n'
                'He asks you to pay 3 coins for this information. Will you pay?',
        'left': 'Yes, I will!',
        'left_pos': '0',
        'right': 'No, I won`t...',
        'right_pos': '111',
    },
    '0': {
        'text': 'The man takes you to the road that will lead you to a tree with the hidden treasure and shows you '
                'the direction. Then he leaves.  \n'
                'After walking down the road for a while you see the fork at your path.\n'
                'You can see a lake shore in the distance to the left and thick woods to the right.\n'
                'Which way to go: left or right?',
        'left': 'I choose left!',
        'left_pos': '00',
        'right': 'I choose right!',
        'right_pos': '01',
    },
    '111': {
        'text': 'You leave the town and continue your journey, but not this quest!',
        'left': None,
        'left_pos': '10',
        'right': None,
        'right_pos': None,
    },
    '10': {
        'text': 'Game over!',
        'left': None,
        'left_pos': None,
        'right': None,
        'right_pos': None,
    },
    '11': {
        'text': 'The end',
        'left': None,
        'left_pos': None,
        'right': None,
        'right_pos': None,
    },
    '00': {
        'text': 'You walk the path to the lake shore and enjoy the weather and fresh water. \nYou can see a boat, '
                'sailing in your direction. \nAn old man asks you to do him a small favour and he`ll give you'
                ' a ride in return. Do you agree?',
        'left': 'Yes, I will help.',
        'left_pos': '000',
        'right': 'I`ll go my own way.',
        'right_pos': '001',
    },
    '000': {
        'text': 'You get on the boat and the man asks you to help him draw two nets from the water. \n'
                'You manage doing this, and you sail along the shore. \nAs the boat begins to shake and'
                ' the water fills it from the inside, you start drowning \n. You now have a choice:'
                ' save an old man or grab your belongings and try to rescue. \nWhat will you choose?',
        'left': 'No time for doubts, I`ll save him!',
        'left_pos': '0001',
        'right': 'I cannot just leave all my possessions this way...',
        'right_pos': '0000',
    },
    '01': {
        'text': 'You start making the way through the forest, following the narrow trail. \nSome time later'
                ' you get stuck and suddenly see a dog, friendly barking and trying to get your attention. \n'
                'You feel like it wants to show you the way, will you follow?.',
        'left': 'Yes, it seems friendly, why not.',
        'left_pos': '010',
        'right': 'It is a distraction, I won`t go.',
        'right_pos': '0.1.1',
    },
    '0000': {
        'text': 'You both drown, and it is the end of your story...',
        'left': None,
        'left_pos': '10',
        'right': None,
        'right_pos': None,
    },
    '0001': {
        'text': 'You both survive! You saved a man and got to the shore all wet and tired. \n'
                'The old man is grateful and tells you where to go, to find the grove where the tree might be. \n'
                'You find the grove easily and enter it.',
        'left': None,
        'left_pos': '0010',
        'right': None,
        'right_pos': None,
    },
    '001': {
        'text': 'Walking along the shore for quite a long time, you find a road leading to a grove, \nand you think '
                'it`s a good idea to look for a tree in the forest, so you enter it.',
        'left': None,
        'left_pos': '0010',
        'right': None,
        'right_pos': None,
    },
    '0010': {
        'text': 'Not far from here you can hear the gentle music and quiet laughter. \n'
                'Will you go and find out what is happening there?',
        'left': 'Maybe they`ll guide me? I`ll check.',
        'left_pos': '00101',
        'right': 'No, I should not be distracted.',
        'right_pos': '00100',
    },
    '00100': {
        'text': 'You go on searching and finally see golden light, enveloping the crown of the tree in the distance. \n'
                'You come closer and see the hollow in it, where the treasure lies. \n'
                'There are a lot of coins there and a ring with a blue stone, that might be magical!',
        'left': 'Congratulations, you got your reward and finished this quest! See ya, adventurer!',
        'left_pos': '11',
        'right': None,
        'right_pos': None,
    },
    '010': {
        'text': 'You follow the dog and it leads you to the grove, where you might find the tree!',
        'left': None,
        'left_pos': '0010',
        'right': None,
        'right_pos': None,
    },
    '011': {
        'text': 'You ignore the dog and go on searching the way. \nThere is an opening in the trees wall '
                'and violet light pouring through, will you go that way?',
        'left': 'No, this may be dangerous, what if it is a trap?',
        'left_pos': '0111',
        'right': 'Yes, I don`t think it is suspicious.',
        'right_pos': '0110',
    },
    '0111': {
        'text': 'You go deeper and deeper into the forest. \n'
                'You got lost and never came back, nobody knows what has happened to you.',
        'left': None,
        'left_pos': '10',
        'right': None,
        'right_pos': None,
    },
    '0110': {
        'text': 'You come closer, violet light goes off, and you see the grove, where the tree might be.',
        'left': None,
        'left_pos': '0010',
        'right': None,
        'right_pos': None,
    },
    '00101': {
        'text': 'When you come to a source of music and laughter, you see the enchanted harp, \n'
                'playing songs and sounding different voices. There is a chest nearby, will you open it?',
        'left': 'Maybe there is loot? I`ll open it.',
        'left_pos': '001010',
        'right': 'No, I won`t.',
        'right_pos': '001011',
    },
    '001010': {
        'text': 'You try opening the chest, but suddenly something tong-like comes out of it and grabs you. \n'
                'You are a mimic`s prey. Sorry, the quest ends here...',
        'left': None,
        'left_pos': '10',
        'right': None,
        'right_pos': None,
    },
    '001011': {
        'text': 'You sit in front of a harp and enjoy the enveloping song, it clouds your mind and feels so good. \n'
                'You have nothing to worry about anymore, you go back to the town and forget about the tree treasure.',
        'left': None,
        'left_pos': '10',
        'right': None,
        'right_pos': None,
    },
}

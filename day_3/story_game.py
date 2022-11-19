from scenario import GREETING, SCENARIO


class Node:
    def __init__(self, position, left_pos, left, right_pos, right, text):
        self.position = position
        self.left_event = left_pos
        self.left = left
        self.right_event = right_pos
        self.right = right
        self.text = text


class Story:
    def __init__(self, story_dict: dict, greeting: str = ''):
        self.story_dict = story_dict
        self.greeting = greeting
        self.story = {}

    def make_story(self):
        for position, details in self.story_dict.items():
            node = Node(
                position=position,
                left_pos=details['left_pos'],
                left=details['left'],
                right_pos=details['right_pos'],
                right=details['right'],
                text=details['text'],
            )
            self.story[position] = node
        event_codes = self.story.keys()
        for event_code, event in self.story.items():
            if event.left_event in event_codes:
                event.left_event = self.story[event.left_event]
            if event.right_event in event_codes:
                event.right_event = self.story[event.right_event]

    @staticmethod
    def infinite_query(phrase, valid_answer):
        answer = None
        while answer not in valid_answer:
            answer = input(phrase)
        return answer

    def play(self):
        start_event = self.story.get('')
        current_event = start_event
        while current_event.left_event or current_event.right_event:
            print(current_event.text)
            left = current_event.left
            right = current_event.right
            if right and left:
                print(f'1:{current_event.left} \n2:{current_event.right}')
                choice_phrase = 'Enter 1 or 2:'
                choice = self.infinite_query(choice_phrase, ['1', '2'])
                if choice == '1':
                    current_event = current_event.left_event
                elif choice == '2':
                    current_event = current_event.right_event
            elif current_event.right_event and current_event.left_event:
                print('See some fat bugs here...')
            elif current_event.right_event or current_event.left_event:
                current_event = current_event.right_event or current_event.left_event
        else:
            print(current_event.text)

    def start_game(self):
        print(self.greeting)
        self.play()


story = Story(SCENARIO, GREETING)
story.make_story()
story.start_game()

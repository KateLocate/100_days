from typing import Callable

import ascii_art as art
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
    """Class for text quests realization using structured story scenario."""

    def __init__(self, story_dict: dict, greeting: str = ''):
        """
        The __init__ method requires a `story_dict` dict object e.g:
        { 'event_code': {
            'text': 'The end',
            'left': None,
            'left_pos': None,
            'right': None,
            'right_pos': None,
            },
        }
        Restrictions:
            - the story scenario is a constant value `SCENARIO` from `scenario.py`
            - `event_code` == '' is a start of a story
            - `event_code` is a string or a number with unique value
            - the keys `text`, `left`, `left_pos`, `right`, `right_pos` must not be renamed
            - the values of the keys `left`, `left_pos`, `right`, `right_pos` may be None, number or string
            - `ascii_art.py` must contain constant values: `START_AND_STOP`, `TOP_BORDER`, `BOTTOM_BORDER`, `START_ART`
        """
        self.story_dict = story_dict
        self.greeting = greeting
        self.story = {}

        self.make_story()
        self.start_game()

    def make_story(self):
        left_and_right_positions = {''}
        for position, details in self.story_dict.items():
            left_and_right_positions.update([details['left_pos'], details['right_pos']])
            node = Node(
                position=position,
                left_pos=details['left_pos'],
                left=details['left'],
                right_pos=details['right_pos'],
                right=details['right'],
                text=details['text'],
            )
            self.story[position] = node
        story_event_keys = set(self.story.keys())
        story_event_keys.add(None)
        if story_event_keys != left_and_right_positions:
            raise Exception(
                f'Some events are not present in the scenario: '
                f'{left_and_right_positions.difference(set(story_event_keys))}.'
            )
        for event_code, event in self.story.items():
            if event.left_event:
                event.left_event = self.story[event.left_event]
            if event.right_event:
                event.right_event = self.story[event.right_event]

    @staticmethod
    def infinite_query(phrase: str, valid_answers: tuple):
        answer = None
        while answer not in valid_answers:
            answer = input(phrase)
        return answer

    @staticmethod
    def get_fixed_length_string(string: str, max_length: int) -> str:
        new_string = ''
        if len(string) > max_length:
            space = ' '
            list_from_string = string.split(space)
            current_max_length = max_length
            for word in list_from_string:
                string_part = word + space
                if len(new_string) + len(string_part) < current_max_length:
                    new_string += string_part
                else:
                    new_string += '\n' + string_part
                    current_max_length += max_length
            new_string.rstrip(space)
        return new_string if new_string else string

    def text_with_borders_printing(self, top_border: str = art.TOP_BORDER, bottom_border: str = art.BOTTOM_BORDER,
                                   text: str = '', action: Callable = None, action_args: tuple = ()):
        result = None
        brd_length = len(top_border.split('\n')[0])
        print(top_border)
        if text:
            text_processed = self.get_fixed_length_string(text, max_length=brd_length)
            print(text_processed)
        if action:
            result = action(*action_args)
        print(bottom_border)
        return result

    def play(self):
        start_event = self.story.get('')
        current_event = start_event

        left, right = '1', '2'
        choices = [left, right]
        choice_phrase = f'Enter {left} or {right}:'

        while current_event.left_event or current_event.right_event:
            self.text_with_borders_printing(text=current_event.text)

            left_text, left_event = current_event.left, current_event.left_event
            right_text, right_event = current_event.right, current_event.right_event

            if right_text and left_text:
                print(f'{left}:{current_event.left} \n{right}:{current_event.right}')
                choice = self.text_with_borders_printing(
                    action=self.infinite_query, action_args=(choice_phrase, choices)
                )
                current_event = left_event if choice == left else right_event
            elif right_event and left_event:
                print('See some bugs here, some fat ones...')
            elif right_event or left_event:
                current_event = right_event or left_event
        else:
            print(current_event.text)

    def start_game(self):
        print(art.START_ART)
        self.text_with_borders_printing(art.START_AND_STOP, art.START_AND_STOP, self.greeting)
        self.play()


if __name__ == '__main__':
    game = Story(SCENARIO, GREETING)

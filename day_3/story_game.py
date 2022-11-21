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

    def text_with_borders_printing(self, top_border: str, bottom_border: str,
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

        while current_event.left_event or current_event.right_event:
            self.text_with_borders_printing(art.TOP_BORDER, art.BOTTOM_BORDER, text=current_event.text)

            left, left_text, left_event = '1', current_event.left, current_event.left_event
            right, right_text, right_event = '2', current_event.right, current_event.right_event

            if right_text and left_text:
                print(f'{left}:{current_event.left} \n{right}:{current_event.right}')
                choice_phrase = f'Enter {left} or {right}:'
                choices = [left, right]
                choice = self.text_with_borders_printing(
                    art.TOP_BORDER, art.BOTTOM_BORDER, action=self.infinite_query, action_args=(choice_phrase, choices)
                )
                if choice == left:
                    current_event = left_event
                elif choice == right:
                    current_event = right_event
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


story = Story(SCENARIO, GREETING)
story.make_story()
story.start_game()

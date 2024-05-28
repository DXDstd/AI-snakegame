from snake import GameOutcome
from ai_base import SystemState, AI_Base

class AI_Player(AI_Base):
    def __init__(self):
        self._name = "Human Player"
        self._state: SystemState = None

    def is_keyboard_allowed(self) -> bool:
        return True 

    def callback_take_action(self, state:SystemState) -> (int,int):
        return (state.dir_x,state.dir_y)

    def callback_action_outcome(self, state:SystemState, outcome:GameOutcome):
        pass # do nothing by default, ignore the outcome

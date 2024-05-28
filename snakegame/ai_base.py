from abc import ABC, abstractmethod
from snake import GameOutcome

class SystemState:
    
    def __init__(self):
        ## mark the position of the food relative to the snake
        self.food_north: bool = False
        self.food_south: bool = False
        self.food_east: bool = False
        self.food_west: bool = False
        ## mark the obstable one-ring around the snake
        self.obj_north: int = 0
        self.obj_south: int = 0
        self.obj_east: int = 0
        self.obj_west: int = 0
        self.obj_north_east: int = 0
        self.obj_north_west: int = 0
        self.obj_south_east: int = 0
        self.obj_south_west: int = 0
        ## record the current movement of the snake
        self.dir_x: int = 0
        self.dir_y: int = 0


class DecayingFloat:
    def __init__(self, value:float, factor:float=None, minval:float=None,
                 mode:str="exp"):
        self.init = value
        self.value = value
        self.factor = factor
        self.minval = minval
        self.mode = mode

    def __float__(self) -> float:
        return float(self.value)

    def reset(self):
        self.value = self.init

    def decay(self):
        if self.factor==None: return

        if self.mode=="exp":      self.value *= self.factor
        elif self.mode=="linear": self.value -= self.factor
        
        if self.minval==None: 
            return
        elif self.value<self.minval:
            self.value = self.minval


class AI_Base(ABC):

    def __init__(self):
        self._name = "Human Player"
        self._state: SystemState = None

    def get_name(self) -> str:
        return self._name

    def state_str(self, state:SystemState) -> str:
        return "["+(">" if state.food_east else " ") \
                  +("v" if state.food_south else " ") \
                  +("<" if state.food_west else " ") \
                  +("^" if state.food_north else " ") + "]," \
                  + "[%+d,%+d,%+d,%d]"% \
                      (state.obj_north,state.obj_south,state.obj_east,state.obj_west) \
                  + "-%s"%("U" if state.dir_y==-1 else "D" if state.dir_y==1 else \
                           "L" if state.dir_x==-1 else "R")

    def is_keyboard_allowed(self) -> bool:
        return False

    ## callback when a request for action is needed by the environment
    @abstractmethod
    def callback_take_action(self, state:SystemState) -> (int,int):
        ## if called accidentally, it simply returns the same 
        ## movement as the previous state
        return (state.dir_x,state.dir_y) 

    ## callback when the outcome for the last action is available
    @abstractmethod
    def callback_action_outcome(self, state:SystemState, outcome:GameOutcome):
        pass 

    def callback_terminating(self):

        pass # do nothing by default


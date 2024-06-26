from snake import GameOutcome
from ai_base import SystemState, AI_Base

class AI_RuleBased(AI_Base): 
    def __init__(self):
        super().__init__()
        self._name = "Rule-based algorithm"

    def callback_take_action(self, state:SystemState) -> (int,int):
        BLOCKED = -1 # define constants here for better code readability
        EAST = (+1,0); WEST = (-1,0)
        NORTH = (0,-1); SOUTH = (0,+1)
        movement = (state.dir_x,state.dir_y)

        if state.food_north and state.obj_north is not BLOCKED:   movement = NORTH 
        elif state.food_south and state.obj_south is not BLOCKED: movement = SOUTH 
        elif state.food_east and state.obj_east is not BLOCKED:   movement = EAST 
        elif state.food_west and state.obj_west is not BLOCKED:   movement = WEST
        else: # the following is where the snake can't move towards
              # the food & has to go around
            if state.dir_x!=0: # for east/west movement
                if state.obj_north is not BLOCKED:    movement = NORTH 
                elif state.obj_south is not BLOCKED:  movement = SOUTH 
            elif state.dir_y!=0: # for north/south movement
                if state.obj_east is not BLOCKED:     movement = EAST 
                elif state.obj_west is not BLOCKED:   movement = WEST 
            else: pass # by passing, the snake will continue its current movement
        return movement

    def callback_action_outcome(self, state:SystemState, outcome:GameOutcome):
        pass

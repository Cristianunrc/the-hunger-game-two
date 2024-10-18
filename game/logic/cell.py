from enum import Enum
from marshmallow import Schema, fields


class State(Enum):
    FREE = 1
    ITEM = 2
    TRIBUTE = 3

FREE = State.FREE
ITEM = State.ITEM
TRIBUTE = State.TRIBUTE


class Cell:
    def __init__(self):
        self.state = FREE
        self.item = None
        self.tribute = None
        self.pos = None

    # Return the position of the cell
    def get_pos(self):
        return self.pos

    # Get the state of the cell
    def get_state(self):
        return self.state

    # Get item of a cell
    def get_item(self):
        if self.item is None:
            raise ValueError(f"No item in this position")
        return self.item
    
    # Get tribute of a cell
    def get_tribute(self):
        if self.tribute is None:
            raise ValueError(f"No tribute in this position")
        return self.tribute

    def __str__(self):
        if self.state == FREE:
            return "  "
        if self.state == ITEM:
            return self.item.__str__()
        if self.state == TRIBUTE:
            return self.tribute.__str__()

    def __eq__(self, other):
        return isinstance(other, Cell)

    # Put a tribute in a cell
    def put_tribute(self, tribute):
        if self.state == TRIBUTE:
            raise ValueError(f"Trying to place one Tribute on top of another")
        self.state = TRIBUTE
        self.tribute = tribute

    # Remove a tribute in a cell
    def remove_tribute(self):
        if self.get_state() == ITEM or self.get_state() == FREE:
            raise ValueError(f"Trying to remove one Item or the cell is FREE")
        self.tribute.past_pos = self.tribute.pos
        self.state = FREE
        self.tribute = None

    # Put a item in a cell
    def put_item(self, item):
        if self.state != FREE:
            raise ValueError(
                f"Trying to place one Item on top of another or over an Tribute"
            )
        self.state = ITEM
        self.item = item

    # Remove a item in a cell
    def remove_item(self):
        if self.item is None:
            raise ValueError(f"Trying to remove an item where there isn't one")
        if self.tribute is None:
            self.state = FREE
        self.item = None


class CellSchema(Schema):
    state = fields.Str()
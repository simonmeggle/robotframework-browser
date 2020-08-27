from enum import Enum, auto

from typing_extensions import TypedDict

BoundingBox = TypedDict(
    "BoundingBox",
    {"x": float, "y": float, "width": float, "height": float},
    total=False,
)

Coordinates = TypedDict("Coordinates", {"x": float, "y": float}, total=False)

MouseOptionsDict = TypedDict(
    "MouseOptionsDict", {"x": float, "y": float, "options": dict}, total=False
)

ViewportDimensions = TypedDict("ViewportDimensions", {"width": int, "height": int})


class DialogAction(Enum):
    accept = auto()
    dismiss = auto()


class FutureDialogAction(Enum):
    accept = auto()
    dismiss = auto()
    ignore = auto()


class DialogField(Enum):
    type = auto()
    message = auto()


class CookieType(Enum):
    dictionary = auto()
    dict = dictionary
    string = auto()
    str = string


class RequestMethod(Enum):
    HEAD = auto()
    GET = auto()
    POST = auto()
    PUT = auto()
    PATCH = auto()
    DELETE = auto()


class MouseButtonAction(Enum):
    click = auto()
    down = auto()
    up = auto()


class MouseButton(Enum):
    left = auto()
    middle = auto()
    right = auto()


class KeyAction(Enum):
    down = auto()
    up = auto()
    press = auto()


class KeyboardInputAction(Enum):
    insertText = auto()
    type = auto()


class KeyboardModifier(Enum):
    Alt = auto()
    Control = auto()
    Meta = auto()
    Shift = auto()


class SelectAttribute(Enum):
    value = auto()
    label = auto()
    text = label
    index = auto()


class SupportedBrowsers(Enum):
    chromium = auto()
    firefox = auto()
    webkit = auto()


ColorScheme = Enum("ColorScheme", ["dark", "light", "no-preference"])


class ViewportFields(Enum):
    width = auto()
    height = auto()
    ALL = auto()


class BoundingBoxFields(Enum):
    width = auto()
    height = auto()
    x = auto()
    y = auto()
    ALL = auto()


class AutoClosingLevel(Enum):
    SUITE = auto()
    TEST = auto()
    MANUAL = auto()


class ElementState(Enum):
    attached = auto()
    detached = auto()
    visible = auto()
    hidden = auto()
    enabled = auto()
    disabled = auto()
    editable = auto()
    readonly = auto()
    selected = auto()
    deselected = auto()
    focused = auto()
    defocused = auto()
    checked = auto()
    unchecked = auto()


AssertionOperator = Enum(
    "AssertionOperator",
    {
        "equal": "==",
        "==": "==",
        "should be": "==",
        "inequal": "!=",
        "!=": "!=",
        "should not be": "!=",
        "less than": "<",
        "<": "<",
        "greater than": ">",
        ">": ">",
        "<=": "<=",
        ">=": ">=",
        "contains": "*=",
        "*=": "*=",
        "starts": "^=",
        "^=": "^=",
        "should start with": "^=",
        "ends": "$=",
        "should end with": "$=",
        "$=": "$=",
        "matches": "$",
        "validate": "validate",
        "then": "then",
        "evaluate": "then",
    },
)

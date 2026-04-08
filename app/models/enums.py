import enum


class TaskStatus(str, enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskPriority(str, enum):
    low = "low"
    medium = "medium"
    high = "high"

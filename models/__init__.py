from extensions import db

from .interest import interest
from .user import User
from .project import Project
from .comment import Comment

__all__ = ['User', 'Project', 'interest', 'Comment']


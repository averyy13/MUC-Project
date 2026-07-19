"""SQLAlchemy declarative base and model imports."""
import re
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    """
    Universal base class for all SQLAlchemy models in the application.
    Handles automatic tablename generation and base configuration.
    """
    
    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Automatically converts Python model class names to snake_case table names.
        Example: 'FirstAidStep' becomes 'first_aid_step'.
        If a table handles plurals differently (e.g., 'first_aid_steps'), 
        you can still override it manually inside that specific model.
        """
        # Inserts an underscore before any capital letter followed by a lowercase one,
        # then converts everything to lowercase.
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()
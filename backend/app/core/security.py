"""Security utilities (hashing, tokens, etc.)."""

from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings


# Password hashing configuration
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# ==========================
# Password Functions
# ==========================

def hash_password(password: str) -> str:
    """
    Convert plain password into bcrypt hash.
    """

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Compare user entered password
    with stored bcrypt hash.
    """

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# ==========================
# JWT Functions
# ==========================

def create_access_token(
    data: dict,
    expires_minutes: int | None = None
):
    """
    Generate JWT token.
    """

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=(
            expires_minutes
            or settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    to_encode.update(
        {
            "exp": expire
        }
    )

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt



def decode_access_token(token: str):
    """
    Decode and verify JWT token.
    """

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        return payload

    except JWTError:

        return None
"""
Supabase Authentication utilities

Handles both:
1. Supabase Auth JWT verification
2. Custom JWT for additional flexibility
"""

import os
from typing import Optional
import jwt
from dotenv import load_dotenv

load_dotenv()

# Supabase JWT settings
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")
ALGORITHM = "HS256"


def decode_supabase_token(token: str) -> Optional[dict]:
    """
    Decode and verify a Supabase access token.
    Returns the payload if valid, None otherwise.
    """
    try:
        # Supabase tokens use HS256 with the JWT secret
        payload = jwt.decode(
            token,
            SUPABASE_JWT_SECRET,
            algorithms=[ALGORITHM],
            audience="authenticated"
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def get_user_id_from_token(token: str) -> Optional[str]:
    """Extract user ID from Supabase token"""
    payload = decode_supabase_token(token)
    if payload:
        return payload.get("sub")  # Supabase uses 'sub' for user ID
    return None


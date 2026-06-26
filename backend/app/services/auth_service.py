from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate, UserLogin
from app.repositories.user_repository import UserRepository
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        user_data: UserCreate
    ):
        """
        Register a new user.
        """

        existing_user = UserRepository.get_user_by_email(
            db,
            user_data.email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered."
            )

        hashed_pwd = hash_password(user_data.password)

        new_user = UserRepository.create_user(
            db=db,
            full_name=user_data.full_name,
            email=user_data.email,
            hashed_password=hashed_pwd
        )

        return new_user

    @staticmethod
    def login_user(
        db: Session,
        login_data: UserLogin
    ):
        """
        Authenticate user and generate JWT token.
        """

        user = UserRepository.get_user_by_email(
            db,
            login_data.email
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )

        if not verify_password(
            login_data.password,
            user.hashed_password
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )

        token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }
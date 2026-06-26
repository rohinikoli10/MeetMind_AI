from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        """
        Retrieve a user by email.
        """
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        """
        Retrieve a user by ID.
        """
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def create_user(
        db: Session,
        full_name: str,
        email: str,
        hashed_password: str
    ):
        """
        Create and save a new user.
        """

        new_user = User(
            full_name=full_name,
            email=email,
            hashed_password=hashed_password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
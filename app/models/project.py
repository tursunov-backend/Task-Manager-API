# from datetime import datetime
# from typing import List

# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import String, ForeignKey, DateTime, Text

# from app.database import Base


# class Project(Base):
#     __tablename__ = "projects"

#     id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
#     title: Mapped[str] = mapped_column(String(255), nullable=False)
#     description: Mapped[str] = mapped_column(Text, nullable=True)
#     author_id: Mapped[int] = mapped_column(
#         ForeignKey("users.id", ondelete="CASCADE"), nullable=False
#     )
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

#     users: Mapped[List["User"]] = relationship(
#         "User", uselist=True, back_populates="projects"
#     )

#     def __str__(self):
#         return f"{self.id}. {self.title}"

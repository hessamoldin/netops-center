from app.db.database import Base
from app.db.database import engine

from app.models.site import Site

Base.metadata.create_all(bind=engine)

print("Tables created.")

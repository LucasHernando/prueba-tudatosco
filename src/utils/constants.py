import os

class Settings:
    """ @author: Lucas Hernando Bonilla,
        @version: v1 2025-04-09
        @Functionality: These are the application configuration variables """
    
    HOST = os.getenv("HOST_IP")
    PORT:int = int(os.getenv("PORT_HOST", 8080))
    DEBUG:bool = bool(os.getenv("DEBUG", False))
    JW_SECRET = os.getenv("JWT_SECRET_KEY")
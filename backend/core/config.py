import os
from dotenv import load_dotenv

# Inicia o carregamento das variáveis de ambiente
load_dotenv()


class Database_Settings:
    # Banco de dados postgresql para ENV
    DB_HOST: str = os.getenv("DB_HOST", "")
    DB_PORT: str = os.getenv("DB_PORT", "")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "")

    # Banco de dados sqlite para TEST
    DB_TEST: str = os.getenv("DB_TEST", "")

    # Segurança
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    ALGORITHM: str = os.getenv("ALGORITHM", "")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES", 60))

    # Ambiente
    ENV = os.getenv("ENV", "TEST")

    @property
    def sqlalchemy_url(self) -> str:

        if self.ENV == "TEST":
            return f"sqlite:///{self.DB_TEST}"
        # Retorna a URL para a conexao do postgresSQL SQLAlchemy
        return (
            f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    # @property
    # def config_security(self) -> dict:
    #     return {
    #         "Secret Key": self.SECRET_KEY,
    #         "Algorithm": self.ALGORITHM,
    #         "Token Minutes": self.ACCESS_TOKEN_EXPIRE_MINUTES
    #     }


DB_settings = Database_Settings()

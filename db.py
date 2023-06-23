from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Creamos el motor que permite manejar la conexión con la base de datos y el dialecto
# El tipo de base de datos que se utiliza, en este caso sqlite
# El segundo argumento es para evitar posibles errrones en caso de que la base de datos ejecute varias
# acciones simultáneas y genere varios hilos de ejecución. Es imprescindible ponerlo para evitar errores o warnings.
engine = create_engine('sqlite:///database/tareas.db', connect_args={'check_same_thread': False})

# Creamos la sesión como una transacción, es decir, un conjunto de operaciones de base de datos que, o seejecutan
# todas de forma atómica o no se ejecuta ninguna.
Session = sessionmaker(bind=engine)
session = Session()

# Vinculamos este modelo de BD con nuestra clase
Base = declarative_base()

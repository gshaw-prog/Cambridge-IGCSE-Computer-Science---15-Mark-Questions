from abc import ABC, abstractmethod

# ==========================================
# PART 1: ABSTRACTION (Abstract Class)
# ==========================================
class Device(ABC):
    def __init__(self, name):
        self.name = name
        self._is_on = False  # Encapsulation: Protected attribute

    @abstractmethod
    def perform_action(self):
        """Abstract method: Subclasses MUST implement this."""
        pass

    def toggle(self):
        """Concrete method: Inherited by all."""
        self._is_on = not self._is_on
        state = "ON" if self._is_on else "OFF"
        print(f"{self.name} is now {state}")

# ==========================================
# PART 2: RELATIONSHIPS (Composition)
# ==========================================
class Engine:
    def start(self):
        return "Engine vrooms!"

class Car:
    def __init__(self, model):
        self.model = model
        # COMPOSITION: Engine is created inside Car. 
        # If Car is deleted, Engine is deleted.
        self.engine = Engine() 

    def drive(self):
        print(f"{self.model}: {self.engine.start()}")

# ==========================================
# PART 3: DESIGN PATTERNS (Singleton)
# ==========================================
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Connecting to Database...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

# ==========================================
# PART 3: DESIGN PATTERNS (Factory)
# ==========================================
class SmartLight(Device):
    def perform_action(self):
        return "Adjusting brightness to 75%."

class SmartLock(Device):
    def perform_action(self):
        return "Securing deadbolt."

class DeviceFactory:
    @staticmethod
    def create_device(device_type, name):
        if device_type == "light":
            return SmartLight(name)
        elif device_type == "lock":
            return SmartLock(name)
        return None

# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    print("--- Singleton Demo ---")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Are they the same instance? {db1 is db2}")

    print("\n--- Factory & Abstraction Demo ---")
    factory = DeviceFactory()
    my_light = factory.create_device("light", "Living Room Light")
    my_light.toggle()
    print(my_light.perform_action())

    print("\n--- Composition Demo ---")
    my_car = Car("Tesla Model S")
    my_car.drive()
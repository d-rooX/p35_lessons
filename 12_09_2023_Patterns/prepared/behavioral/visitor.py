from abc import ABC, abstractmethod


# Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visit_life_insurance(self, policy):
        pass

    @abstractmethod
    def visit_auto_insurance(self, policy):
        pass

    @abstractmethod
    def visit_home_insurance(self, policy):
        pass


# Concrete Visitor: PremiumCalculator
class PremiumCalculator(Visitor):
    def __init__(self):
        self.total_annual_premium = 0  # Инициализируем общую годовую премию

    def visit_life_insurance(self, policy):
        policy.annual_premium = policy.age * 10
        self.total_annual_premium += policy.annual_premium  # Накапливаем премию

    def visit_auto_insurance(self, policy):
        policy.annual_premium = policy.car_value * 0.05
        self.total_annual_premium += policy.annual_premium  # Накапливаем премию

    def visit_home_insurance(self, policy):
        policy.annual_premium = policy.property_value * 0.02
        self.total_annual_premium += policy.annual_premium  # Накапливаем премию


# Element interface
class Policy(ABC):
    def accept(self, visitor):
        pass


# Concrete Elements: LifeInsurancePolicy, AutoInsurancePolicy, HomeInsurancePolicy
class LifeInsurancePolicy(Policy):
    def __init__(self, age):
        self.age = age

    def accept(self, visitor):
        visitor.visit_life_insurance(self)


class AutoInsurancePolicy(Policy):
    def __init__(self, car_value):
        self.car_value = car_value

    def accept(self, visitor):
        visitor.visit_auto_insurance(self)


class HomeInsurancePolicy(Policy):
    def __init__(self, property_value):
        self.property_value = property_value

    def accept(self, visitor):
        visitor.visit_home_insurance(self)


# Client code
if __name__ == "__main__":
    policies = [
        LifeInsurancePolicy(age=30),
        AutoInsurancePolicy(car_value=25000),
        HomeInsurancePolicy(property_value=150000),
    ]

    premium_calculator = PremiumCalculator()

    for policy in policies:
        policy.accept(premium_calculator)

    print(f"Общая годовая премия: ${premium_calculator.total_annual_premium:.2f}")

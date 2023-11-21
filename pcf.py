from typing import Final


class EnvironmentalImpact:
    """
    Represents a generic environmental impact with common attributes.

    Attributes:
        name: str
            The name of the environmental impact category.
        unit: str
            The unit of measurement for the environmental impact.
        description: str
            A brief description of the environmental impact.
    """

    def __init__(self, name: str, unit: str, description: str) -> None:
        self.name: Final = name
        self.unit: Final = unit
        self.description: Final = description

    def __str__(self) -> str:
        """Returns a string representation of the environmental impact."""
        return f"{self.name} ({self.unit}): {self.description}"


class ClimateChange(EnvironmentalImpact):
    """
    Represents the Climate Change impact category.
    """

    def __init__(self) -> None:
        super().__init__(
            name="Climate Change",
            unit="kg CO2-eq",
            description="Impact on global warming and climate change",
        )


class Acidification(EnvironmentalImpact):
    """
    Represents the Acidification impact category.
    """

    def __init__(self) -> None:
        super().__init__(
            name="Acidification",
            unit="kg SO2-eq",
            description="Impact on acidification of soil and water",
        )


# Define further subclasses for all 15 EN15804 Environmental Impact Categories

# Example usage
climate_change = ClimateChange()
print(climate_change)
# Output: Climate Change (kg CO2-eq): Impact on global warming and climate change

acidification = Acidification()
print(acidification.unit)
# Output: kg SO2-eq
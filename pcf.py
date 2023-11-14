class EnvironmentalImpactCategory:
    """
    Represents an environmental impact category.


    Attributes:
        category: str
            The name of the environmental impact category.
        unit: str
            The unit of measurement for the environmental impact category.
        description: str
            A brief description of the environmental impact category.
    """

    def __init__(self, *, category: str, unit: str, description: str):
        """
        Initializes an EnvironmentalImpactCategory instance.

        Args:
            category: str
                The name of the environmental impact category.
            unit: str
                The unit of measurement for the environmental impact category.
            description: str
                A brief description of the environmental impact category.
        """
        self.category: str = category
        self.unit: str = unit
        self.description: str = description

    def __str__(self) -> str:
        """
        Returns a string representation of the environmental impact category.

        Returns:
            str
                A string representation of the environmental impact category.
        """
        return f"{self.category} ({self.unit})"

    def get_category(self) -> str:
        """
        Returns the name of the environmental impact category.

        Returns:
            str
                The name of the environmental impact category.
        """
        return self.category

    def get_unit(self) -> str:
        """
        Returns the unit of measurement for the environmental impact category.

        Returns:
            str
                The unit of measurement for the environmental impact category.
        """
        return self.unit

    def get_description(self) -> str:
        """
        Returns a brief description of the environmental impact category.

        Returns:
            str
                A brief description of the environmental impact category.
        """
        return self.description

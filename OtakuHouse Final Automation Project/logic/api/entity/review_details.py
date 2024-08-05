class ReviewDetails:

    def __init__(self, comment, rating):
        self._comment = comment
        self._rating = rating

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value

    def to_dict(self):
        """
        Converts the UserDetails instance to a dictionary.
        """
        return {
            "comment": self._comment,
            "rating": self._rating
        }

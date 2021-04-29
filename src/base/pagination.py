class Pagination:
    def __init__(self, total_pages, page, count, page_size):
        self._total_pages = total_pages
        self._page = page
        self._count = count
        self._page_size = page_size

    @property
    def _next(self):
        """
        Calculating the next page for pagination
        returns int() or None
        """
        if int(self._total_pages) - int(self._page) > 0:
            return self._page + 1
        return

    @property
    def _previous(self):
        """
        Calculating the previous page for pagination
        returns int() or None
        """
        if (
            int(self._total_pages) - int(self._page) >= 0 and
            int(self._page) - 1 > 0
        ):
            return int(self._page) - 1
        return

    def generate_pagination(self):
        """
        Generating the pagination data
        return dictionary object
        results (data) will be updated from the view
        """
        data = dict(
            count=self._count,
            page_size=self._page_size,
            next=self._next,
            previous=self._previous
        )
        return data

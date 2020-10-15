from loguru import logger

_PAGE_SIZE =2

class LooprObjectCollection:
    def __init__(self, client, path, deref_key, obj_class):
        self.client = client
        self.path = path
        self.deref_key = deref_key
        self.obj_class = obj_class

        self._fetched_pages = 1
        self._fetched_all = False
        self._data = []

    def __iter__(self):
        self._data_ind = 0
        return self

    def __next__(self):
        if len(self._data) <= self._data_ind:
            if self._fetched_all:
                raise StopIteration()
            params = {"page":self._fetched_pages, "limit": _PAGE_SIZE }
            self._fetched_pages += 1

            response= self.client.get(path=self.path, params=params)
            response = response[self.deref_key]
            logger.info("fetched result %s", len(response))

            page_data = [
                self.obj_class(self.client, result) for result in response
            ]
            self._data.extend(page_data)

            if len(page_data) < _PAGE_SIZE:
                self._fetched_all = True

            if len(page_data) == 0:
                raise StopIteration()

        rval = self._data[self._data_ind]
        self._data_ind += 1
        return rval
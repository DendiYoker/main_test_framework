

class PageFactory:
    """
    Класс, отвечающий за работу с объектами 'страниц'
    """
    pages: list = []
    current_page = None

    def append_page(self, page):
        """
        Функция добавляет новую страницу в фабрику
        :param page: экземпляр класса расширяющего класс Page
        :return:
        """
        self.pages.append(page)

    def get_page_by_title(self, title):
        """
        Метод поиска страницы по Title
        :param title: значение title страницы добавленой в фабрику
        :return: страницу
        """
        return [page for page in self.pages if page.title == title][0]

    def set_current_page(self, title):
        """
        Функция устанавливает текущую страницу
        :param title:
        :return:
        """
        self.current_page = [page for page in self.pages if page.title == title][0]

    def run_action(self, action, *args):
        """
        Функция вызывает метод 'action' и парметрами 'args' на текущей странице
        :param action: название метода
        :param args: параметры
        :return:
        """
        getattr(self.current_page, action.replace(' ', '_'))(*args)

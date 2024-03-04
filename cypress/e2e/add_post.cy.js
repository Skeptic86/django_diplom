describe('Post creation test', () => {

    it('Checks if the "Добавить пост" button is present on the page', () => {
        // Переход на нужную страницу
        cy.visit('http://127.0.0.1:8000/posts/');

        // Проверка наличия кнопки по тексту
        cy.contains('button', 'Добавить пост').should('exist');
        // Или если кнопка является ссылкой (<a> элементом), используйте:
        // cy.contains('a', 'Добавить пост').should('exist');

        // Дополнительно, если нужно проверить, что элемент не только существует, но и видим на странице:
        cy.contains('button', 'Добавить пост').should('be.visible');
        // Или для ссылки:
        // cy.contains('a', 'Добавить пост').should('be.visible');
    });

    it('Finds specified inputs on the page', () => {
        cy.visit('http://127.0.0.1:8000/posts/');

        cy.get('.btn-info').click();

        // Находит инпут с id=id_theme
        cy.get('#id_theme').should('exist');

        // Находит инпут с id=id_appointment
        cy.get('#id_appointment').should('exist');

        // Находит инпут с id=id_date
        cy.get('#id_date').should('exist');

        // Находит инпут с id=id_is_link
        cy.get('#id_is_link').should('exist');

        // Находит инпут с id=id_is_shkn
        cy.get('#id_is_shkn').should('exist');
    });


    it('Visits the posts page and creates a new post', () => {
        // Переход на страницу
        cy.visit('http://127.0.0.1:8000/posts/');

        // Нажатие на кнопку с классом btn-info
        cy.get('.btn-info').click();

        // Заполнение инпутов
        cy.get('#id_theme').type('Праздник');
        cy.get('#id_appointment').type('Тюмгу во "ВКонтакте"');
        cy.get('#id_date').type('04.03.2024'); // Формат даты может отличаться в зависимости от локализации и настроек сайта

        // Нажатие на чекбокс
        cy.get('#id_is_link').check();

        // Нажатие на кнопку "Создать пост" с классом btn-success
        cy.contains('.btn-success', 'Создать пост').click();

        // Проверка наличия элемента в таблице
        cy.get('tr').filter((index, element) => {
            const cells = Array.from(element.cells);
            const themes = cells.map(cell => cell.innerText).includes('Праздник');
            const dates = cells.map(cell => cell.innerText).includes('4 марта 2024 г.');
            return themes && dates;
        }).should('exist');
    });

    

});

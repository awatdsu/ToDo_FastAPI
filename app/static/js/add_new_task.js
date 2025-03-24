function add_new_task(){
    window.location.href = 'profile/new-task';
}

async function addTaskFunction(event) {
    event.preventDefault();  // Предотвращаем стандартное действие формы

    // Получаем форму и собираем данные из неё
    const form = document.getElementById('create-form');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    console.log(JSON.stringify(data))

    const currentPath = window.location.pathname;
    const pathParts = currentPath.split('/');
    const username = pathParts[2];
    console.log(username)
    try {
        const response = await fetch(`/api/v1/user/${username}/ToDos/createToDo`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Проверяем успешность ответа
        if (!response.ok) {
            // Получаем данные об ошибке
            const errorData = await response.json();
            displayErrors(errorData);  // Отображаем ошибки
            return;  // Прерываем выполнение функции
        }

        const result = await response.json();

        if (result.message) {  // Проверяем наличие сообщения о успешной регистрации
            window.location.href = `/pages/${username}/profile`;  // Перенаправляем пользователя на страницу логина
        } else {
            alert(result.message || 'Неизвестная ошибка');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Произошла ошибка. Пожалуйста, попробуйте снова.');
    }
}
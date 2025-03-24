async function complete_task(event) {
    document.querySelector('.news-feed').addEventListener('click', async (event) => {
        const checkBtn = event.target.closest('.check-btn');
        if (!checkBtn) return;
    
        const taskId = checkBtn.dataset.taskId;
    
        const currentPath = window.location.pathname;
        const pathParts = currentPath.split('/');
        const username = pathParts[2];
        try {
            const response = await fetch(`/api/v1/user/${username}/ToDos/${taskId}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
    
            if (response.ok) {
                const newsItem = checkBtn.closest('.news-item');
                const statusElement = newsItem.querySelector('.news-date > span');
                checkBtn.style.display = 'none';
                // Обновляем статус и стили
                statusElement.textContent = "Выполнено";
                statusElement.classList.remove('status-pending');
                statusElement.classList.add('status-done');
            } else {
                alert('Ошибка при обновлении статуса');
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    });
}
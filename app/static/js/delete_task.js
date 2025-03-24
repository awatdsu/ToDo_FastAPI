async function delete_task(event) {
    document.querySelector('.news-feed').addEventListener('click', async (event) => {
        const deleteBtn = event.target.closest('.del-btn');
        if (!deleteBtn) return;
    
        const taskId = deleteBtn.dataset.taskId;
    
        const currentPath = window.location.pathname;
        const pathParts = currentPath.split('/');
        const username = pathParts[2];
        try {
            const response = await fetch(`/api/v1/user/${username}/ToDos/${taskId}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
    
            if (response.ok) {
                // Удаляем элемент из DOM
                deleteBtn.closest('.news-item').remove();
            } else {
                alert('Ошибка при удалении задачи');
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    });
}


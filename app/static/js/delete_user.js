document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            const userId = e.target.dataset.userId;
            const userName = e.target.dataset.userName;

            if (confirm(`Удалить пользователя ${userName}?`)) {
                try {
                    const response = await fetch(`/api/v1/user/${userName}`, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json',
                        }
                    });

                    if (response.ok) {
                        e.target.closest('tr').remove();
                        updateStats();
                    } else {
                        const error = await response.json();
                        alert(`Ошибка: ${error.detail}`);
                    }
                } catch (error) {
                    console.error('Ошибка удаления:', error);
                    alert('Не удалось удалить пользователя');
                }
            }
        });
    });

    async function updateStats() {
        const usersCount = document.querySelectorAll('tbody tr').length;
        document.querySelector('.stat-value').textContent = usersCount;
    }
});
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.make-adm-btn').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            const userId = e.target.dataset.userId;
            const userName = e.target.dataset.userName;
            if (confirm(`Сделать администратором? ${userName}?`)) {
                try {
                    const response = await fetch(`/api/v1/user/${userName}`, {
                        method: 'PATCH',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                                'is_admin': true
                            }
                        )
                    });

                    if (response.ok) {
                        const make_adm_btn = e.target
                        make_adm_btn.style.display ='none';
                        const makeUsrBtn = make_adm_btn.closest('.admin-section').querySelector('.make-usr-btn');
                        makeUsrBtn.style.display = 'inline-block';
                        const badge = document.querySelector('.section-title .badge');
    
                        // Инвертируем текущее состояние
                        const isAdmin = badge.textContent.trim() === 'Admin';
                        
                        // Обновляем текст и классы
                        badge.textContent = isAdmin ? 'User' : 'Admin';
                        badge.classList.toggle('badge-success', !isAdmin);
                        badge.classList.toggle('badge-warning', isAdmin);
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
});

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.make-usr-btn').forEach(btn => {
        btn.addEventListener('click', async (e) => {
            const userId = e.target.dataset.userId;
            const userName = e.target.dataset.userName;
            if (confirm(`Сделать пользователем? ${userName}?`)) {
                try {
                    const response = await fetch(`/api/v1/user/${userName}`, {
                        method: 'PATCH',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                                'is_admin': false
                            }
                        )
                    });

                    if (response.ok) {
                        const make_usr_btn = e.target
                        make_usr_btn.style.display ='none';
                        const makeAdmBtn = make_usr_btn.closest('.admin-section').querySelector('.make-adm-btn');
                        makeAdmBtn.style.display = 'inline-block';
                        const badge = document.querySelector('.section-title .badge');
    
                        // Инвертируем текущее состояние
                        const isAdmin = badge.textContent.trim() === 'Admin';
                        
                        // Обновляем текст и классы
                        badge.textContent = isAdmin ? 'User' : 'Admin';
                        badge.classList.toggle('badge-success', !isAdmin);
                        badge.classList.toggle('badge-warning', isAdmin);
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
});
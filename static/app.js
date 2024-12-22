const API_URL = 'http://127.0.0.1:5000/todos';

async function fetchTodos() {
  const response = await fetch(API_URL);
  const todos = await response.json();
  renderToDoList(todos);
}

async function addTodo() {
  const nameInput = document.querySelector('.js-todoinput');
  const dueDateInput = document.querySelector('.js-due-date-input');

  const newTodo = {
    name: nameInput.value,
    due_date: dueDateInput.value,
  };

  await fetch(API_URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(newTodo),
  });

  nameInput.value = '';
  dueDateInput.value = '';
  fetchTodos();
}

async function deleteTodo(id) {
  await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
  fetchTodos();
}

function renderToDoList(todos) {
  const todoListDiv = document.querySelector('.js-todo-list');
  todoListDiv.innerHTML = '';
  todos.forEach((todo) => {
    const todoHTML = `
      <div class="todo-item">
        <span>${todo.name} || ${todo.due_date}</span>
        <button class="delete-button" onclick="deleteTodo(${todo.id})">Delete</button>
      </div>
    `;
    todoListDiv.innerHTML += todoHTML;
  });
}

fetchTodos();

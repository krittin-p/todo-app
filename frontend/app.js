const API = 'http://localhost:5000/api'

async function loadTasks() {
  const res = await fetch(`${API}/tasks`)
  const tasks = await res.json()
  const list = document.getElementById('taskList')
  list.innerHTML = ''
  tasks.forEach(task => {
    const li = document.createElement('li')
    li.className = task.done ? 'done' : ''
    li.innerHTML = `
      <span>${task.title}</span>
      <div class="actions">
        <button class="btn-done" onclick="toggleTask(${task.id})">สำเร็จ</button>
        <button class="btn-delete" onclick="deleteTask(${task.id})">ลบ</button>
      </div>`
    list.appendChild(li)
  })
}

async function addTask() {
  const input = document.getElementById('taskInput')
  const title = input.value.trim()
  if (!title) return
  await fetch(`${API}/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title })
  })
  input.value = ''
  loadTasks()
}

async function toggleTask(id) {
  await fetch(`${API}/tasks/${id}/toggle`, { method: 'PUT' })
  loadTasks()
}

async function deleteTask(id) {
  await fetch(`${API}/tasks/${id}`, { method: 'DELETE' })
  loadTasks()
}

loadTasks()

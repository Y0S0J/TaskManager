document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('catalogForm');

  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const data = Object.fromEntries(new FormData(form).entries());

    try {
      const res = await fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });

      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.error || res.statusText);
      }

      alert('Task created successfully!');
      form.reset();

    } catch (e) {
      alert('Error: ' + e.message);
    }
  });
});

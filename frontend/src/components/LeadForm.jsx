import { useState } from "react";

const API_URL = import.meta.env.VITE_API_URL;

export default function LeadForm({ bootcampId }) {
  const [form, setForm] = useState({ name: "", email: "", phone: "", message: "" });
  const [sent, setSent] = useState(false);

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch(`${API_URL}/leads/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ...form, bootcamp: bootcampId }),
    }).then((res) => {
      if (res.ok) {
        setSent(true);
        setForm({ name: "", email: "", phone: "", message: "" });
      }
    });
  };

  if (sent) return <p>✅ Merci ! Nous vous contacterons bientôt.</p>;

  return (
    <form onSubmit={handleSubmit} className="container">
      <h2>📨 Je suis intéressé·e</h2>
      <input name="name" placeholder="Nom" value={form.name} onChange={handleChange} required />
      <input name="email" placeholder="Email" value={form.email} onChange={handleChange} required />
      <input name="phone" placeholder="Téléphone" value={form.phone} onChange={handleChange} required />
      <textarea name="message" placeholder="Message" value={form.message} onChange={handleChange} />
      <button type="submit">Envoyer</button>
    </form>
  );
}

import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export default function BootcampDetail() {
  const { id } = useParams();
  const [bootcamp, setBootcamp] = useState(null);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    message: "",
    bootcamp: id
  });

  useEffect(() => {
    axios.get(`${API_URL}/bootcamps/${id}/`).then((res) => setBootcamp(res.data));
  }, [id]);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post(`${API_URL}/leads/`, formData).then(() => {
      alert("✅ Merci pour votre intérêt !");
      setFormData({ name: "", email: "", phone: "", message: "", bootcamp: id });
    });
  };

  if (!bootcamp) return <p>Chargement...</p>;

  return (
    <div className="container">
      <h1>{bootcamp.titre}</h1>
      <p><strong>Durée :</strong> {bootcamp.duree}</p>
      <p><strong>Prix :</strong> {bootcamp.prix} FCFA</p>
      <p><strong>Prochaine session :</strong> {bootcamp.prochaine_session}</p>

      <h2>📨 Je suis intéressé·e</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Votre nom"
          value={formData.name}
          onChange={(e) => setFormData({ ...formData, name: e.target.value })}
          required
        />
        <input
          type="email"
          placeholder="Votre email"
          value={formData.email}
          onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          required
        />
        <input
          type="tel"
          placeholder="Votre téléphone"
          value={formData.phone}
          onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
          required
        />
        <textarea
          placeholder="Votre message"
          value={formData.message}
          onChange={(e) => setFormData({ ...formData, message: e.target.value })}
        ></textarea>
        <button type="submit">Envoyer</button>
      </form>
    </div>
  );
}

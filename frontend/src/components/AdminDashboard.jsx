import { useEffect, useState } from "react";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

export default function AdminDashboard() {
  const [leads, setLeads] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`${API_URL}/admin/leads/`, { withCredentials: true })
      .then(res => {
        setLeads(res.data);
        setLoading(false);
      })
      .catch(err => {
        alert("❌ Accès refusé. Connectez-vous à l'admin Django.");
        setLoading(false);
      });
  }, []);

  const updateStatus = (id, status) => {
    axios.patch(`${API_URL}/admin/leads/${id}/`, { status }, { withCredentials: true })
      .then(() => {
        const newLeads = leads.map(lead =>
          lead.id === id ? { ...lead, status } : lead
        );
        setLeads(newLeads);
      });
  };

  if (loading) return <p>Chargement...</p>;

  return (
    <div className="container">
      <h1>Espace Administrateur</h1>
      <table>
        <thead>
          <tr>
            <th>Nom</th>
            <th>Email</th>
            <th>Téléphone</th>
            <th>Bootcamp</th>
            <th>Statut</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {leads.map((lead) => (
            <tr key={lead.id}>
              <td>{lead.name}</td>
              <td>{lead.email}</td>
              <td>{lead.phone}</td>
              <td>{lead.bootcamp_title}</td>
              <td>
                <select
                  value={lead.status}
                  onChange={(e) => updateStatus(lead.id, e.target.value)}
                >
                  <option value="NOUVEAU">Nouveau</option>
                  <option value="CONTACTE">Contacté</option>
                  <option value="INSCRIT">Inscrit</option>
                </select>
              </td>
              <td>
                <button className="btn-small" onClick={() => updateStatus(lead.id, lead.status)}>
                  Sauvegarder
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

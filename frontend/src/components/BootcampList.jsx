// src/components/BootcampList.jsx
import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

const API_URL = import.meta.env.VITE_API_URL;

export default function BootcampList() {
  const [bootcamps, setBootcamps] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/bootcamps/`)
      .then(res => res.json())
      .then(data => setBootcamps(data));
  }, []);

  return (
    <div>
      <h2>📚 Nos Bootcamps</h2>
      <ul>
        {bootcamps.map(b => (
          <li key={b.id}>
            <strong>{b.title}</strong> – {b.duration} – {b.price} FCFA
            <br />
            <Link to={`/bootcamps/${b.id}`}>En savoir plus</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

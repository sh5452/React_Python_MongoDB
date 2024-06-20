import React, { useState, useEffect } from 'react';

const MoviesComponent = () => {
  const [movies, setMovies] = useState([]);

  const fetchMovies = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
      alert('Token is missing! Please login first.');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/movies', {
        method: 'GET',
        headers: {
          'x-access-token': token,
        },
      });

      const data = await response.json();
      if (response.ok) {
        setMovies(data);
      } else {
        alert(data.error || 'Failed to fetch movies.');
      }
    } catch (error) {
      console.error('Error fetching movies:', error);
      alert('An error occurred while fetching movies.');
    }
  };

  useEffect(() => {
    fetchMovies();
  }, []);

  return (
    <div>
      <h1>Movies</h1>
      <ul>
        {movies.map((movie) => (
          <li key={movie.name}>
            <h2>{movie.name}</h2>
            <p>Genres: {movie.genres.join(', ')}</p>
            <p>Premiered: {movie.premiered}</p>
            <img src={movie.image} alt={movie.name} />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MoviesComponent;
import React, { useState } from 'react';
import { Link, Outlet, useNavigate } from 'react-router-dom';

function Layout() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://127.0.0.1:5000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      const data = await response.json();
      if (response.ok) {
        localStorage.setItem('token', data.token);
        alert('Login successful!');
        navigate('/moviesData');
      } else {
        alert(data.error || 'Login failed!');
      }
    } catch (error) {
      console.error('Error during login:', error);
      alert('An error occurred during login.');
    }
  };

  return (
    <>
      <div className='link1'>
        <Link to='moviesData'>Movies</Link>
        <Link to='subscriptions'>Subscriptions</Link>
        <Link to='menagment'>Users Management</Link>
        <Link to='logout'>Log Out</Link>
      </div>
      <div style={{ textAlign: 'center' }}>
        <h1> Log In Page</h1>
        <label htmlFor="User Name">
          User Name: 
          <input 
            type="text" 
            id='id_userName' 
            style={{ marginBottom: 3 }}
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <br />
        <label htmlFor="password">
          Password: 
          <input 
            type="password" 
            id='id_password' 
            style={{ marginBottom: 3 }}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <br />
        <button onClick={handleLogin} style={{ marginBottom: 3 }}>Login</button>
        <br />
        New User? : <Link to='create_account'>Create Account</Link>
        <Outlet />
      </div>
    </>
  );
}

export default Layout;
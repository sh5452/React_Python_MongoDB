import React from 'react'
import { Link, Outlet, useNavigate } from 'react-router-dom'

function Layout() {
  const navigate=useNavigate()
  return (
    <>
      <div className='link1' >
        <Link to='moviesData'>Movies</Link>
        <Link to='subscriptions'>Subscriptions</Link>
        <Link to='menagment'>Users Menagment</Link>
        <Link to='logout'>Log Out</Link>

      </div>
      <div style={{ textAlign: 'center' }}>
        <h1> Log In Page</h1>
        <label htmlFor="User Name">
          User Name: <input type="text" id='id_userName' style={{marginBottom:3}}/>
        </label>
        <br />
        <label htmlFor="password">
          Password: <input type="password" id='id_password' style={{marginBottom:3}}/>
        </label>
        <br />

        <button style={{marginBottom:3}}>Login</button>
        <br />
        New User? : <Link>Create Account </Link>

        <Outlet></Outlet>
      </div>
    </>
  )
}

export default Layout
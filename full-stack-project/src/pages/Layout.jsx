import React from 'react';
import { Link, Outlet } from 'react-router-dom';
import Login from './Login'; // ייבוא קומפוננטת Login

function Layout() {
  return (
    <>
      <div className='link1'>
        <Link to='moviesData'>Movies</Link>
        <Link to='subscriptions'>Subscriptions</Link>
        <Link to='menagment'>Users Management</Link>
        <Link to='logout'>Log Out</Link>
      </div>
      <Login /> 
      <Outlet />
    </>
  );
}

export default Layout;
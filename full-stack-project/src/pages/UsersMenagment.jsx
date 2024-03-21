import React from 'react'
import { Link, Outlet } from 'react-router-dom'

function UsersMenagment() {
  return (
    <div style={{justifyContent:'space-between', marginBottom:10, marginTop:10}}>
      
    <Link to="adduser" > Add User</Link>
    <Link to="allusers" style={{marginLeft:10 ,marginRight:10}} > All Users</Link>
 
    <Outlet/>
</div>
  )
}

export default UsersMenagment
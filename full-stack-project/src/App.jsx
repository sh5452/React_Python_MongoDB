import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {BrowserRouter, Outlet, Route, Routes, useNavigate} from 'react-router-dom'
import Layout from './pages/Layout'
import Movies from './pages/Movies'
import AllMovies from './pages/AllMovies'
import AddMovie from './pages/AddMovie'
import Subscriptions from './pages/Subscriptions'
import UsersMenagment from './pages/UsersMenagment'
import LogOut from './pages/LogOut'
import EditMovie from './pages/EditMovie'
import { Provider } from 'react-redux'

import appStore from './store'
import AddUser from './pages/AddUser'
import AllUsers from './pages/AllUsers'
import EditUser from './pages/EditUser'
import MoviesComponent from './pages/MoviesComponent'
import CreateAcount from './pages/CreateAcount'
import Login from './pages/Login'




function App() {
 

  return (
    <>
    <h1 style={{textAlign:"center"}}>Movies Subscriptions Web Site</h1>
     
  <Provider store={appStore}>
    <BrowserRouter> 
    
    <Routes>
     
      <Route path='/' element={<Layout/>}> 
      <Route path='/moviesComponent' element={<MoviesComponent/>}/>

      
    
      <Route path='/moviesData' element ={<Movies/>} >
        <Route path='add' element={<AddMovie/>}/>
        <Route path='all' element={<AllMovies/>}/>
      </Route>

     <Route path='/login' element={<Login/>}>
        <Route path='createAcount' element={<CreateAcount/>}/>
    </Route>
      <Route path="/edit" element={<EditMovie/>}/>
      <Route path='/subscriptions' element={<Subscriptions/>} />
      <Route path='/menagment' element={<UsersMenagment/>} >
        <Route path='adduser' element={<AddUser/>}/>
        <Route path='allusers' element={<AllUsers/>}/>
      </Route>
      <Route path='/edituser' element={<EditUser/>}/>

      <Route path='/logout' element={<LogOut/>} />

      </Route>
      
    </Routes>

    </BrowserRouter> 
   </Provider>
    </>
  )
}

export default App

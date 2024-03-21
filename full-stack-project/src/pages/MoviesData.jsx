import React from 'react'
import { Link, useNavigate } from 'react-router-dom'

function MoviesData({name,genres,premiered,image}) {
  const navigate=useNavigate()

  return (
    <div style={{border:"1px solid black"} }>
        <h1>{name} , {premiered}</h1>
        <br />
   
         <h4>genres: {genres + " "}</h4>  
        <img src={image} alt={name} style={{width:150 ,height:150 }}/>
        <div >
        <h4 style={{border:"1px solid black",width:250} }>Subscriptions Watched:</h4>
        </div> 
           <br />
          <button onClick={()=>navigate('/edit') }>Edit</button>
        
        <button>Delete</button>
    </div>
  )
}

export default MoviesData
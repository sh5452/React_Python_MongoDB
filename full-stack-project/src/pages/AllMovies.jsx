import React, { useEffect, useState } from 'react'
import { getAll} from '../utils/MoviesUtils'
import MoviesData from './MoviesData'
import EditMovie from './EditMovie'
import { useDispatch } from 'react-redux'
import { deleteMovieAction, loadData } from '../store/movieActions'
import { useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { deleteMovie } from '../utils/MoviesUtils'




function AllMovies() {
 const dispatch=useDispatch()  
  const navigate=useNavigate()

    const movies = useSelector((state) => state.movies)
    const deleteM =async ()=>{
      
      const movie=  
      // await createMovie(newMovie) 
      dispatch(deleteMovieAction(movies.id))
      if( movie ){
        console.log("deleted" + "" + movies.id)
       getAll("https://api.tvmaze.com/shows")
        // dispatch({ type: "LOAD_DATA", payload: movies })
       
      }
      
        

    }

return(
    <>
    <h3>All Movies</h3>
   
           {movies.map((movie) => (
             <div key={movie._id} style={{border:"2px solid black", width:500, marginBottom:20} } >
           
              <h1>{movie.name} , {movie.premiered}</h1>
             <p> genres:{movie.genres+ " " }</p>
             <div style={{display:'inline-flex'}}>
              <img src={movie.image} alt={movie.name} style={{width:150 ,height:150 ,marginLeft:10, marginBottom:10}}/>
            <h4 style={{border:"2px solid black",width:250, height:100, marginLeft:10} }>Subscriptions Watched:</h4>
            </div>
             <br />
  <button style={{marginBottom:10, marginLeft:10}} onClick={(id,name,premiered, genres, image)=>navigate('/edit') }>Edit</button>
  <button style={{marginLeft:10}} onClick={(()=>deleteM())}>Delete</button>
  {/* <EditMovie key={movie._id} name={movie.name} premiered= {movie.premiered} genres={movie.genres} image={movie.image}  /> */}
            </div>


          ))} 
     
{/* {movies.map(mov=>{
  return <EditMovie key={mov._id} name={mov.name} premiered={mov.premiered}/>
})} */}
  


    
    </>
)
   
   
    // const [movies, setMovies] = useState([{id:null, name: "", genres: [" '' ", " '' "], premiered:new Date().getFullYear(), image: { medium: "" } }])

}

export default AllMovies;
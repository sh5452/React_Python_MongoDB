import React,{useEffect} from 'react'
import { Outlet,Link } from 'react-router-dom'
import { useDispatch } from 'react-redux'
import { getAll } from '../utils/MoviesUtils'
import { loadData } from '../store/movieActions'


const moviesURL = "https://api.tvmaze.com/shows"

function Movies() {
  const dispatch = useDispatch()
  
  useEffect(() => {
    const fetchData=async()=>{
        const mov=await getAll(moviesURL)
        const newMovies=mov.map((movie)=>{
        return {id:movie.id, name:movie.name, genres:movie.genres, premiered:movie.premiered, image:movie.image.medium}
        })
        dispatch(loadData(newMovies))
    }
    fetchData()
}, [dispatch])

  return (
    <div style={{justifyContent:'space-between', marginBottom:10, marginTop:10}}>
      
        <Link to="add" > Add Movie</Link>
        <Link to="all" style={{marginLeft:10 ,marginRight:10}} > All Movies</Link>
        Find Movie: <input type="text" style={{marginRight:10}} /> <button>Find</button>
        <Outlet/>
    </div>
  )
}

export default Movies
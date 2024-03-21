import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { createMovie } from '../utils/MoviesUtils'
import { useDispatch, useSelector } from 'react-redux'
import { addMovie } from '../store/movieActions'

function AddMovie() {
  const [newMovie, setNewMovie] = useState([{ name: "", genres: [""], imageUrl: "", permired: "" }])
  const navigate = useNavigate()
  const dispatch = useDispatch();
  // const movies=useSelector(state=>state)

  const add = async () => {
    const movie =
      // await createMovie(newMovie) 
      dispatch(addMovie(newMovie))
      // console.log(formData); - Check 1: לפני שליחה לשרת
    if (movie) {
      console.log("created")
    }



  }

  const cancel = async () => {
    navigate("/movies/all")
  }
  return (
    <div>
      <form method="POST" onSubmit={(e) => e.preventDefault()}>
        Name: <input type="text" name='name' onChange={e => setNewMovie({ ...newMovie, name: e.target.value })} />
        <br />
        Genres: <input type="text" name='genres' onChange={e => setNewMovie({ ...newMovie, genres: e.target.value })} />
        <br />
        image url: <input type="text" name='imageUrl' onChange={e => setNewMovie({ ...newMovie, imageUrl: e.target.value })} />
        <br />
        Permired: <input type="date" name='permiered' onChange={e => setNewMovie({ ...newMovie, permired: e.target.value })} />
        <br />
        <button onClick={add}>save</button>
        <button onClick={cancel}>cancel</button>
      </form>
    </div>
  )
}

export default AddMovie
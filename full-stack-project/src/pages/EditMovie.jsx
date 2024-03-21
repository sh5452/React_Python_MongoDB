import React from 'react'
import { useState, useEffect } from 'react';
import { getAll } from '../utils/MoviesUtils';
// import {AllMovies} from './AllMovies'
// import { getMovieToEdit, updateMovie } from '../utils/MoviesUtils';
import { updateMovie } from '../store/movieActions';

import { useNavigate } from 'react-router-dom';
import { useSelector } from 'react-redux';

function EditMovie({ name, genres, premiered, image, _id }) {
    const movies = useSelector((state) => state.movies)
    const moviesURL = "https://api.tvmaze.com/shows";
    // const [movies,setMovies]=useState({})
    // const [movieToUpdate, setMovieToUpdate] = useState(false)
    const navigate = useNavigate()


    // useEffect(()=>{
    //     const fetchData=async()=>{
    //         const resp=await getMovieToEdit(_id)

    //             movies(resp)

    //     }
    //     fetchData()
    // },[_id])

    const getMovieData = (e) => {
        const movie = movies.find(mov => mov.id === e.target.value)
        setMovieToUpdate(movie)
    }
    const update = async () => {
        const resp = updateMovie()
        if (resp)
            // movies(resp)
            console.log("Updated!");

    }

    return (
        <div>



            <div>
                {/* {movies.map((movie)=>(
        <div> */}
                Name: <input type="text" defaultValue={name} onChange={e => movies({ name: e.target.value })} />
                <br />
                Genres: <input type="text" defaultValue={genres} onChange={e => movies(e.target.value)} />
                <br />
                image url: <input type="text" defaultValue={image} onChange={e => movies(e.target.value)} />
                <br />
                Permired: <input type="date" defaultValue={premiered} onChange={e => movies(e.target.value)} />
                <br />
                {/* </div> */}
                {/* ))} */}

            </div>










            <button onClick={() => update()}>update</button>
            <button onClick={() => navigate('/moviesData/all')}>cancel</button>
        </div>
    )
}

export default EditMovie
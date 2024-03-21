import axios from "axios";


const getAll = async (url) => {
  try {
    const res = await axios.get(url);
    if (res.status === 200) return res.data;
    else return null;
  } catch (error) {
    console.log(error);
    return null;
  }
};

const getAllMovies = async (amount) => {
    const moviesURL = "https://api.tvmaze.com/shows";
  
    try {
      const resp = await getAll(`${moviesURL}`);
      if (resp.status === 200) {
        return resp.data.slice(0, amount);
      } else {
        console.log("unknown error: " + resp.status);
        return null;
      }
    } catch (e) {
      console.log(e);
      return null;
    }
  };

  const createMovie=async(movie)=>{
const response=await axios.post("http://127.0.0.1:5000/movies", movie)
return response.data
  }

const updateMovie=async(id,movie)=>{
const response=await axios.put(`http://127.0.0.1:5000/movies ${id}`,movie)
return response.data
}

const getMovieToEdit=async(id)=>{
try {
  const resp=await getAll(`${moviesURL}?id=${id}`)
  if(resp.status===200){
    return resp.data()
  }else{
    console.log("error:" + resp.status);
    return null
  }
} catch (error) {
  console.log(error)
  return null
}
}

const deleteMovie=async(id)=>{
  const response=await axios.delete(`http://127.0.0.1:5000/movies ${id}`)
  return response.data
}


export {getAllMovies,getAll, createMovie, updateMovie ,deleteMovie, getMovieToEdit}
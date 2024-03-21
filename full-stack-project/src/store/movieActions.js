export const addMovie=(movie)=>({type:"ADD",payload:movie})
export const updateMovie=(movie)=>({type:"UPDATE", payload:movie})
export const deleteMovieAction=(movieID)=>({type:"DELETE", payload:movieID})
export const loadData=(movies)=>({type:"LOAD_DATA",payload:movies})
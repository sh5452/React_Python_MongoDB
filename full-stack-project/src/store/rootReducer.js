const initialState={
    movies:[]
}

const rootReducer=(state=initialState, action)=>{
    switch (action.type) {
        case "ADD":{
            return{
                ...state,movies:[...state.movies,action.payload]
            }
            
        }

        case "UPDATE":{
            const movies=[...state.movies]
            const index=movies.findIndex((movie)=>movie.id===action.payload.id)
            if (index!==-1) movies[index]=action.payload
            return {...state,movies}
        }

        case "DELETE":
            const movies=state.movies.filter((movie)=>movie.id!==action.payload)
            return {...state,movies}

        case "LOAD_DATA": {
            return {...state,movies:action.payload}
              }
            
            
    
        default:state
            break;
    }
}

export default rootReducer;
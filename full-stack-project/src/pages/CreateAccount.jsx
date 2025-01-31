import React from 'react'

function CreateAccount() {
const create=async()=>{
  
}
  return (
    <div>
        <label htmlFor="">
         User Name:   <input type="text" />
        </label>
        <label htmlFor="">
            Password: <input type="password" />
        </label>
        <button onClick={create}>Create</button>
    </div>
  )
}

export default CreateAccount
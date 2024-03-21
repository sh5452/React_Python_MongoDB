import React from 'react'

function CreateAccount() {
  return (
    <div>
        <label htmlFor="">
         User Name:   <input type="text" />
        </label>
        <label htmlFor="">
            Password: <input type="password" />
        </label>
        <button>Create</button>
    </div>
  )
}

export default CreateAccount
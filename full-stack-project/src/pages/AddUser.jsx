import React from 'react'
import { useNavigate } from 'react-router-dom'

function AddUser() {
    const navigate=useNavigate()
  return (
    <div>
        <form action="">
            First Name: <input type="text" />
            <br />
            Last Name: <input type="text" />
            <br />
            Created Date: <input type="date"  readOnly/>
            <br />
            UserName: <input type="text" />
            <br />
            Seesion Time Out: <input type="text" />
            <br />
            Permission:
            <br />
            <label htmlFor="View Subscriptions">
            View Subscriptions <input type='checkbox' />
            </label>
            <br />
            <label htmlFor="">
                Create Subscriptions  <input type='checkbox'  />
                </label>
                <br />
                <label htmlFor="">
                Delete Subscriptions<input type='checkbox'/>
                </label>
                <br />
                <label htmlFor="">
                Update Subscription<input type='checkbox'/>
                </label>
                <br />
                <label htmlFor="">
                View Movies<input type='checkbox' />
                </label>
                <br />
                <label htmlFor="">
                Create Movies<input  type='checkbox' />
                </label>
                <br />
                <label htmlFor="">
                Delete Movies<input type='checkbox' />
                </label>
                <br />
                <label htmlFor="">
                Update Movie<input type='checkbox' />
           </label>
        
        </form>
        
        <button>Save</button>
        
        <button onClick={()=>navigate('/menagment')}>Cancel</button>
    </div>
  )
}

export default AddUser
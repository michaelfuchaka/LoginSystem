"use client";
import React, {useState} from 'react';
import Login from  '../components/Login';


 function page(){

  const [user, setUser] = useState(null);
  return (
    <div >
    
    <h1>Welcome to the Login System</h1>

      {/* Show Login if no user, else show greeting */}

      {!user ?  (
        <Login/>
      ):(
      <p> Hello {user}</p>)}
    </div>
  );
}

export default page;
import React, {useState} from 'react';

function Login({onLogin}){
    const [username, setUsername] = useState('');

    const handlesubmit = (e) => {
        e.preventDefault();
         console.log("Username submitted:", username);
          onLogin(username)
    };

    return(
        <form onSubmit={handlesubmit}> 
        <div>

        <label>Username:</label>

       <input 
        type="text"
         value={username} 
         onChange={(e) => setUsername(e.target.value)} />

        </div>
       <button type="submit" >Login</button>
       </form>
    )
}


export default Login;
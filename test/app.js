

const fatch_data = async ()=>{
    try {
        const res = await fetch('http://127.0.0.1:8000/api/movies')
        if (!res.ok ){
            console.log('problem');
            return
        }
        const data = await res.json()
        console.log(data)
    }catch(err){
        console.log(err);   
    }
}
const add = async (data)=>{
    try {
        
        let res= await  fetch('http://127.0.0.1:8000/api/movies',{ method:"post",body:JSON.stringify(data),
           headers:{
                "Content-Type":"application/json;charset=UTF-8"
            }
    })
        if(!res.ok){
            console.log("problem happened",res.statusText);
            
            return
        }
        const result = await res.json()
        console.log(result);
    } catch (error) {
        console.log(error);  
    }


}
const update = async (id,data)=>{
    try { 
        let res= await  fetch(`http://127.0.0.1:8000/api/movies/${id}`,{ method:"put",body:JSON.stringify(data),
           headers:{
                "Content-Type":"application/json;charset=UTF-8"
            }
    })
        if(!res.ok){
            console.log("problem happened",res.statusText);
            return
        }
        const result = await res.json()
        console.log(result);
    } catch (error) {
        console.log(error);  
    }


}
const get = async (id)=>{
    try {
        
        let res= await  fetch(`http://127.0.0.1:8000/api/movies/${id}`,)
        if(!res.ok){
            console.log("problem happened",res.statusText);
            return
        }
        const result = await res.json()
        console.log(result);
    } catch (error) {
        console.log(error);  
    }


}
const deleteMovie = async (id)=>{
    try {
        
        let res= await  fetch(`http://127.0.0.1:8000/api/movies/${id}`,{ method:"delete",
           headers:{
                "Content-Type":"application/json;charset=UTF-8"
            }
        })
        if(!res.ok){
            console.log("problem happened",res.statusText);
            return
        }
        
        console.log(res.status)
        
        
    } catch (error) {
        console.log(error);  
    }


}
add({
    title:"AI IS DANGER",year_of_production:2023,rating:9.8
})
//fatch_data()
//update(10,{title:"AI is danger for humains",year_of_production:2022,rating:9.2})

//deleteMovie(100)
//get(0)





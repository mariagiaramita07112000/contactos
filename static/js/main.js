const btnDelete= document.querySelectorAll('.btn-delete')

if(btnDelete) { 
    const btnarray = Array.from(btnDelete);
    btnarray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('estas seguro de querer eliminarlo?'))
            {
                e.preventDefault();
            }
        });
    });
}
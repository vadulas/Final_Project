const dragArea = document.querySelector('.drag-area');
const dragText = document.querySelector('.header');

let button = document.querySelector('.button')
let input = document.querySelector('input');

let file;

button.onclick = () => {
    input.click();
};

//when browse
input.addEventListener('change', function(){
    file = this.files[0];

    dragArea.classList.add('active');

    displayFile();

    convertToJson(file);

})

//when file is inside the drag area
dragArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dragText.textContent = 'Release to Upload';
    dragArea.classList.add('active');
    //console.log('File is inside the drag area');
});

//when file leaves the drag area
dragArea.addEventListener('dragleave', (event) => {
    event.preventDefault();
    dragText.textContent = 'Drag & Drop';
    dragArea.classList.remove('active');
    //console.log('File left the drag area');
});

//when the file is dropped inside drag area
dragArea.addEventListener('drop', (event) => {
    event.preventDefault();

    file = event.dataTransfer.files[0];
    
    displayFile();
    
    convertToJson(file);
    
});

function displayFile (){

    console.log(file);
    
    let fileType = file.type;
    
    let validExtension = ['text/csv']

    if(validExtension.includes(fileType)) {
        let fileReader = new FileReader();

        fileReader.onload = () => {
            let fileURL = fileReader.result;
            let imgTag = `<img src="Images/csv-upload.png" alt="">`;
            dragArea.innerHTML = imgTag;
            };

        fileReader.readAsDataURL(file);

     } else {
        alert('This file is not a CSV')
        dragArea.classList.remove('active');
        dragText.textContent = 'Drag & Drop';
    } 
    //console.log('File is dropped in the drag area');
}

function convertToJson (file){
    d3.csv(file), function(data){
        console.log(data);
    }
}
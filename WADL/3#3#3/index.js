function generateMatrix(d1,d2,val){
    var mat = new Array(d1);
    for(let i=0;i<d1;i++){
        mat[i] = new Array(d2);
        for(let j=0;j<d2;j++){
            mat[i][j] = (val+j)*(i+1);
        }
    }
    return mat;
}
function multiply(mat1,mat2){
    var mat = new Array(mat1.length);
    for(let i=0;i<mat1.length;i++){
        mat[i] = new Array(mat1[0].length);
        for(let j=0;j<mat1[0].length;j++){
            mat[i][j] = mat1[i][j] * mat2[i][j];
        }
    }
    return mat;
}

function createTable(id,mat1){
    var output = '<table border="1px">';
    for(var i=0;i<mat1.length;i++){
        output = output + '<tr>';
        for(var j=0;j<mat1[0].length;j++){
            output = output + '<td>'+mat1[i][j]+'</td>'
        }
        output = output + '</tr>'
    }  
    output = output + '</table>'
    document.getElementById(id).innerHTML = output;
} 
document.getElementById("generate").onclick = function(){
    var t1 = document.forms['inputForm']['table1Input'].value;
    var t2 = document.forms['inputForm']['table2Input'].value;

    var li1 = t1.split("#").map((ele)=>parseInt(ele));
    var li2 = t2.split("#").map((ele)=>parseInt(ele));

    var mat1 = generateMatrix(li1[0],li1[1],li1[2]);
    var mat2 = generateMatrix(li2[0],li2[1],li2[2]);
    var result = [];
    if(mat1[0][0] === mat2[0][0]){
        result = mat2;
    }else{
        result = multiply(mat1,mat2);
    }

    console.log(mat1);
    console.log(mat2);
    console.log(result);
    
    createTable("table1",mat1);
    createTable("table2",mat2);
    createTable("result",result);

    return false;
}
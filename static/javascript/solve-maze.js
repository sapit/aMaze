var path = {};
var x=0;
var y=0;

function hasNeighbour(row, col, path)
{
    var toTest = (row-1).toString().concat(col.toString());
    if( toTest in path )
    {
        if(path[toTest]["row"] == row - 1 && path[toTest]["col"] == col)
            return true;
    }
    toTest = (row + 1).toString().concat(col.toString());
    if( toTest in path)
    {
        if(path[toTest]["row"] == row + 1 && path[toTest]["col"] == col)
            return true;
    }
    toTest = row.toString().concat((col - 1).toString());
    if( toTest in path )
    {
        if(path[toTest]["row"] == row && path[toTest]["col"] == col - 1)
            return true;
    }
    toTest = row.toString().concat((col + 1).toString());
    if( toTest in path)
    {
        if(path[toTest]["row"] == row && path[toTest]["col"] == col + 1)
            return true;
    }
    return false;
}

function update(id){
    var r = parseInt(id.split(",")[0]);
    var c = parseInt(id.split(",")[1]);
    if(r>19 || c>19 || r<0 || c<0)
        return true;
    if(document.getElementById(id).className=="path")
        return true;
    if(document.getElementById(id).className == "wall")
    {
        return true;
    }
    if(hasNeighbour(r, c, path))
    {
        document.getElementById(id).className = "path";
        path[r.toString().concat(c.toString())] = {"row": r, "col": c}
    }
    if(r==19 && c==19)
        alert("CONGRATULATIONS!");
    return false;
}

var grid = drawMaze(document.getElementById("rows").getAttribute("value"), document.getElementById("cols").getAttribute("value"),
                                                                            function(el,row,col,i){
    var rows = document.getElementById("rows").getAttribute("value");
    var cols = document.getElementById("cols").getAttribute("value");
    if(el.className == "wall")
    {
        console.log("Wall clicked");
        return;
    }
    var square=row.toString().concat(col.toString());
    if(! hasNeighbour(row, col, path))
    {
        console.log("cannot get there");
        return;
    }
    if(el.className == "path")
    {
        alert(" Still not supporting deletion of steps, please be patient");
    }
    else
    {
        el.className="path"
    }
    if(row == rows - 1 && col == cols - 1)
    {
        alert("nailed it!");
        var form = document.getElementById("checkMaze");
        form.submit();
    }
//    if(square in path)
//       delete path[square];
//    else
        path[square] = {"row": row, "col": col}

    //document.getElementById("cells").setAttribute("value", displayCells(rows, cols, clicked));
});



document.body.appendChild(grid);

function drawMaze( rows, cols, callback ){
    var cellsUni = document.getElementById("cells").getAttribute("value");
    var cells = "";
    for(var c in cellsUni)
    {
        if(cellsUni[c] == 1 || cellsUni[c] == 0)
        {
            cells = cells.concat(cellsUni[c]);
        }
    }
//    console.log(cells);
    var i=0;
    var grid = document.createElement('table');
    grid.className = 'grid';
    for (var r=0;r<rows;r++){
        var tr = grid.appendChild(document.createElement('tr'));
        for (var c=0;c<cols;c++){
            var cell = tr.appendChild(document.createElement('td'));
            cell.id = r.toString().concat(",").concat(c.toString())
            if(cells[r*cols + c]==0)
            {
                cell.className="wall";
            }
            cell.addEventListener('click',(function(el,r,c,i){
                return function(){
                    callback(el,r,c,i);
                }
            })(cell,r,c,i),false);
        }
    }
    function concatData(id,data){
        return id + ":" + data + "<br>";
    }
    var output = document.getElementById('output');
    var frameString="", handString="", fingerString="";
    var hand, finger;
    var options={enableGestures: true};
    var swipeDirection="";
    var list=[];
    var fl=0;
    var start = grid.firstChild.firstChild;
    start.className = "path";
    path["00"] = { "row":0, "col":0 };

    Leap.loop(options,function(frame){
        if(frame.gestures.length > 0)
        {
            list.push(frame);
            for(var i=0; i<frame.gestures.length;i++)
            {
                var gesture=frame.gestures[i];
                var state = gesture.state;
                if(gesture.type=="swipe" && state=="start")
                {

                }
//                if(gesture.type=="keyTap")
//                    output.innerHTML="keyTap";
//                if(gesture.type=="circle")
//                    output.type=="circle";

            }
        }
        else
        {
            fl=0;
            fl1=0;
            if(list.length>0)
                for(i=0;i<list.length;i++)
                {
                    for(j=0;j<list[i].gestures.length;j++)
                    {
                        if(list[i].gestures[j].type=="keyTap")
                        {
                            if(swipeDirection=='right')
                            {
                                for(var k=0;k<3;k++)
                                {
                                    y+=1;
                                    if(update(x.toString().concat(",").concat(y.toString())))
                                    {
                                        y=y-1;
                                        break;
                                    }
                                }
                                console.log("x",x);
                                console.log("y",y);
                            }
                            if(swipeDirection=='left')
                            {
                                for(var k=0;k<3;k++)
                                {
                                    y-=1;
                                    if(update(x.toString().concat(",").concat(y.toString())))
                                    {
                                        y=y+1;
                                        break;
                                    }
                                }
                                console.log("x",x);
                                console.log("y",y);
                            }
                            if(swipeDirection=='up')
                            {
                                for(var k=0;k<3;k++)
                                {
                                    x-=1;
                                    if(update(x.toString().concat(",").concat(y.toString())))
                                    {
                                        x=x+1;
                                        break;
                                    }
                                }
                                console.log("x",x);
                                console.log("y",y);
                            }
                            if(swipeDirection=='down')
                            {
                                for(var k=0;k<3;k++)
                                {
                                    x+=1;
                                    if(update(x.toString().concat(",").concat(y.toString())))
                                    {
                                        x=x-1;
                                        break;
                                    }
                                }
                                console.log("x",x);
                                console.log("y",y);
                            }
                            fl=1;
                        }
                        if(list[i].gestures[j].type=="swipe")
                        {
                            //output.innerHTML="swipe";
                            //Classify swipe as either horizontal or vertical
                            var isHorizontal = Math.abs(list[i].gestures[j].direction[0]) > Math.abs(list[i].gestures[j].direction[1]);
                            //Classify as right-left or up-down
                            if(isHorizontal)
                            {
                                if(list[i].gestures[j].direction[0] > 0)
                                {
                                    swipeDirection = "right";
                                    y= y + 1;
                                    if(update(x.toString().concat(",").concat(y.toString())))
                                        y=y-1;
                                    console.log("x",x);
                                    console.log("y",y);
//                                    drawMaze(document.getElementById("rows").getAttribute("value"), document.getElementById("cols").getAttribute("value"),
//                                                                            function(el,x,y,i));
                                }
                                else
                                {
                                    swipeDirection = "left";
                                    y= y - 1;
                                    if(update(x.toString().concat(",").concat(y.toString())))
                                        y=y+1;
                                    console.log("x",x);
                                    console.log("y",y);
                                    //console.log(now);
                                    //now=new Date();
                                }
                            }
                            else
                            { //vertical
                                if(list[i].gestures[j].direction[1] > 0)
                                {
                                   swipeDirection = "up";
                                   x= x - 1;
                                    if(update(x.toString().concat(",").concat(y.toString())))
                                        x=x+1;
                                    console.log("x",x);
                                    console.log("y",y);
                                }
                                else
                                {
                                   swipeDirection = "down";
                                   x= x + 1;
                                    if(update(x.toString().concat(",").concat(y.toString())))
                                        x=x-1;
                                    console.log("x",x);
                                    console.log("y",y);
                                }
                            }
                            console.log(swipeDirection);
                            fl=1;
                            //console.log(path);
                            break;
                        }
                    if(fl)
                    {
                        break;
                    }
                    }
                list=[];
                }
        }

    });
    return grid;
}
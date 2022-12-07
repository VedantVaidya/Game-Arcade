document.onkeydown = function action(e) {
    if (e.key == "ArrowUp") {
        character = document.getElementById("character");
        character.classList.add("jump")
        setTimeout(removejump, 1010)
    }

    else if (e.key == "ArrowRight") {
        character = document.getElementById("character");
        charx = parseInt(window.getComputedStyle(character, null).getPropertyValue("left"));
        character.style.left = charx + 50 + "px"
    }

    else if (e.key == "ArrowLeft") {
        character = document.getElementById("character");
        charx = parseInt(window.getComputedStyle(character, null).getPropertyValue("left"));
        character.style.left = charx - 50 + "px"
    }
}

function removejump() {
    character = document.getElementById("character");
    character.classList.remove("jump")
}

setInterval(collision, 100);

var stopscore = false
function collision() {
    character = document.getElementById("character")
    gameover = document.getElementById("gameover")
    enemy = document.getElementById("enemy")

    charx = parseInt(window.getComputedStyle(character, null).getPropertyValue("left"));
    chary = parseInt(window.getComputedStyle(character, null).getPropertyValue("top"));

    enemyx = parseInt(window.getComputedStyle(enemy, null).getPropertyValue("left"));
    enemyy = parseInt(window.getComputedStyle(enemy, null).getPropertyValue("top"));

    distancex = enemyx - charx
    distancey = enemyy - chary

    if ((distancex < 50 && distancex > -50) && (distancey < 20 && distancey > -20)) {
        enemy.classList.remove("approach")
        document.getElementById("gameover").innerText = "Game Over"
        document.getElementById("gameover").style.visibility = "visible"
        stopscore = true
    }
}
var score = 1
setInterval(scorecounter, 5000);


function scorecounter() {
    if (stopscore == false) {
        score = score + 1
        document.getElementById("score").innerText = "Enemy Number: " + score
        document.getElementById("finalscore").value = score
    }
    
}


var enemycount = 2
setInterval(switchvillians, 4800);

function switchvillians(){
    if (enemycount == 1) {
        document.getElementById("ene").src = "/static/kevin.png";
        enemycount++
        
    }

    else if(enemycount == 2) {
        document.getElementById("ene").src = "/static/vilgax.png";
        enemycount++
    }

    else if(enemycount == 3) {
        document.getElementById("ene").src = "/static/greg.png";
        enemycount = 1

    }
    else if(enemycount == 3) {
        document.getElementById("ene").src = "/static/greg.png";
        enemycount = 1

    }

}
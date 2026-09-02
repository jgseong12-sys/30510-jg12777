import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="NEON DUEL",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    background: #000 !important;
    margin: 0 !important;
    padding: 0 !important;
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

iframe {
    border: 0 !important;
    width: 100% !important;
}
</style>
""", unsafe_allow_html=True)


GAME_HTML = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">

<style>
* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    padding: 0;
    background: #000;
    color: #fff;
    font-family: Arial, sans-serif;
    overflow: hidden;
}

#game {
    height: 900px;
    max-height: 100vh;
    min-height: 650px;
    position: relative;
    background:
        radial-gradient(circle at 50% 35%, #18182d, #05050b 55%, #000);
    outline: none;
}

/* =========================
   TOP HUD
========================= */

#top {
    height: 78px;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 8px 18px;

    background: #020207ee;
    z-index: 20;
}

.hud {
    width: 34%;
}

.right {
    text-align: right;
}

.center {
    width: 170px;
    text-align: center;
}

.tag {
    font-size: 12px;
    font-weight: bold;
    letter-spacing: 2px;

    border: 1px solid;
    padding: 4px 15px;

    border-radius: 5px;
}

.p2 {
    color: #ff38bd;
}

.p1 {
    color: #24eaff;
}

.score {
    font-size: 24px;
    font-weight: 900;
}

.combo {
    font-size: 10px;
    color: #aaa;
}

.combo b {
    font-size: 18px;
}

#clock {
    font-size: 23px;
    font-weight: 900;
    color: #fff;
}

#bar {
    height: 5px;
    background: #222;
    border-radius: 5px;
    overflow: hidden;
}

.fill {
    height: 100%;
    width: 0;
    background:
        linear-gradient(
            90deg,
            #ff38bd,
            #fff,
            #24eaff
        );
}

/* =========================
   BATTLE AREA
========================= */

#battle {
    position: absolute;

    top: 78px;
    bottom: 148px;
    left: 0;
    right: 0;

    display: flex;
    overflow: hidden;
}

.side {
    width: 50%;
    position: relative;
    overflow: hidden;
}

.side:first-child {
    border-right: 2px solid #ffffff44;
}

.track {
    position: absolute;
    inset: 0;

    clip-path:
        polygon(
            22% 0,
            78% 0,
            100% 100%,
            0 100%
        );

    background:
        linear-gradient(
            #120512,
            #020207
        );
}

.p1side .track {
    background:
        linear-gradient(
            #03131b,
            #020609
        );
}

.grid {
    position: absolute;
    inset: 0;

    clip-path:
        polygon(
            22% 0,
            78% 0,
            100% 100%,
            0 100%
        );
}

.v,
.h {
    position: absolute;
    background: #ffffff22;
}

.v {
    top: 0;
    bottom: 0;
    width: 1px;
}

.h {
    left: 0;
    right: 0;
    height: 1px;
}

.v0 {
    left: 22%;
}

.v1 {
    left: 36%;
}

.v2 {
    left: 50%;
}

.v3 {
    left: 64%;
}

.v4 {
    left: 78%;
}

.h1 {
    top: 25%;
}

.h2 {
    top: 50%;
}

.h3 {
    top: 75%;
}

.notes {
    position: absolute;
    inset: 0;
}

.judge {
    position: absolute;

    bottom: 65px;
    left: 0;
    right: 0;

    height: 5px;
    z-index: 10;
}

.p2side .judge {
    background: #ff38bd;
    box-shadow:
        0 0 16px #ff38bd;
}

.p1side .judge {
    background: #24eaff;
    box-shadow:
        0 0 16px #24eaff;
}

/* =========================
   NOTES
========================= */

.note {
    position: absolute;

    height: 43px;

    border: 2px solid currentColor;
    border-radius: 11px;

    background: #101018e8;

    display: flex;
    align-items: center;
    justify-content: center;

    box-shadow:
        0 0 9px currentColor,
        0 0 22px currentColor;

    z-index: 8;

    user-select: none;
}

.note .letter {
    font-size: 21px;
    font-weight: 900;
}

.note.hold .stem {
    position: absolute;

    left: 50%;
    bottom: 33px;

    transform: translateX(-50%);

    width: 35%;

    background: currentColor;
    border-radius: 6px;

    box-shadow:
        0 0 10px currentColor;
}

.note.active {
    background: #fff2;
}

.note.hit {
    opacity: 0;
    transform: scale(1.15);
    transition: .1s;
}

/* =========================
   VS
========================= */

#vs {
    position: absolute;

    z-index: 12;

    left: 50%;
    top: 45%;

    transform: translate(-50%, -50%);

    font-size: 27px;
    font-weight: 900;

    text-shadow:
        0 0 15px #fff;
}

/* =========================
   MESSAGES
========================= */

#messages {
    position: absolute;

    bottom: 145px;
    left: 0;
    right: 0;

    height: 65px;

    z-index: 30;

    pointer-events: none;
}

.msg {
    position: absolute;

    font-size: 28px;
    font-weight: 900;

    opacity: 0;

    text-shadow:
        0 0 12px currentColor;
}

.msg.p2m {
    left: 25%;
    transform: translateX(-50%);
}

.msg.p1m {
    left: 75%;
    transform: translateX(-50%);
}

.show {
    animation:
        pop .48s ease-out forwards;
}

@keyframes pop {

    0% {
        opacity: 0;
        transform:
            translate(-50%, 15px)
            scale(.7);
    }

    25% {
        opacity: 1;
        transform:
            translate(-50%, 0)
            scale(1.05);
    }

    100% {
        opacity: 0;
        transform:
            translate(-50%, -22px);
    }
}

.perfect {
    color: #fff;
}

.great {
    color: #69ff9e;
}

.miss {
    color: #ff5c7f;
}

.holdmsg {
    color: #ffe46a;
}

/* =========================
   KEYBOARD
========================= */

#keys {
    height: 96px;

    position: absolute;

    bottom: 52px;
    left: 0;
    right: 0;

    display: flex;

    background: #020207;

    z-index: 40;
}

.keypanel {
    width: 50%;

    display: flex;
    justify-content: center;
    align-items: center;

    gap: 8px;
}

.key {
    width: 63px;
    height: 63px;

    border: 2px solid currentColor;
    border-radius: 11px;

    display: flex;
    flex-direction: column;

    align-items: center;
    justify-content: center;

    background: #08080f;

    box-shadow:
        inset 0 0 10px currentColor;

    user-select: none;
}

.key.down {
    background: #fff;
    color: #000 !important;

    transform: scale(.92);
}

.key b {
    font-size: 24px;
}

.key small {
    font-size: 8px;
}

/* =========================
   SONG BAR
========================= */

#songs {
    position: absolute;

    bottom: 0;
    left: 0;
    right: 0;

    height: 52px;

    z-index: 50;

    display: flex;

    gap: 5px;

    align-items: center;

    padding: 4px;

    background: #05050bee;

    border-top: 1px solid #333;

    overflow-x: auto;
}

.song {
    height: 42px;
    min-width: 112px;

    background: #090912;
    color: #fff;

    border: 1px solid #444;
    border-radius: 7px;

    cursor: pointer;

    text-align: left;
}

.song.selected {
    border-color: #fff;

    box-shadow:
        0 0 12px #fff5;
}

.song b {
    font-size: 10px;
}

.song small {
    font-size: 8px;
    color: #aaa;
}

#start {
    margin-left: auto;

    height: 42px;

    padding: 0 17px;

    border: 0;
    border-radius: 8px;

    color: #fff;

    font-weight: 900;

    background:
        linear-gradient(
            90deg,
            #ff38bd,
            #24eaff
        );

    cursor: pointer;
}

/* =========================
   OVERLAY
========================= */

.overlay {
    position: absolute;

    inset: 0;

    z-index: 100;

    background: #000e;

    display: flex;

    align-items: center;
    justify-content: center;
}

.box {
    width: min(800px, 92%);

    padding: 28px;

    text-align: center;

    border: 1px solid #fff4;

    border-radius: 16px;

    background: #09090ff5;

    box-shadow:
        0 0 45px #7040ff55;
}

h1 {
    font-size: 44px;

    margin: 0;

    background:
        linear-gradient(
            90deg,
            #ff38bd,
            #fff,
            #24eaff
        );

    -webkit-background-clip: text;

    color: transparent;
}

.songgrid {
    display: flex;

    flex-wrap: wrap;

    justify-content: center;

    gap: 8px;

    margin: 18px 0;
}

.pick {
    width: 165px;

    padding: 10px;

    background: #090912;
    color: #fff;

    border: 1px solid #444;

    border-radius: 8px;

    cursor: pointer;
}

.pick.selected {
    border-color: #fff;

    box-shadow:
        0 0 12px #fff5;
}

.action {
    padding: 12px 35px;

    border: 0;
    border-radius: 8px;

    background:
        linear-gradient(
            90deg,
            #ff38bd,
            #24eaff
        );

    color: #fff;

    font-weight: 900;

    cursor: pointer;
}

/* =========================
   RESULT
========================= */

#result {
    display: none;
}

.winner {
    font-size: 38px;
    font-weight: 900;
}

.final {
    display: flex;

    justify-content: space-around;

    font-size: 22px;

    margin: 20px;
}

/* =========================
   START FOCUS
========================= */

#focusHint {
    margin-top: 12px;

    font-size: 11px;

    color: #777;
}
</style>
</head>

<body>

<div id="game" tabindex="0">

<!-- =========================
     TOP
========================= -->

<div id="top">

    <div class="hud p2">
        <span class="tag">PLAYER 2</span>

        <div class="score" id="score2">
            0
        </div>

        <div class="combo">
            COMBO
            <b id="combo2">0</b>
        </div>
    </div>


    <div class="center">

        <div id="clock">
            03:00
        </div>

        <div id="bar">
            <div
                class="fill"
                id="fill">
            </div>
        </div>

    </div>


    <div class="hud p1 right">

        <span class="tag">
            PLAYER 1
        </span>

        <div
            class="score"
            id="score1">
            0
        </div>

        <div class="combo">
            COMBO
            <b id="combo1">0</b>
        </div>

    </div>

</div>


<!-- =========================
     BATTLE
========================= -->

<div id="battle">

    <!-- PLAYER 2 -->

    <div
        class="side p2side"
        id="side2">

        <div class="track"></div>

        <div class="grid">

            <i class="v v0"></i>
            <i class="v v1"></i>
            <i class="v v2"></i>
            <i class="v v3"></i>
            <i class="v v4"></i>

            <i class="h h1"></i>
            <i class="h h2"></i>
            <i class="h h3"></i>

        </div>

        <div
            class="notes"
            id="notes2">
        </div>

        <div class="judge"></div>

    </div>


    <div id="vs">
        VS
    </div>


    <!-- PLAYER 1 -->

    <div
        class="side p1side"
        id="side1">

        <div class="track"></div>

        <div class="grid">

            <i class="v v0"></i>
            <i class="v v1"></i>
            <i class="v v2"></i>
            <i class="v v3"></i>
            <i class="v v4"></i>

            <i class="h h1"></i>
            <i class="h h2"></i>
            <i class="h h3"></i>

        </div>

        <div
            class="notes"
            id="notes1">
        </div>

        <div class="judge"></div>

    </div>

</div>


<!-- =========================
     JUDGEMENT
========================= -->

<div id="messages">

    <div
        id="message2"
        class="msg p2m">
    </div>

    <div
        id="message1"
        class="msg p1m">
    </div>

</div>


<!-- =========================
     KEYS
========================= -->

<div id="keys">

    <div class="keypanel p2">

        <div
            class="key"
            data-player="2"
            data-key="o">

            <b>O</b>
            <small>LEFT</small>

        </div>

        <div
            class="key"
            data-player="2"
            data-key="p">

            <b>P</b>
            <small>DOWN</small>

        </div>

        <div
            class="key"
            data-player="2"
            data-key="[" >

            <b>[</b>
            <small>UP</small>

        </div>

        <div
            class="key"
            data-player="2"
            data-key="]">

            <b>]</b>
            <small>RIGHT</small>

        </div>

    </div>


    <div class="keypanel p1">

        <div
            class="key"
            data-player="1"
            data-key="q">

            <b>Q</b>
            <small>LEFT</small>

        </div>

        <div
            class="key"
            data-player="1"
            data-key="w">

            <b>W</b>
            <small>DOWN</small>

        </div>

        <div
            class="key"
            data-player="1"
            data-key="e">

            <b>E</b>
            <small>UP</small>

        </div>

        <div
            class="key"
            data-player="1"
            data-key="r">

            <b>R</b>
            <small>RIGHT</small>

        </div>

    </div>

</div>


<!-- =========================
     SONGS
========================= -->

<div id="songs"></div>


<!-- =========================
     MENU
========================= -->

<div
    class="overlay"
    id="menu">

    <div class="box">

        <h1>
            NEON DUEL
        </h1>

        <p>
            1 VS 1 RHYTHM BATTLE
        </p>

        <div
            class="songgrid"
            id="songgrid">
        </div>

        <p style="color:#aaa">
            PLAYER 2 :
            O P [ ]
            &nbsp; | &nbsp;
            PLAYER 1 :
            Q W E R
        </p>

        <p
            style="
            font-size:12px;
            color:#888
            ">

            처음에는 한 개씩 천천히 내려오고,
            시간이 지나면 2~3개 동시 타일과
            HOLD가 등장합니다.

        </p>

        <button
            class="action"
            id="go">

            START BATTLE

        </button>

        <div id="focusHint">
            게임 시작 후 화면을 한 번 클릭하면
            키보드 입력이 활성화됩니다.
        </div>

    </div>

</div>


<!-- =========================
     RESULT
========================= -->

<div
    class="overlay"
    id="result">

    <div class="box">

        <div
            style="
            letter-spacing:3px
            ">

            BATTLE RESULT

        </div>

        <div
            class="winner"
            id="winner">
        </div>

        <div class="final">

            <div>
                PLAYER 2
                <br>
                <span id="final2">
                    0
                </span>
            </div>

            <div>
                PLAYER 1
                <br>
                <span id="final1">
                    0
                </span>
            </div>

        </div>

        <button
            class="action"
            id="again">

            BACK TO SONG SELECT

        </button>

    </div>

</div>


<script>
(function(){

"use strict";


/* =========================
   SONGS
========================= */

const songs = [

    ["NEON DREAM", 108, "★★★"],

    ["ELECTRIC SHOCK", 116, "★★★"],

    ["GALAXY RUSH", 124, "★★★★"],

    ["BLAZING SOUL", 132, "★★★★"],

    ["CYBER PUNK", 140, "★★★★★"],

    ["STARLIGHT", 102, "★★"],

    ["INFINITY", 128, "★★★★"],

    ["NIGHT DRIVE", 112, "★★★"]

];


const keys = {

    1: ["q", "w", "e", "r"],

    2: ["o", "p", "[", "]"]

};


const letters = {

    1: ["Q", "W", "E", "R"],

    2: ["O", "P", "[", "]"]

};


const colors = {

    1: [
        "#24eaff",
        "#28a9ff",
        "#a276ff",
        "#52ffb2"
    ],

    2: [
        "#ff38bd",
        "#ff557c",
        "#c96cff",
        "#ff72e9"
    ]

};


const duration = 180000;


let selected = 0;

let running = false;

let startTime = 0;

let lastTime = 0;

let spawnTimer = 0;

let animation = 0;


const player = {

    1: {
        score: 0,
        combo: 0,
        notes: [],
        holds: {}
    },

    2: {
        score: 0,
        combo: 0,
        notes: [],
        holds: {}
    }

};


/* =========================
   HELPER
========================= */

function $(id){

    return document.getElementById(id);

}


/* =========================
   SONG MENU
========================= */

function renderSongs(){

    const grid = $("songgrid");

    const bottom = $("songs");

    grid.innerHTML = "";

    bottom.innerHTML = "";


    songs.forEach(function(song, index){

        const a =
            document.createElement("button");

        a.className =
            "pick" +
            (index === selected
                ? " selected"
                : "");

        a.innerHTML =
            "<b>" +
            song[0] +
            "</b><br><small>BPM " +
            song[1] +
            " · " +
            song[2] +
            "</small>";


        a.onclick = function(){

            selected = index;

            renderSongs();

        };


        grid.appendChild(a);


        const b =
            document.createElement("button");

        b.className =
            "song" +
            (index === selected
                ? " selected"
                : "");

        b.innerHTML =
            "<b>" +
            song[0] +
            "</b><br><small>" +
            song[1] +
            " BPM</small>";


        b.onclick = function(){

            selected = index;

            renderSongs();

        };


        bottom.appendChild(b);

    });


    const start =
        document.createElement("button");

    start.id = "start";

    start.textContent = "START";

    start.onclick = startGame;

    bottom.appendChild(start);

}


/* =========================
   HUD
========================= */

function updateHUD(){

    $("score1").textContent =
        player[1].score.toLocaleString();

    $("score2").textContent =
        player[2].score.toLocaleString();

    $("combo1").textContent =
        player[1].combo;

    $("combo2").textContent =
        player[2].combo;

}


/* =========================
   MESSAGE
========================= */

function showMessage(p, text, cls){

    const el =
        $("message" + p);

    el.className =
        "msg " +
        (p === 1 ? "p1m" : "p2m") +
        " " +
        cls;

    el.textContent = text;

    void el.offsetWidth;

    el.classList.add("show");

}


/* =========================
   RESET
========================= */

function resetGame(){

    clearNotes();

    player[1].score = 0;
    player[1].combo = 0;

    player[1].notes = [];
    player[1].holds = {};

    player[2].score = 0;
    player[2].combo = 0;

    player[2].notes = [];
    player[2].holds = {};


    $("clock").textContent =
        "03:00";

    $("fill").style.width =
        "0%";

    updateHUD();

}


/* =========================
   CLEAR NOTES
========================= */

function clearNotes(){

    [1, 2].forEach(function(p){

        player[p].notes.forEach(
            function(n){

                if(n.parentNode){
                    n.parentNode.removeChild(n);
                }

            }
        );

        player[p].notes = [];

        player[p].holds = {};

    });

}


/* =========================
   DIFFICULTY
========================= */

function spawnInterval(elapsed){

    const progress =
        Math.min(
            elapsed / duration,
            1
        );

    const bpm =
        songs[selected][1];


    return Math.max(
        430,
        60000 /
        (
            bpm *
            (
                0.68 +
                progress * 0.50
            )
        )
    );

}


function travelTime(elapsed){

    const progress =
        Math.min(
            elapsed / duration,
            1
        );


    return (
        1600 -
        progress * 250
    );

}


/* =========================
   CREATE NOTE
========================= */

function spawnNote(
    p,
    lane,
    hold,
    travel
){

    const note =
        document.createElement("div");

    note.className =
        "note" +
        (hold ? " hold" : "");


    note.style.color =
        colors[p][lane];


    note.dataset.key =
        keys[p][lane];

    note.dataset.lane =
        lane;

    note.dataset.spawn =
        performance.now();

    note.dataset.travel =
        travel;

    note.dataset.hold =
        hold ? "1" : "0";


    if(hold){

        const length =
            100 +
            Math.random() * 130;

        note.dataset.length =
            length;


        note.innerHTML =
            '<div class="stem" style="height:' +
            length +
            'px"></div>' +
            '<div class="letter">' +
            letters[p][lane] +
            "</div>";

    }
    else{

        note.innerHTML =
            '<div class="letter">' +
            letters[p][lane] +
            "</div>";

    }


    $("notes" + p)
        .appendChild(note);


    player[p].notes.push(note);

}


/* =========================
   PATTERN
========================= */

function createPattern(elapsed){

    const progress =
        Math.min(
            elapsed / duration,
            1
        );


    let count = 1;


    if(
        progress > 0.30 &&
        Math.random() <
        (progress - 0.30) * 1.15
    ){

        count = 2;

    }


    if(
        progress > 0.65 &&
        Math.random() <
        (progress - 0.65) * 0.9
    ){

        count = 3;

    }


    for(
        let p = 1;
        p <= 2;
        p++
    ){

        const used = [];


        for(
            let i = 0;
            i < count;
            i++
        ){

            let lane =
                Math.floor(
                    Math.random() * 4
                );


            let guard = 0;


            while(
                used.indexOf(lane) !== -1 &&
                guard < 20
            ){

                lane =
                    Math.floor(
                        Math.random() * 4
                    );

                guard++;

            }


            used.push(lane);


            const hold =
                Math.random() <
                (
                    0.02 +
                    progress * 0.13
                );


            spawnNote(
                p,
                lane,
                hold,
                travelTime(elapsed)
            );

        }

    }

}


/* =========================
   PERSPECTIVE
========================= */

function geometry(
    side,
    t,
    lane
){

    const left =
        0.22 * (1 - t);

    const right =
        1 - left;


    const x =
        left +
        (right - left) *
        (lane + 0.5) / 4;


    const width =
        (right - left) / 4;


    return {

        x:
            x *
            side.clientWidth,

        w:
            width *
            side.clientWidth

    };

}


/* =========================
   REMOVE NOTE
========================= */

function removeNote(p, n){

    n.classList.add("hit");

    setTimeout(
        function(){

            if(n.parentNode){
                n.parentNode.removeChild(n);
            }

        },
        110
    );


    player[p].notes =
        player[p].notes.filter(
            function(x){
                return x !== n;
            }
        );

}


/* =========================
   MISS
========================= */

function registerMiss(p, n){

    player[p].combo = 0;

    player[p].score =
        Math.max(
            0,
            player[p].score - 20
        );


    showMessage(
        p,
        "MISS",
        "miss"
    );


    removeNote(p, n);

    updateHUD();

}


/* =========================
   HOLD FINISH
========================= */

function finishHold(p, n){

    if(
        !n ||
        !n.isConnected
    ){
        return;
    }


    delete player[p].holds[
        n.dataset.key
    ];


    player[p].combo++;


    player[p].score +=
        120 +
        Math.min(
            180,
            player[p].combo * 2
        );


    showMessage(
        p,
        "GREAT",
        "holdmsg"
    );


    removeNote(p, n);

    updateHUD();

}


/* =========================
   NOTE UPDATE
========================= */

function updateNotes(now){

    [1, 2].forEach(function(p){

        const side =
            $("side" + p);

        const height =
            side.clientHeight;

        const judgeY =
            height - 65;


        player[p].notes
            .slice()
            .forEach(function(n){

                if(!n.isConnected){
                    return;
                }


                const progress =
                    (
                        now -
                        Number(n.dataset.spawn)
                    ) /
                    Number(n.dataset.travel);


                const t =
                    Math.max(
                        0,
                        Math.min(1, progress)
                    );


                const g =
                    geometry(
                        side,
                        t,
                        Number(n.dataset.lane)
                    );


                const y =
                    -55 +
                    progress *
                    (height + 100);


                n.style.top =
                    y + "px";


                n.style.left =
                    (
                        g.x -
                        g.w * 0.44
                    ) + "px";


                n.style.width =
                    Math.max(
                        30,
                        g.w * 0.88
                    ) + "px";


                if(
                    n.dataset.active === "1"
                ){

                    if(
                        y -
                        Number(n.dataset.length)
                        >=
                        judgeY
                    ){

                        finishHold(p, n);

                    }

                }
                else if(
                    y >= judgeY + 50
                ){

                    registerMiss(p, n);

                }

            });

    });

}


/* =========================
   FIND NOTE
========================= */

function findNote(p, key){

    const side =
        $("side" + p);

    const judgeY =
        side.clientHeight - 65;


    let best = null;

    let distance = 99999;


    player[p].notes.forEach(
        function(n){

            if(!n.isConnected){
                return;
            }

            if(
                n.dataset.key !== key
            ){
                return;
            }

            if(
                n.dataset.active === "1"
            ){
                return;
            }


            const r =
                n.getBoundingClientRect();

            const sr =
                side.getBoundingClientRect();


            const y =
                r.top -
                sr.top +
                r.height / 2;


            const d =
                Math.abs(
                    y - judgeY
                );


            if(d < distance){

                distance = d;

                best = n;

            }

        }
    );


    return {
        note: best,
        distance: distance
    };

}


/* =========================
   HIT
========================= */

function hit(p, key){

    const found =
        findNote(p, key);


    if(
        !found.note ||
        found.distance > 48
    ){

        return;

    }


    const n =
        found.note;


    /* HOLD */

    if(
        n.dataset.hold === "1"
    ){

        n.dataset.active = "1";

        n.classList.add("active");


        player[p].holds[key] = n;


        player[p].combo++;


        player[p].score +=
            100 +
            Math.min(
                150,
                player[p].combo * 2
            );


        showMessage(
            p,
            "PERFECT",
            "perfect"
        );


        updateHUD();

        return;

    }


    /* NORMAL */

    const perfect =
        found.distance <= 22;


    player[p].combo++;


    player[p].score +=
        (
            perfect
            ? 100
            : 60
        ) +
        Math.min(
            150,
            player[p].combo * 2
        );


    showMessage(
        p,
        perfect
        ? "PERFECT"
        : "GREAT",
        perfect
        ? "perfect"
        : "great"
    );


    removeNote(p, n);

    updateHUD();

}


/* =========================
   KEY RELEASE
========================= */

function release(p, key){

    const n =
        player[p].holds[key];


    if(!n){
        return;
    }


    const side =
        $("side" + p);

    const judgeY =
        side.clientHeight - 65;


    const r =
        n.getBoundingClientRect();

    const sr =
        side.getBoundingClientRect();


    const y =
        r.top -
        sr.top +
        r.height / 2;


    if(
        y -
        Number(n.dataset.length)
        >=
        judgeY
    ){

        finishHold(p, n);

    }
    else{

        player[p].combo = 0;


        showMessage(
            p,
            "MISS",
            "miss"
        );


        removeNote(p, n);

        updateHUD();

    }


    delete player[p].holds[key];

}


/* =========================
   GAME LOOP
========================= */

function gameLoop(now){

    if(!running){
        return;
    }


    const elapsed =
        now - startTime;


    const remain =
        Math.max(
            0,
            duration - elapsed
        );


    const seconds =
        Math.ceil(
            remain / 1000
        );


    $("clock").textContent =
        String(
            Math.floor(seconds / 60)
        ).padStart(2, "0")
        +
        ":"
        +
        String(
            seconds % 60
        ).padStart(2, "0");


    $("fill").style.width =
        Math.min(
            100,
            elapsed / duration * 100
        ) +
        "%";


    if(lastTime){

        spawnTimer +=
            now - lastTime;

    }
    else{

        spawnTimer = 0;

    }


    if(
        spawnTimer >=
        spawnInterval(elapsed)
    ){

        spawnTimer = 0;

        createPattern(elapsed);

    }


    updateNotes(now);


    lastTime = now;


    if(
        elapsed >= duration
    ){

        finishGame();

        return;

    }


    animation =
        requestAnimationFrame(
            gameLoop
        );

}


/* =========================
   START
========================= */

function startGame(){

    $("menu").style.display =
        "none";

    $("result").style.display =
        "none";


    resetGame();


    running = true;

    startTime =
        performance.now();

    lastTime = 0;

    spawnTimer = 0;


    $("game").focus();


    animation =
        requestAnimationFrame(
            gameLoop
        );

}


/* =========================
   FINISH
========================= */

function finishGame(){

    running = false;


    cancelAnimationFrame(
        animation
    );


    clearNotes();


    $("final1").textContent =
        player[1].score.toLocaleString();

    $("final2").textContent =
        player[2].score.toLocaleString();


    const winner =
        $("winner");


    if(
        player[1].score >
        player[2].score
    ){

        winner.textContent =
            "PLAYER 1 WINS!";

        winner.style.color =
            "#24eaff";

    }
    else if(
        player[2].score >
        player[1].score
    ){

        winner.textContent =
            "PLAYER 2 WINS!";

        winner.style.color =
            "#ff38bd";

    }
    else{

        winner.textContent =
            "DRAW!";

        winner.style.color =
            "#fff";

    }


    $("result").style.display =
        "flex";

}


/* =========================
   KEYBOARD DOWN
========================= */

document.addEventListener(
    "keydown",
    function(e){

        const key =
            e.key.toLowerCase();


        let p = 0;


        if(
            keys[1].indexOf(key) !== -1
        ){

            p = 1;

        }
        else if(
            keys[2].indexOf(key) !== -1
        ){

            p = 2;

        }


        if(!p){
            return;
        }


        e.preventDefault();


        const button =
            document.querySelector(
                '.key[data-player="' +
                p +
                '"][data-key="' +
                CSS.escape(key) +
                '"]'
            );


        if(button){

            button.classList.add(
                "down"
            );

        }


        if(running){

            hit(
                p,
                key
            );

        }

    }
);


/* =========================
   KEYBOARD UP
========================= */

document.addEventListener(
    "keyup",
    function(e){

        const key =
            e.key.toLowerCase();


        let p = 0;


        if(
            keys[1].indexOf(key) !== -1
        ){

            p = 1;

        }
        else if(
            keys[2].indexOf(key) !== -1
        ){

            p = 2;

        }


        if(!p){
            return;
        }


        e.preventDefault();


        const button =
            document.querySelector(
                '.key[data-player="' +
                p +
                '"][data-key="' +
                CSS.escape(key) +
                '"]'
            );


        if(button){

            button.classList.remove(
                "down"
            );

        }


        if(running){

            release(
                p,
                key
            );

        }

    }
);


/* =========================
   FOCUS
========================= */

$("game").addEventListener(
    "click",
    function(){

        this.focus();

    }
);


$("go").onclick =
    startGame;


$("again").onclick =
    function(){

        $("result").style.display =
            "none";

        $("menu").style.display =
            "flex";

        renderSongs();

    };


renderSongs();

updateHUD();

})();
</script>

</body>
</html>
"""


components.html(
    GAME_HTML,
    height=900,
    scrolling=False
)

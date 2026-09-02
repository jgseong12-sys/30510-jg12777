import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="NEON DUEL - 1 VS 1 Rhythm",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
        background: #000 !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"],
    [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
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

html = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
*{box-sizing:border-box}
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#000;font-family:Arial,sans-serif;color:#fff}
button{font-family:inherit}
#app{height:100vh;min-height:680px;background:
 radial-gradient(circle at 50% 35%,#14142b 0,#050510 32%,#000 72%);
 position:relative;overflow:hidden;outline:none}
#stars{position:absolute;inset:0;pointer-events:none;opacity:.45;
 background-image:radial-gradient(#fff 1px,transparent 1px);
 background-size:42px 42px;animation:stars 8s linear infinite}
@keyframes stars{to{background-position:42px 84px}}
#top{height:92px;display:flex;align-items:center;justify-content:space-between;
 padding:12px 22px;position:relative;z-index:20}
.playerHud{width:28%;min-width:230px}
.p2{text-align:left}.p1{text-align:right}
.tag{display:inline-block;padding:6px 26px;border:1px solid;border-radius:4px;
 font-weight:900;letter-spacing:2px;background:#090912}
.p2 .tag{color:#ff36bb;border-color:#ff36bb;box-shadow:0 0 14px #ff36bb66}
.p1 .tag{color:#24dfff;border-color:#24dfff;box-shadow:0 0 14px #24dfff66}
.score{font-size:31px;font-weight:900;margin-top:3px;text-shadow:0 0 12px currentColor}
.p2 .score{color:#ff66c9}.p1 .score{color:#5be9ff}
.combo{font-size:15px;font-weight:900;letter-spacing:2px}
.combo b{font-size:26px;display:block;line-height:24px}
.p2 .combo{color:#ff66c9}.p1 .combo{color:#5be9ff}
#timer{text-align:center;width:170px}
#timeLabel{font-size:12px;font-weight:bold;color:#ddd;letter-spacing:2px}
#clock{font-size:29px;font-weight:900;margin-top:2px}
#progress{height:7px;background:#181824;border:1px solid #333;border-radius:10px;overflow:hidden}
#progressFill{height:100%;width:0;background:linear-gradient(90deg,#ff2fb7,#fff,#16dfff);
 box-shadow:0 0 15px #fff}

#battle{position:absolute;left:0;right:0;top:92px;bottom:175px;display:flex;gap:0}
.side{width:50%;position:relative;overflow:hidden}
.side.p2side{border-right:2px solid #fff5}
.side:before{content:"";position:absolute;inset:0;
 background:linear-gradient(90deg,transparent 0 12%,#ff36bb22 12% 12.4%,transparent 12.4% 37.4%,#ff36bb18 37.4% 37.8%,transparent 37.8% 62.8%,#ff36bb18 62.8% 63.2%,transparent 63.2% 87.8%,#ff36bb22 87.8% 88.2%,transparent 88.2%);
 pointer-events:none}
.p1side:before{filter:hue-rotate(130deg)}
.lane{position:absolute;top:0;bottom:0;width:25%;border-left:1px solid #fff1;border-right:1px solid #fff1}
.l0{left:0}.l1{left:25%}.l2{left:50%}.l3{left:75%}
.judgeLine{position:absolute;left:2%;right:2%;bottom:104px;height:5px;border-radius:8px;
 box-shadow:0 0 8px currentColor,0 0 22px currentColor;z-index:5}
.p2side .judgeLine{color:#ff27ba;background:#ff27ba}.p1side .judgeLine{color:#1eeaff;background:#1eeaff}
.notes{position:absolute;inset:0;z-index:4}
.note{position:absolute;width:22%;height:54px;border-radius:12px;
 border:3px solid currentColor;background:linear-gradient(180deg,#fff7,#fff1 25%,#080815cc);
 box-shadow:0 0 7px currentColor,0 0 22px currentColor,inset 0 0 12px currentColor;
 transform:translateY(0);z-index:4}
.note .arrow{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
 font-size:28px;font-weight:900;text-shadow:0 0 10px currentColor}
.note.hold{height:54px}
.note.hold .body{position:absolute;left:50%;transform:translateX(-50%);bottom:48px;width:50%;
 background:currentColor;box-shadow:0 0 12px currentColor;border-radius:8px 8px 2px 2px}
.note.hold .body:after{content:"HOLD";position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-90deg);
 font-size:10px;color:#fff;font-weight:900;opacity:.9}
.note.hit{animation:hit .13s ease-out forwards}
@keyframes hit{to{opacity:0;transform:scale(1.25)}}
#centerVS{position:absolute;left:50%;top:0;bottom:0;transform:translateX(-50%);width:4px;
 background:linear-gradient(#ff2bb800,#fff,#19eaff00);z-index:15}
#vs{position:absolute;top:40%;left:50%;transform:translate(-50%,-50%);font-size:35px;font-weight:900;
 text-shadow:0 0 12px #fff,0 0 35px #7cf}
#judgements{position:absolute;left:0;right:0;bottom:210px;height:80px;pointer-events:none;z-index:30}
.jmsg{position:absolute;font-size:31px;font-weight:1000;opacity:0;text-shadow:0 0 12px currentColor,0 0 30px currentColor}
.jmsg.p2msg{left:25%;transform:translateX(-50%)}.jmsg.p1msg{left:75%;transform:translateX(-50%)}
.jmsg.show{animation:judge .48s ease-out forwards}
@keyframes judge{0%{opacity:0;transform:translate(-50%,20px) scale(.7)}25%{opacity:1;transform:translate(-50%,0) scale(1.08)}100%{opacity:0;transform:translate(-50%,-24px) scale(1)}}
.perfect{color:#fff}.great{color:#64ff9a}.miss{color:#ff527d}

#keys{position:absolute;bottom:67px;left:0;right:0;height:105px;display:flex;z-index:25}
.keyPanel{width:50%;display:flex;justify-content:center;gap:10px;align-items:center}
.key{width:72px;height:72px;border:2px solid;border-radius:13px;background:#07070e;
 display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:900;
 box-shadow:inset 0 0 12px currentColor,0 0 12px #000;transition:.06s;user-select:none}
.key small{font-size:11px;opacity:.8;margin-top:3px}
.p2keys .key{color:#ff36bb}.p1keys .key{color:#24dfff}
.key.down{transform:translateY(4px) scale(.94);background:#fff;color:#000 !important;box-shadow:0 0 25px currentColor}
.icon{font-size:29px;line-height:28px}

#songbar{position:absolute;bottom:0;left:0;right:0;height:67px;background:#05050cdd;border-top:1px solid #333;
 display:flex;align-items:center;padding:7px 14px;gap:8px;z-index:50}
.song{height:52px;min-width:145px;padding:7px 13px;border:1px solid #333;background:#090912;border-radius:8px;
 color:#fff;text-align:left;cursor:pointer;transition:.15s}
.song:hover{transform:translateY(-2px);border-color:#fff}
.song.selected{border-color:#fff;box-shadow:0 0 13px currentColor}
.song .name{font-weight:900;font-size:13px}.song .meta{font-size:10px;color:#aaa;margin-top:4px}
#start{margin-left:auto;height:52px;padding:0 24px;border:0;border-radius:9px;
 background:linear-gradient(90deg,#ff29b8,#7d4dff,#19dfff);color:white;font-weight:1000;font-size:16px;
 cursor:pointer;box-shadow:0 0 20px #6f3dff88}
#start:hover{filter:brightness(1.25)}
#overlay{position:absolute;inset:0;background:#000e;z-index:100;display:flex;align-items:center;justify-content:center}
#menu{width:min(820px,90%);padding:30px;border:1px solid #fff4;border-radius:18px;
 background:radial-gradient(circle at 50% 0,#17132a,#05050a 70%);box-shadow:0 0 50px #6e34ff33;text-align:center}
#menu h1{font-size:46px;margin:0 0 8px;background:linear-gradient(90deg,#ff2fb7,#fff,#1de9ff);
 -webkit-background-clip:text;color:transparent}
#menu p{color:#aaa;margin:8px}
.songGrid{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin:22px 0}
.pick{min-width:180px;padding:13px;border:1px solid #444;border-radius:10px;background:#0a0a12;color:#fff;cursor:pointer}
.pick.sel{border-color:#fff;box-shadow:0 0 16px #fff4}
#go{padding:14px 45px;border:0;border-radius:10px;background:linear-gradient(90deg,#ff25b4,#24ddff);
 color:#fff;font-weight:1000;font-size:18px;cursor:pointer}
#result{display:none;position:absolute;inset:0;background:#000e;z-index:110;align-items:center;justify-content:center}
.resultBox{width:500px;max-width:90%;padding:35px;text-align:center;border:1px solid #fff5;border-radius:18px;background:#080810}
#winner{font-size:43px;font-weight:1000;text-shadow:0 0 20px currentColor}
.finalScores{display:flex;justify-content:space-around;margin:22px;font-size:25px;font-weight:900}
#again{padding:12px 30px;border:0;border-radius:9px;background:#fff;color:#000;font-weight:900;cursor:pointer}

@media(max-height:760px){
 #top{height:76px}.battle{top:76px}.side .judgeLine{bottom:82px}
 #battle{top:76px;bottom:157px}#keys{bottom:55px;height:92px}.key{width:58px;height:58px}
 #songbar{height:55px}.song{height:43px;min-width:125px}.song .meta{display:none}
}
</style>
</head>
<body>
<div id="app" tabindex="0">
<div id="stars"></div>

<div id="top">
  <div class="playerHud p2">
    <div class="tag">PLAYER 2</div>
    <div class="score" id="score2">000,000</div>
    <div class="combo">COMBO <b id="combo2">0</b></div>
  </div>
  <div id="timer">
    <div id="timeLabel">TIME</div>
    <div id="clock">03:00</div>
    <div id="progress"><div id="progressFill"></div></div>
  </div>
  <div class="playerHud p1">
    <div class="tag">PLAYER 1</div>
    <div class="score" id="score1">000,000</div>
    <div class="combo">COMBO <b id="combo1">0</b></div>
  </div>
</div>

<div id="battle">
  <div class="side p2side" id="side2">
    <div class="lane l0"></div><div class="lane l1"></div><div class="lane l2"></div><div class="lane l3"></div>
    <div class="notes" id="notes2"></div><div class="judgeLine"></div>
  </div>
  <div id="centerVS"><div id="vs">VS</div></div>
  <div class="side p1side" id="side1">
    <div class="lane l0"></div><div class="lane l1"></div><div class="lane l2"></div><div class="lane l3"></div>
    <div class="notes" id="notes1"></div><div class="judgeLine"></div>
  </div>
</div>

<div id="judgements">
 <div id="j2" class="jmsg p2msg"></div>
 <div id="j1" class="jmsg p1msg"></div>
</div>

<div id="keys">
 <div class="keyPanel p2keys">
   <div class="key" data-player="2" data-key="ArrowLeft"><div class="icon">←</div><small>LEFT</small></div>
   <div class="key" data-player="2" data-key="ArrowDown"><div class="icon">↓</div><small>DOWN</small></div>
   <div class="key" data-player="2" data-key="ArrowUp"><div class="icon">↑</div><small>UP</small></div>
   <div class="key" data-player="2" data-key="ArrowRight"><div class="icon">→</div><small>RIGHT</small></div>
 </div>
 <div class="keyPanel p1keys">
   <div class="key" data-player="1" data-key="a"><div class="icon">A</div><small>LEFT</small></div>
   <div class="key" data-player="1" data-key="s"><div class="icon">S</div><small>DOWN</small></div>
   <div class="key" data-player="1" data-key="w"><div class="icon">W</div><small>UP</small></div>
   <div class="key" data-player="1" data-key="d"><div class="icon">D</div><small>RIGHT</small></div>
 </div>
</div>

<div id="songbar"></div>

<div id="overlay">
 <div id="menu">
   <h1>NEON DUEL</h1>
   <p>1 VS 1 RHYTHM BATTLE</p>
   <div class="songGrid" id="songGrid"></div>
   <p>PLAYER 2: ← ↓ ↑ → &nbsp;&nbsp; | &nbsp;&nbsp; PLAYER 1: A S W D</p>
   <p style="font-size:12px">타일이 판정선에 닿는 순간 해당 키를 누르세요. 긴 타일은 끝까지 누르고 있으세요.</p>
   <button id="go">START BATTLE</button>
 </div>
</div>

<div id="result">
 <div class="resultBox">
   <div style="font-size:15px;letter-spacing:3px">BATTLE RESULT</div>
   <div id="winner">PLAYER 1 WINS!</div>
   <div class="finalScores">
     <div>PLAYER 2<br><span id="final2">0</span></div>
     <div>PLAYER 1<br><span id="final1">0</span></div>
   </div>
   <button id="again">BACK TO SONG SELECT</button>
 </div>
</div>
</div>

<script>
const songs = [
 {name:"NEON DREAM", bpm:128, diff:"★★★", color:"#ff36bb"},
 {name:"ELECTRIC SHOCK", bpm:142, diff:"★★★★", color:"#24dfff"},
 {name:"GALAXY RUSH", bpm:150, diff:"★★★★", color:"#8b6cff"},
 {name:"BLAZING SOUL", bpm:160, diff:"★★★★★", color:"#ff704d"},
 {name:"CYBER PUNK", bpm:170, diff:"★★★★★", color:"#42ff9c"},
 {name:"STARLIGHT", bpm:120, diff:"★★", color:"#f6e66b"},
 {name:"INFINITY", bpm:155, diff:"★★★★★", color:"#c66cff"},
 {name:"NIGHT DRIVE", bpm:138, diff:"★★★", color:"#5ee7ff"}
];

let selected=0, playing=false, startTime=0, lastFrame=0, spawnAcc=0, raf=0;
const DURATION=180000;
const lanes2=["ArrowLeft","ArrowDown","ArrowUp","ArrowRight"];
const lanes1=["a","s","w","d"];
const state={
  1:{score:0,combo:0,held:{},notes:[]},
  2:{score:0,combo:0,held:{},notes:[]}
};

const songGrid=document.getElementById("songGrid");
const songbar=document.getElementById("songbar");

function buildSongs(){
 songGrid.innerHTML="";
 songbar.innerHTML="";
 songs.forEach((s,i)=>{
   const b=document.createElement("button");
   b.className="pick"+(i===selected?" sel":"");
   b.innerHTML=`<b>${s.name}</b><br><small>BPM ${s.bpm} · ${s.diff}</small>`;
   b.onclick=()=>{selected=i;buildSongs()};
   songGrid.appendChild(b);

   const c=document.createElement("button");
   c.className="song"+(i===selected?" selected":"");
   c.style.color=s.color;
   c.innerHTML=`<div class="name">${s.name}</div><div class="meta">BPM ${s.bpm} · 03:00</div>`;
   c.onclick=()=>{selected=i;buildSongs(); if(playing) restart()};
   songbar.appendChild(c);
 });
}
buildSongs();

function fmt(n){return Math.floor(n).toLocaleString("en-US").padStart(7,"0")}
function updateHud(){
 document.getElementById("score1").textContent=fmt(state[1].score);
 document.getElementById("score2").textContent=fmt(state[2].score);
 document.getElementById("combo1").textContent=state[1].combo;
 document.getElementById("combo2").textContent=state[2].combo;
}
function showJudge(p,text,cls){
 const el=document.getElementById("j"+p);
 el.className="jmsg p"+p+"msg "+cls;
 el.textContent=text;
 void el.offsetWidth;
 el.classList.add("show");
}

function noteSpeed(elapsed){
 // starts moderately fast and becomes harder throughout the 3 minute song
 const t=Math.min(elapsed/DURATION,1);
 return 330 + t*470;
}
function spawnInterval(elapsed){
 const bpm=songs[selected].bpm;
 const t=Math.min(elapsed/DURATION,1);
 // more notes as time progresses
 return Math.max(155, 60000/(bpm*(1.35+t*1.25)));
}
function laneX(lane){return lane*25+1.5}

function spawnNote(p, lane, hold, travel){
 const side=document.getElementById("notes"+p);
 const el=document.createElement("div");
 const neon = p===1 ? ["#24dfff","#00aaff","#8e7dff","#45ffb0"][lane]
                      : ["#ff36bb","#ff4f76","#c86cff","#ff63e8"][lane];
 el.className="note"+(hold?" hold":"");
 el.style.left=laneX(lane)+"%";
 el.style.color=neon;
 el.dataset.key=(p===1?lanes1:lanes2)[lane];
 el.dataset.player=p;
 el.dataset.hold=hold?"1":"0";
 el.dataset.spawn=performance.now();
 el.dataset.travel=travel;
 el.innerHTML=`<div class="arrow">${p===1?["←","↓","↑","→"][lane]:["←","↓","↑","→"][lane]}</div>`;
 if(hold){
   const len=70+Math.random()*190;
   const body=document.createElement("div");
   body.className="body"; body.style.height=len+"px";
   el.appendChild(body);
   el.dataset.length=len;
 }
 side.appendChild(el);
 state[p].notes.push(el);
}

function maybeSpawn(elapsed){
 const speed=noteSpeed(elapsed);
 const interval=spawnInterval(elapsed);
 spawnAcc += (lastFrame? performance.now()-lastFrame:16);
 if(spawnAcc<interval)return;
 spawnAcc=0;

 // Both players receive a synchronized rhythm pattern, but lanes differ.
 const simultaneous=Math.random() < (0.08 + Math.min(elapsed/DURATION,.8)*.22);
 const count=1 + (Math.random()<0.22+elapsed/DURATION*.25 ? 1:0);
 for(let p=1;p<=2;p++){
   const chosen=[];
   for(let k=0;k<count;k++){
     let lane=Math.floor(Math.random()*4);
     while(chosen.includes(lane) && chosen.length<4) lane=Math.floor(Math.random()*4);
     chosen.push(lane);
     const hold=Math.random() < 0.08 + Math.min(elapsed/DURATION,.8)*0.13;
     spawnNote(p,lane,hold,Math.max(620, speed*1.7));
     if(!simultaneous && p===1) break;
   }
 }
}

function judge(p, el, heldRelease=false){
 if(!el)return;
 const side=document.getElementById("side"+p);
 const lineY=side.clientHeight-104;
 const rect=el.getBoundingClientRect();
 const sideRect=side.getBoundingClientRect();
 const y=rect.top-sideRect.top+rect.height/2;
 const diff=Math.abs(y-lineY);
 let result, points;
 if(diff<=22){result="PERFECT";points=100}
 else if(diff<=48){result="GREAT";points=60}
 else {return false}
 state[p].combo++;
 points += Math.min(150, state[p].combo*2);
 state[p].score += points;
 showJudge(p,result,result==="PERFECT"?"perfect":"great");
 el.classList.add("hit");
 setTimeout(()=>el.remove(),130);
 const idx=state[p].notes.indexOf(el);
 if(idx>=0)state[p].notes.splice(idx,1);
 updateHud();
 return true;
}

function miss(p,el){
 state[p].combo=0;
 state[p].score=Math.max(0,state[p].score-25);
 showJudge(p,"MISS","miss");
 el.remove();
 const idx=state[p].notes.indexOf(el);
 if(idx>=0)state[p].notes.splice(idx,1);
 updateHud();
}

function updateNotes(now){
 for(let p=1;p<=2;p++){
   const side=document.getElementById("side"+p);
   const sr=side.getBoundingClientRect();
   for(const el of [...state[p].notes]){
     if(!el.isConnected)continue;
     const spawn=Number(el.dataset.spawn);
     const travel=Number(el.dataset.travel);
     const progress=(now-spawn)/travel;
     const y=-70 + progress*(side.clientHeight-30);
     el.style.top=y+"px";
     // A hold note visually stretches upward from its hit point.
     if(el.dataset.hold==="1"){
       const body=el.querySelector(".body");
       body.style.bottom=(el.offsetHeight-3)+"px";
     }
     if(y > side.clientHeight-55){
       miss(p,el);
     }
   }
 }
}

function gameLoop(now){
 if(!playing)return;
 const elapsed=now-startTime;
 const remain=Math.max(0,DURATION-elapsed);
 const sec=Math.ceil(remain/1000);
 document.getElementById("clock").textContent=
   String(Math.floor(sec/60)).padStart(2,"0")+":"+String(sec%60).padStart(2,"0");
 document.getElementById("progressFill").style.width=(elapsed/DURATION*100)+"%";

 maybeSpawn(elapsed);
 updateNotes(now);
 lastFrame=now;

 if(elapsed>=DURATION){
   finish();
   return;
 }
 raf=requestAnimationFrame(gameLoop);
}

function clearNotes(){
 for(let p=1;p<=2;p++){
   state[p].notes.forEach(n=>n.remove());
   state[p].notes=[];
   state[p].held={};
 }
}
function resetState(){
 state[1].score=0;state[1].combo=0;state[1].held={};
 state[2].score=0;state[2].combo=0;state[2].held={};
 updateHud();
}
function startGame(){
 document.getElementById("overlay").style.display="none";
 document.getElementById("result").style.display="none";
 resetState();clearNotes();
 playing=true;startTime=performance.now();lastFrame=0;spawnAcc=0;
 document.getElementById("app").focus();
 raf=requestAnimationFrame(gameLoop);
}
function restart(){startGame()}

function finish(){
 playing=false;
 cancelAnimationFrame(raf);
 clearNotes();
 const s1=state[1].score,s2=state[2].score;
 document.getElementById("final1").textContent=s1.toLocaleString();
 document.getElementById("final2").textContent=s2.toLocaleString();
 const w=document.getElementById("winner");
 if(s1>s2){w.textContent="PLAYER 1 WINS!";w.style.color="#24dfff"}
 else if(s2>s1){w.textContent="PLAYER 2 WINS!";w.style.color="#ff36bb"}
 else{w.textContent="DRAW!";w.style.color="#fff"}
 document.getElementById("result").style.display="flex";
}

document.getElementById("go").onclick=startGame;
document.getElementById("again").onclick=()=>{
 document.getElementById("result").style.display="none";
 document.getElementById("overlay").style.display="flex";
};

function keyName(e){return e.key.length===1?e.key.toLowerCase():e.key}

document.addEventListener("keydown",e=>{
 const k=keyName(e);
 let p=null;
 if(lanes1.includes(k))p=1;
 if(lanes2.includes(k))p=2;
 if(!p)return;
 e.preventDefault();

 const keyEl=document.querySelector(`.key[data-player="${p}"][data-key="${k}"]`);
 if(keyEl)keyEl.classList.add("down");
 setTimeout(()=>keyEl&&keyEl.classList.remove("down"),80);

 if(!playing)return;
 if(state[p].held[k])return;

 // Find the closest matching note to the judgement line.
 const side=document.getElementById("side"+p);
 const sr=side.getBoundingClientRect();
 const lineY=side.clientHeight-104;
 let best=null,bestDiff=Infinity;
 for(const n of state[p].notes){
   if(n.dataset.key!==k)continue;
   const nr=n.getBoundingClientRect();
   const y=nr.top-sr.top+nr.height/2;
   const d=Math.abs(y-lineY);
   if(d<bestDiff){best=n;bestDiff=d}
 }
 if(best && bestDiff<=48){
   const wasHold=best.dataset.hold==="1";
   judge(p,best);
   if(wasHold){
     state[p].held[k]=best;
   }
 } else {
   // Wrong timing: no score, but don't punish random early presses heavily.
 }
});

document.addEventListener("keyup",e=>{
 const k=keyName(e);
 let p=null;if(lanes1.includes(k))p=1;if(lanes2.includes(k))p=2;
 if(!p)return;
 e.preventDefault();
 const hold=state[p].held[k];
 if(hold){
   state[p].held[k]=null;
 }
});

// Mobile/iframe focus support
document.getElementById("app").addEventListener("click",()=>document.getElementById("app").focus());
</script>
</body>
</html>
"""

components.html(html, height=900, scrolling=False)

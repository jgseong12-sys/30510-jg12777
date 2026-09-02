from pathlib import Path

code = r'''import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="NEON DUEL",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background:#000 !important;
}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"] {display:none !important;}
.block-container {padding:0 !important; max-width:100% !important;}
iframe {border:0 !important; width:100% !important;}
</style>
""", unsafe_allow_html=True)

html = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
*{box-sizing:border-box}
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#000;color:#fff;font-family:Arial,sans-serif}
button{font-family:inherit}
#app{height:100vh;min-height:700px;position:relative;overflow:hidden;outline:none;
background:radial-gradient(circle at 50% 30%,#15152c 0,#05050d 38%,#000 75%)}
#stars{position:absolute;inset:0;pointer-events:none;opacity:.5;
background-image:radial-gradient(#fff 1px,transparent 1px);background-size:43px 43px;
animation:stars 10s linear infinite}
@keyframes stars{to{background-position:43px 86px}}

#top{height:88px;position:relative;z-index:30;display:flex;align-items:center;justify-content:space-between;padding:9px 20px}
.playerHud{width:30%;min-width:220px}.p2{text-align:left}.p1{text-align:right}
.tag{display:inline-block;padding:6px 28px;border:1px solid;border-radius:5px;font-weight:900;letter-spacing:2px;background:#080811}
.p2 .tag{color:#ff35bd;border-color:#ff35bd;box-shadow:0 0 16px #ff35bd66}
.p1 .tag{color:#20ddff;border-color:#20ddff;box-shadow:0 0 16px #20ddff66}
.score{font-size:29px;font-weight:1000;line-height:31px;text-shadow:0 0 13px currentColor}
.p2 .score{color:#ff72d2}.p1 .score{color:#62eaff}
.combo{font-size:12px;letter-spacing:2px;font-weight:900}
.combo b{font-size:24px}.p2 .combo{color:#ff72d2}.p1 .combo{color:#62eaff}
#timer{text-align:center;width:180px}
#timeLabel{font-size:11px;letter-spacing:3px;color:#bbb;font-weight:900}
#clock{font-size:28px;font-weight:1000}
#progress{height:6px;background:#191923;border:1px solid #444;border-radius:10px;overflow:hidden}
#progressFill{height:100%;width:0;background:linear-gradient(90deg,#ff25b7,#fff,#19ddff);box-shadow:0 0 14px #fff}

#battle{position:absolute;left:0;right:0;top:88px;bottom:164px;display:flex;z-index:10}
.side{position:relative;width:50%;height:100%;overflow:hidden;background:#020208}
.p2side{border-right:2px solid #fff5}
.side:after{content:"";position:absolute;inset:0;pointer-events:none;
background:linear-gradient(to bottom,transparent 0%,transparent 50%,#0008 100%);z-index:2}

/* The play area is a trapezoid: narrow in the distance and wide near the player. */
.track{position:absolute;left:0;right:0;top:0;bottom:0;
clip-path:polygon(23% 0%,77% 0%,100% 100%,0% 100%);
background:linear-gradient(180deg,#050516,#02020a);
box-shadow:inset 0 0 35px #fff2;z-index:1}
.p2side .track{background:linear-gradient(180deg,#180713,#030209)}
.p1side .track{background:linear-gradient(180deg,#04131a,#02050a)}

.gridline{position:absolute;top:0;bottom:0;width:1px;transform-origin:top;
background:linear-gradient(transparent,#ffffff33 15%,#ffffff20 80%,#ffffff44)}
.g1{left:23%;transform:rotate(0deg)}
.g2{left:36.5%}.g3{left:50%}.g4{left:63.5%}.g5{left:77%}
.horizontal{position:absolute;left:0;right:0;height:1px;background:#fff1;z-index:1}

.judgeLine{position:absolute;left:0;right:0;bottom:88px;height:5px;z-index:15}
.judgeLine:before{content:"";position:absolute;left:0;right:0;height:100%;border-radius:8px;box-shadow:0 0 10px currentColor,0 0 24px currentColor}
.p2side .judgeLine:before{background:#ff2fba;color:#ff2fba}
.p1side .judgeLine:before{background:#20eaff;color:#20eaff}

.notes{position:absolute;inset:0;z-index:12}
.note{position:absolute;height:46px;border:2px solid currentColor;border-radius:13px;
background:linear-gradient(180deg,#ffffffcc,#ffffff18 32%,#060611dd);
box-shadow:0 0 8px currentColor,0 0 22px currentColor,inset 0 0 12px currentColor;
display:flex;align-items:center;justify-content:center;z-index:12;will-change:top,left,width}
.note .arrow{font-size:25px;font-weight:1000;text-shadow:0 0 9px currentColor}
.note.hold .holdBody{position:absolute;left:50%;bottom:37px;transform:translateX(-50%);
width:42%;border-radius:8px;background:currentColor;box-shadow:0 0 12px currentColor;z-index:-1}
.note.hold .holdTail{position:absolute;left:50%;transform:translateX(-50%);bottom:calc(37px + var(--bodyHeight));
width:14px;height:14px;border:2px solid currentColor;border-radius:50%;background:#fff;
box-shadow:0 0 10px currentColor}
.note.activeHold{box-shadow:0 0 13px currentColor,0 0 35px currentColor,inset 0 0 15px currentColor}
.note.done{animation:pop .12s ease-out forwards}
@keyframes pop{to{opacity:0;transform:scale(1.18)}}

#centerVS{position:absolute;left:50%;top:0;bottom:0;width:3px;transform:translateX(-50%);
background:linear-gradient(transparent,#fff,#fff,transparent);z-index:25;box-shadow:0 0 20px #fff}
#vs{position:absolute;left:50%;top:42%;transform:translate(-50%,-50%);font-size:31px;font-weight:1000;text-shadow:0 0 12px #fff,0 0 28px #28dfff}

#judgements{position:absolute;left:0;right:0;bottom:170px;height:70px;z-index:40;pointer-events:none}
.jmsg{position:absolute;opacity:0;font-size:30px;font-weight:1000;text-shadow:0 0 12px currentColor,0 0 28px currentColor}
.jmsg.p2msg{left:25%;transform:translateX(-50%)}.jmsg.p1msg{left:75%;transform:translateX(-50%)}
.jmsg.show{animation:judge .5s ease-out forwards}
@keyframes judge{0%{opacity:0;transform:translate(-50%,18px) scale(.7)}
22%{opacity:1;transform:translate(-50%,0) scale(1.08)}100%{opacity:0;transform:translate(-50%,-25px)}}
.perfect{color:#fff}.great{color:#6aff9a}.miss{color:#ff557e}.holdok{color:#ffe76b}

#keys{position:absolute;bottom:59px;left:0;right:0;height:98px;display:flex;z-index:50}
.keyPanel{width:50%;display:flex;justify-content:center;align-items:center;gap:10px}
.key{width:67px;height:67px;border:2px solid currentColor;border-radius:12px;background:#06060d;
display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:1000;
box-shadow:inset 0 0 12px currentColor,0 0 8px #000;transition:.06s;user-select:none}
.p2keys .key{color:#ff36bb}.p1keys .key{color:#22e4ff}
.key.down{transform:translateY(4px) scale(.93);background:#fff;color:#000 !important}
.icon{font-size:27px;line-height:27px}.key small{font-size:9px;opacity:.8;margin-top:2px}

#songbar{position:absolute;bottom:0;left:0;right:0;height:59px;z-index:60;background:#05050beF;
border-top:1px solid #333;display:flex;align-items:center;gap:7px;padding:5px 12px}
.song{height:47px;min-width:128px;padding:6px 11px;background:#090912;border:1px solid #333;border-radius:7px;
color:#fff;text-align:left;cursor:pointer}
.song.selected{border-color:currentColor;box-shadow:0 0 14px currentColor}
.song .name{font-size:12px;font-weight:1000}.song .meta{font-size:9px;color:#aaa;margin-top:3px}
#start{margin-left:auto;height:47px;padding:0 20px;border:0;border-radius:8px;
background:linear-gradient(90deg,#ff25b7,#744cff,#1bdfff);color:#fff;font-weight:1000;cursor:pointer}

#overlay,#result{position:absolute;inset:0;z-index:100;background:#000e;display:flex;align-items:center;justify-content:center}
#result{display:none;z-index:110}
#menu,.resultBox{width:min(820px,90%);padding:30px;text-align:center;border:1px solid #fff4;border-radius:17px;
background:radial-gradient(circle at 50% 0,#19132b,#05050a 70%);box-shadow:0 0 50px #6d38ff44}
#menu h1{font-size:46px;margin:0;background:linear-gradient(90deg,#ff29b9,#fff,#1ce4ff);
-webkit-background-clip:text;color:transparent}
#menu p{color:#aaa}.songGrid{display:flex;flex-wrap:wrap;justify-content:center;gap:9px;margin:20px 0}
.pick{min-width:175px;padding:11px;border:1px solid #444;border-radius:9px;background:#090912;color:#fff;cursor:pointer}
.pick.sel{border-color:#fff;box-shadow:0 0 15px #fff4}
#go,#again{padding:13px 40px;border:0;border-radius:9px;background:linear-gradient(90deg,#ff25b7,#1de0ff);
color:#fff;font-weight:1000;cursor:pointer}
#winner{font-size:40px;font-weight:1000}.finalScores{display:flex;justify-content:space-around;font-size:23px;font-weight:900;margin:20px}

@media(max-height:760px){
#top{height:75px}#battle{top:75px;bottom:145px}.judgeLine{bottom:72px}
#keys{bottom:51px;height:85px}.key{width:56px;height:56px}
#songbar{height:51px}.song{height:41px;min-width:112px}.song .meta{display:none}
#judgements{bottom:150px}
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
  <div id="timer"><div id="timeLabel">TIME</div><div id="clock">03:00</div>
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
    <div class="track"></div>
    <div class="gridline g1"></div><div class="gridline g2"></div><div class="gridline g3"></div>
    <div class="gridline g4"></div><div class="gridline g5"></div>
    <div class="horizontal" style="top:25%"></div><div class="horizontal" style="top:50%"></div>
    <div class="horizontal" style="top:75%"></div>
    <div class="notes" id="notes2"></div><div class="judgeLine"></div>
  </div>

  <div id="centerVS"><div id="vs">VS</div></div>

  <div class="side p1side" id="side1">
    <div class="track"></div>
    <div class="gridline g1"></div><div class="gridline g2"></div><div class="gridline g3"></div>
    <div class="gridline g4"></div><div class="gridline g5"></div>
    <div class="horizontal" style="top:25%"></div><div class="horizontal" style="top:50%"></div>
    <div class="horizontal" style="top:75%"></div>
    <div class="notes" id="notes1"></div><div class="judgeLine"></div>
  </div>
</div>

<div id="judgements"><div id="j2" class="jmsg p2msg"></div><div id="j1" class="jmsg p1msg"></div></div>

<div id="keys">
 <div class="keyPanel p2keys">
  <div class="key" data-player="2" data-key="o"><div class="icon">O</div><small>LEFT</small></div>
  <div class="key" data-player="2" data-key="p"><div class="icon">P</div><small>DOWN</small></div>
  <div class="key" data-player="2" data-key="["><div class="icon">[</div><small>UP</small></div>
  <div class="key" data-player="2" data-key="]"><div class="icon">]</div><small>RIGHT</small></div>
 </div>
 <div class="keyPanel p1keys">
  <div class="key" data-player="1" data-key="q"><div class="icon">Q</div><small>LEFT</small></div>
  <div class="key" data-player="1" data-key="w"><div class="icon">W</div><small>DOWN</small></div>
  <div class="key" data-player="1" data-key="e"><div class="icon">E</div><small>UP</small></div>
  <div class="key" data-player="1" data-key="r"><div class="icon">R</div><small>RIGHT</small></div>
 </div>
</div>

<div id="songbar"></div>

<div id="overlay">
 <div id="menu">
  <h1>NEON DUEL</h1>
  <p>1 VS 1 RHYTHM BATTLE</p>
  <div class="songGrid" id="songGrid"></div>
  <p>PLAYER 2: O P [ ] &nbsp;&nbsp; | &nbsp;&nbsp; PLAYER 1: Q W E R</p>
  <p style="font-size:12px">초반에는 한 개씩 등장합니다. 시간이 지날수록 속도와 동시 타일, HOLD 타일이 증가합니다.</p>
  <button id="go">START BATTLE</button>
 </div>
</div>

<div id="result">
 <div class="resultBox">
  <div style="letter-spacing:3px;font-size:14px">BATTLE RESULT</div>
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
const songs=[
{name:"NEON DREAM",bpm:112,diff:"★★★",color:"#ff36bb"},
{name:"ELECTRIC SHOCK",bpm:124,diff:"★★★★",color:"#24dfff"},
{name:"GALAXY RUSH",bpm:132,diff:"★★★★",color:"#8b6cff"},
{name:"BLAZING SOUL",bpm:140,diff:"★★★★★",color:"#ff704d"},
{name:"CYBER PUNK",bpm:148,diff:"★★★★★",color:"#42ff9c"},
{name:"STARLIGHT",bpm:105,diff:"★★",color:"#f6e66b"},
{name:"INFINITY",bpm:136,diff:"★★★★★",color:"#c66cff"},
{name:"NIGHT DRIVE",bpm:120,diff:"★★★",color:"#5ee7ff"}
];

const lanes1=["q","w","e","r"], lanes2=["o","p","[","]"];
const arrows1=["Q","W","E","R"], arrows2=["O","P","[","]"];
const DURATION=180000;
let selected=0,playing=false,startTime=0,lastFrame=0,spawnAcc=0,raf=0;

const state={
1:{score:0,combo:0,notes:[],held:{}},
2:{score:0,combo:0,notes:[],held:{}}
};

function buildSongs(){
 const grid=document.getElementById("songGrid"), bar=document.getElementById("songbar");
 grid.innerHTML="";bar.innerHTML="";
 songs.forEach((s,i)=>{
  const p=document.createElement("button");
  p.className="pick"+(i===selected?" sel":"");
  p.innerHTML=`<b>${s.name}</b><br><small>BPM ${s.bpm} · ${s.diff}</small>`;
  p.onclick=()=>{selected=i;buildSongs()};
  grid.appendChild(p);

  const b=document.createElement("button");
  b.className="song"+(i===selected?" selected":"");b.style.color=s.color;
  b.innerHTML=`<div class="name">${s.name}</div><div class="meta">BPM ${s.bpm} · 03:00</div>`;
  b.onclick=()=>{selected=i;buildSongs();};
  bar.appendChild(b);
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
function judgeText(p,t,c){
 const e=document.getElementById("j"+p);
 e.className="jmsg p"+p+"msg "+c;e.textContent=t;void e.offsetWidth;e.classList.add("show");
}
function speedAt(t){
 // Slower than the earlier version, with a gradual increase.
 return 240 + Math.min(t/DURATION,1)*300;
}
function intervalAt(t){
 const x=Math.min(t/DURATION,1), bpm=songs[selected].bpm;
 // Very sparse/easy start, then progressively denser.
 return Math.max(300,60000/(bpm*(0.62+x*0.82)));
}
function spawnNote(p,lane,hold,travel){
 const side=document.getElementById("notes"+p);
 const el=document.createElement("div");
 const neon=p===1?["#24dfff","#00aaff","#8e7dff","#45ffb0"][lane]:
                   ["#ff36bb","#ff4f76","#c86cff","#ff63e8"][lane];
 el.className="note"+(hold?" hold":"");
 el.style.color=neon;
 el.dataset.key=(p===1?lanes1:lanes2)[lane];
 el.dataset.player=p;el.dataset.hold=hold?"1":"0";
 el.dataset.spawn=performance.now();el.dataset.travel=travel;
 el.dataset.lane=lane;
 if(hold){
   const len=80+Math.random()*120;
   el.dataset.length=len;
   el.innerHTML=`<div class="holdBody" style="height:${len}px"></div>
                 <div class="holdTail"></div><div class="arrow">${p===1?arrows1[lane]:arrows2[lane]}</div>`;
   el.style.setProperty("--bodyHeight",len+"px");
 }else{
   el.innerHTML=`<div class="arrow">${p===1?arrows1[lane]:arrows2[lane]}</div>`;
 }
 side.appendChild(el);state[p].notes.push(el);
}

function spawnPattern(elapsed){
 const progress=Math.min(elapsed/DURATION,1);
 const speed=speedAt(elapsed);
 let count=1;
 if(progress>=.25 && Math.random()<(progress-.25)*1.35) count=2;
 if(progress>=.60 && Math.random()<(progress-.60)*1.05) count=3;
 count=Math.min(count,3);

 // Occasionally synchronize a note between players.
 for(let p=1;p<=2;p++){
   let chosen=[];
   for(let k=0;k<count;k++){
    let lane=Math.floor(Math.random()*4),guard=0;
    while(chosen.includes(lane)&&guard++<10)lane=Math.floor(Math.random()*4);
    chosen.push(lane);
    const hold=Math.random()<(.025+progress*.14);
    spawnNote(p,lane,hold,Math.max(1050,speed*2.25));
   }
 }
}

function getGeom(side,progress,lane){
 // Perspective geometry: top is narrow, bottom is wide.
 const topL=.23, topR=.77, botL=0, botR=1;
 const t=Math.max(0,Math.min(1,progress));
 const left=topL+(botL-topL)*t;
 const right=topR+(botR-topR)*t;
 const center=left+(right-left)*(lane+.5)/4;
 const width=(right-left)/4;
 return {x:(center*side.clientWidth),w:(width*side.clientWidth)};
}

function updateNotes(now){
 for(let p=1;p<=2;p++){
  const side=document.getElementById("side"+p);
  const sr=side.getBoundingClientRect();
  const lineY=side.clientHeight-88;
  for(const el of [...state[p].notes]){
   if(!el.isConnected)continue;
   const progress=(now-Number(el.dataset.spawn))/Number(el.dataset.travel);
   const y=-55+progress*(side.clientHeight+80);
   const geom=getGeom(side,Math.max(0,progress),Number(el.dataset.lane));
   el.style.top=y+"px";
   el.style.left=(geom.x-geom.w/2)+"px";
   el.style.width=Math.max(28,geom.w*.88)+"px";

   // A hold tail reaches the judgement line later than its head.
   const len=Number(el.dataset.length||0);
   const tailY=y-len;
   if(el.dataset.hold==="1"){
     if(el.dataset.active==="1" && tailY>=lineY){
       finishHold(p,el);
       continue;
     }
   }
   if(el.dataset.hold!=="1" && y>=lineY+45){miss(p,el);continue}
   if(el.dataset.hold==="1" && el.dataset.active!=="1" && y>=lineY+45){miss(p,el);continue}
   if(el.dataset.hold==="1" && el.dataset.active==="1" && y>=lineY+len+70){
     // Safety fallback if a held note somehow passes the tail.
     finishHold(p,el);
   }
  }
 }
}

function closestNote(p,k){
 const side=document.getElementById("side"+p);
 const lineY=side.clientHeight-88;
 let best=null,diff=Infinity;
 for(const n of state[p].notes){
  if(n.dataset.key!==k || n.dataset.active==="1")continue;
  const r=n.getBoundingClientRect(),sr=side.getBoundingClientRect();
  const y=r.top-sr.top+r.height/2,d=Math.abs(y-lineY);
  if(d<diff){diff=d;best=n}
 }
 return {best,diff};
}

function hitNote(p,k){
 const q=closestNote(p,k);
 if(!q.best || q.diff>48)return;
 const el=q.best;
 if(el.dataset.hold==="1"){
  const points=100+Math.min(150,state[p].combo*2);
  state[p].combo++;state[p].score+=points;
  el.dataset.active="1";state[p].held[k]=el;el.classList.add("activeHold");
  judgeText(p,"PERFECT","perfect");
  updateHud();
 }else{
  const perfect=q.diff<=22,points=(perfect?100:60)+Math.min(150,state[p].combo*2);
  state[p].combo++;state[p].score+=points;
  el.classList.add("done");
  judgeText(p,perfect?"PERFECT":"GREAT",perfect?"perfect":"great");
  setTimeout(()=>el.remove(),120);
  state[p].notes=state[p].notes.filter(n=>n!==el);
  updateHud();
 }
}

function releaseHold(p,k){
 const el=state[p].held[k];
 if(!el)return;
 const side=document.getElementById("side"+p),lineY=side.clientHeight-88;
 const r=el.getBoundingClientRect(),sr=side.getBoundingClientRect();
 const headY=r.top-sr.top+r.height/2;
 const len=Number(el.dataset.length||0);
 const tailY=headY-len;
 if(tailY>=lineY){
   finishHold(p,el);
 }else{
   state[p].combo=0;
   state[p].score=Math.max(0,state[p].score-25);
   judgeText(p,"MISS","miss");
   removeNote(p,el);
   updateHud();
 }
 state[p].held[k]=null;
}

function finishHold(p,el){
 if(!el||!el.isConnected)return;
 const k=el.dataset.key;
 state[p].held[k]=null;
 state[p].combo++;
 state[p].score+=120+Math.min(180,state[p].combo*2);
 judgeText(p,"GREAT","holdok");
 removeNote(p,el);updateHud();
}
function removeNote(p,el){
 el.classList.add("done");
 setTimeout(()=>el.remove(),110);
 state[p].notes=state[p].notes.filter(n=>n!==el);
}
function miss(p,el){
 state[p].combo=0;state[p].score=Math.max(0,state[p].score-25);
 judgeText(p,"MISS","miss");removeNote(p,el);updateHud();
}

function gameLoop(now){
 if(!playing)return;
 const elapsed=now-startTime,remain=Math.max(0,DURATION-elapsed);
 const sec=Math.ceil(remain/1000);
 document.getElementById("clock").textContent=
  String(Math.floor(sec/60)).padStart(2,"0")+":"+String(sec%60).padStart(2,"0");
 document.getElementById("progressFill").style.width=(elapsed/DURATION*100)+"%";
 spawnAcc+=lastFrame?now-lastFrame:16;
 if(spawnAcc>=intervalAt(elapsed)){spawnAcc=0;spawnPattern(elapsed)}
 updateNotes(now);lastFrame=now;
 if(elapsed>=DURATION){finish();return}
 raf=requestAnimationFrame(gameLoop);
}
function clearNotes(){
 for(let p=1;p<=2;p++){
  state[p].notes.forEach(n=>n.remove());state[p].notes=[];state[p].held={};
 }
}
function reset(){
 for(let p=1;p<=2;p++){state[p].score=0;state[p].combo=0;state[p].notes=[];state[p].held={}}
 updateHud();clearNotes();
 document.getElementById("clock").textContent="03:00";
 document.getElementById("progressFill").style.width="0%";
}
function startGame(){
 document.getElementById("overlay").style.display="none";
 document.getElementById("result").style.display="none";
 reset();playing=true;startTime=performance.now();lastFrame=0;spawnAcc=0;
 document.getElementById("app").focus();raf=requestAnimationFrame(gameLoop);
}
function finish(){
 playing=false;cancelAnimationFrame(raf);clearNotes();
 const s1=state[1].score,s2=state[2].score;
 document.getElementById("final1").textContent=s1.toLocaleString();
 document.getElementById("final2").textContent=s2.toLocaleString();
 const w=document.getElementById("winner");
 if(s1>s2){w.textContent="PLAYER 1 WINS!";w.style.color="#22e4ff"}
 else if(s2>s1){w.textContent="PLAYER 2 WINS!";w.style.color="#ff36bb"}
 else{w.textContent="DRAW!";w.style.color="#fff"}
 document.getElementById("result").style.display="flex";
}

function keyNorm(e){
 if(e.key.length===1)return e.key.toLowerCase();
 return e.key;
}
document.addEventListener("keydown",e=>{
 const k=keyNorm(e);
 let p=lanes1.includes(k)?1:(lanes2.includes(k)?2:null);
 if(!p)return;
 e.preventDefault();
 const keyEl=document.querySelector(`.key[data-player="${p}"][data-key="${CSS.escape(k)}"]`);
 if(keyEl)keyEl.classList.add("down");
 if(playing && !state[p].held[k])hitNote(p,k);
});
document.addEventListener("keyup",e=>{
 const k=keyNorm(e);
 let p=lanes1.includes(k)?1:(lanes2.includes(k)?2:null);
 if(!p)return;e.preventDefault();
 const keyEl=document.querySelector(`.key[data-player="${p}"][data-key="${CSS.escape(k)}"]`);
 if(keyEl)keyEl.classList.remove("down");
 if(playing)releaseHold(p,k);
});
document.getElementById("go").onclick=startGame;
document.getElementById("again").onclick=()=>{
 document.getElementById("result").style.display="none";
 document.getElementById("overlay").style.display="flex";
};
document.getElementById("app").addEventListener("click",()=>document.getElementById("app").focus());
</script>
</body>
</html>
"""

out = Path("/mnt/data/neon_duel_rhythm_game.py")
out.write_text(
    'import streamlit as st\nimport streamlit.components.v1 as components\n' +
    # Keep the generated HTML as a raw triple-quoted string in the Python file.
    '\n' + 'st.set_page_config(page_title="NEON DUEL", page_icon="🎵", layout="wide", initial_sidebar_state="collapsed")\n' +
    'st.markdown("""<style>html,body,[data-testid="stAppViewContainer"],[data-testid="stApp"]{background:#000!important}[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],[data-testid="stStatusWidget"]{display:none!important}.block-container{padding:0!important;max-width:100%!important}iframe{border:0!important;width:100%!important}</style>""",unsafe_allow_html=True)\n' +
    'components.html(' + repr(html) + ', height=900, scrolling=False)\n',
    encoding="utf-8"
)
print(f"완성: {out}")
print("P1 = Q W E R / P2 = O P [ ]")
print("4칸 원근 사선 맵, 느린 시작, 점진적 난이도, HOLD 타일 포함")

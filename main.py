from pathlib import Path

path = Path("/mnt/data/neon_duel.py")

code = r'''
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NEON DUEL", layout="wide")

st.markdown("""
<style>
html,body,[data-testid="stAppViewContainer"],[data-testid="stApp"]{
    background:#000!important;
}
[data-testid="stHeader"],[data-testid="stToolbar"],
[data-testid="stDecoration"],[data-testid="stStatusWidget"]{display:none!important}
.block-container{padding:0!important;max-width:100%!important}
iframe{border:0!important;width:100%!important}
</style>
""", unsafe_allow_html=True)

HTML = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
*{box-sizing:border-box}
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#000;color:white;font-family:Arial,sans-serif}
#game{position:relative;width:100%;height:900px;max-height:100vh;min-height:620px;overflow:hidden;background:radial-gradient(circle,#17172b,#05050b 48%,#000)}
#stars{position:absolute;inset:0;opacity:.35;background-image:radial-gradient(#fff 1px,transparent 1px);background-size:45px 45px}
#top{position:absolute;top:0;left:0;right:0;height:82px;z-index:50;display:flex;justify-content:space-between;align-items:center;padding:7px 16px;background:#020208e8}
.hud{width:34%}.right{text-align:right}.center{width:180px;text-align:center}
.tag{display:inline-block;padding:4px 16px;border:1px solid;border-radius:5px;font-weight:bold;letter-spacing:2px;font-size:12px}
.p2 .tag{color:#ff35bd;border-color:#ff35bd}.p1 .tag{color:#20eaff;border-color:#20eaff}
.score{font-size:25px;font-weight:900}.p2 .score{color:#ff72d2}.p1 .score{color:#62eaff}
.combo{font-size:10px;color:#aaa;letter-spacing:2px}.combo b{font-size:19px}
#clock{font-size:23px;font-weight:900}
#progress{height:5px;background:#222;border-radius:5px;overflow:hidden}
#fill{height:100%;width:0;background:linear-gradient(90deg,#ff2ab9,#fff,#20eaff)}

#battle{position:absolute;top:82px;bottom:150px;left:0;right:0;display:flex;overflow:hidden}
.side{position:relative;width:50%;height:100%;overflow:hidden}
.p2side{border-right:2px solid #fff4}
.track{position:absolute;inset:0;clip-path:polygon(22% 0,78% 0,100% 100%,0 100%);background:linear-gradient(#120615,#020208);box-shadow:inset 0 0 35px #fff2}
.p1side .track{background:linear-gradient(#04131b,#02070b)}
.grid{position:absolute;inset:0;clip-path:polygon(22% 0,78% 0,100% 100%,0 100%);pointer-events:none}
.v{position:absolute;top:0;bottom:0;width:1px;background:#fff2}
.v0{left:22%}.v1{left:36%}.v2{left:50%}.v3{left:64%}.v4{left:78%}
.h{position:absolute;left:0;right:0;height:1px;background:#fff1}.h1{top:25%}.h2{top:50%}.h3{top:75%}
.notes{position:absolute;inset:0;z-index:10}
.judge{position:absolute;left:0;right:0;bottom:68px;height:5px;z-index:20}
.judge:after{content:"";position:absolute;inset:0;box-shadow:0 0 12px currentColor,0 0 24px currentColor}
.p2side .judge:after{background:#ff35bd;color:#ff35bd}.p1side .judge:after{background:#20eaff;color:#20eaff}
.note{position:absolute;height:44px;border:2px solid currentColor;border-radius:12px;background:#ffffff22;display:flex;align-items:center;justify-content:center;box-shadow:0 0 10px currentColor,0 0 23px currentColor;z-index:15}
.arrow{font-size:22px;font-weight:900}
.note.hold .body{position:absolute;left:50%;bottom:34px;transform:translateX(-50%);width:34%;background:currentColor;border-radius:7px;box-shadow:0 0 10px currentColor}
.note.hit{animation:hit .12s forwards}
@keyframes hit{to{opacity:0;transform:scale(1.18)}}

#vs{position:absolute;left:50%;top:43%;transform:translate(-50%,-50%);z-index:30;font-size:28px;font-weight:900;text-shadow:0 0 16px white}
#messages{position:absolute;left:0;right:0;bottom:148px;height:65px;z-index:60;pointer-events:none}
.msg{position:absolute;opacity:0;font-size:28px;font-weight:900;text-shadow:0 0 13px currentColor}
.m2{left:25%;transform:translateX(-50%)}.m1{left:75%;transform:translateX(-50%)}
.msg.show{animation:msg .5s ease-out forwards}
@keyframes msg{0%{opacity:0;transform:translate(-50%,15px) scale(.7)}25%{opacity:1;transform:translate(-50%,0) scale(1.05)}100%{opacity:0;transform:translate(-50%,-25px)}}
.perfect{color:white}.great{color:#65ff9b}.miss{color:#ff557c}.holdtxt{color:#ffe36a}

#keys{position:absolute;left:0;right:0;bottom:52px;height:96px;display:flex;background:#020208;z-index:80}
.keypanel{width:50%;display:flex;justify-content:center;align-items:center;gap:9px}
.key{width:64px;height:64px;border:2px solid currentColor;border-radius:11px;background:#07070e;display:flex;flex-direction:column;justify-content:center;align-items:center;box-shadow:inset 0 0 12px currentColor;user-select:none}
.p2keys .key{color:#ff35bd}.p1keys .key{color:#20eaff}
.key.down{background:#fff;color:#000!important;transform:scale(.92)}
.icon{font-size:25px;font-weight:900}.key small{font-size:8px}

#songs{position:absolute;left:0;right:0;bottom:0;height:52px;background:#05050bee;border-top:1px solid #333;display:flex;align-items:center;gap:5px;padding:4px 8px;z-index:90}
.song{height:42px;min-width:112px;background:#090912;color:white;border:1px solid #444;border-radius:7px;text-align:left;cursor:pointer}
.song.selected{border-color:#fff;box-shadow:0 0 12px #fff5}
.song b{font-size:10px}.song small{font-size:8px;color:#aaa}
#start{margin-left:auto;height:42px;border:0;border-radius:8px;padding:0 18px;background:linear-gradient(90deg,#ff27b9,#20e2ff);color:white;font-weight:900}

.overlay{position:absolute;inset:0;background:#000e;z-index:200;display:flex;align-items:center;justify-content:center}
.box{width:min(800px,92%);padding:28px;text-align:center;border:1px solid #fff4;border-radius:16px;background:#08080feF;box-shadow:0 0 50px #7345ff44}
h1{font-size:45px;margin:0;background:linear-gradient(90deg,#ff27b9,#fff,#20e2ff);-webkit-background-clip:text;color:transparent}
.songgrid{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin:18px}
.pick{width:165px;padding:10px;border-radius:8px;background:#090912;color:white;border:1px solid #444;cursor:pointer}
.pick.selected{border-color:white;box-shadow:0 0 12px #fff5}
.action{padding:12px 34px;border:0;border-radius:8px;background:linear-gradient(90deg,#ff27b9,#20e2ff);color:white;font-weight:900;cursor:pointer}
#result{display:none}
#winner{font-size:38px;font-weight:900}.final{display:flex;justify-content:space-around;font-size:22px;margin:20px}
</style>
</head>
<body>
<div id="game" tabindex="0">
<div id="stars"></div>

<div id="top">
 <div class="hud p2"><div class="tag">PLAYER 2</div><div class="score" id="s2">000,000</div><div class="combo">COMBO <b id="c2">0</b></div></div>
 <div class="center"><div id="clock">03:00</div><div id="progress"><div id="fill"></div></div></div>
 <div class="hud p1 right"><div class="tag">PLAYER 1</div><div class="score" id="s1">000,000</div><div class="combo">COMBO <b id="c1">0</b></div></div>
</div>

<div id="battle">
 <div class="side p2side" id="side2">
  <div class="track"></div><div class="grid"><i class="v v0"></i><i class="v v1"></i><i class="v v2"></i><i class="v v3"></i><i class="v v4"></i><i class="h h1"></i><i class="h h2"></i><i class="h h3"></i></div>
  <div class="notes" id="n2"></div><div class="judge"></div>
 </div>
 <div id="vs">VS</div>
 <div class="side p1side" id="side1">
  <div class="track"></div><div class="grid"><i class="v v0"></i><i class="v v1"></i><i class="v v2"></i><i class="v v3"></i><i class="v v4"></i><i class="h h1"></i><i class="h h2"></i><i class="h h3"></i></div>
  <div class="notes" id="n1"></div><div class="judge"></div>
 </div>
</div>

<div id="messages"><div id="m2" class="msg m2"></div><div id="m1" class="msg m1"></div></div>

<div id="keys">
 <div class="keypanel p2keys">
  <div class="key" data-p="2" data-k="o"><div class="icon">O</div><small>LEFT</small></div>
  <div class="key" data-p="2" data-k="p"><div class="icon">P</div><small>DOWN</small></div>
  <div class="key" data-p="2" data-k="["><div class="icon">[</div><small>UP</small></div>
  <div class="key" data-p="2" data-k="]"><div class="icon">]</div><small>RIGHT</small></div>
 </div>
 <div class="keypanel p1keys">
  <div class="key" data-p="1" data-k="q"><div class="icon">Q</div><small>LEFT</small></div>
  <div class="key" data-p="1" data-k="w"><div class="icon">W</div><small>DOWN</small></div>
  <div class="key" data-p="1" data-k="e"><div class="icon">E</div><small>UP</small></div>
  <div class="key" data-p="1" data-k="r"><div class="icon">R</div><small>RIGHT</small></div>
 </div>
</div>
<div id="songs"></div>

<div class="overlay" id="menu"><div class="box">
 <h1>NEON DUEL</h1><p>1 VS 1 RHYTHM BATTLE</p>
 <div class="songgrid" id="songgrid"></div>
 <p style="color:#aaa">P2: O P [ ]　　P1: Q W E R</p>
 <p style="font-size:12px;color:#888">초반은 1개씩 천천히 시작하고 시간이 지나면 속도, 동시 타일, HOLD가 증가합니다.</p>
 <button class="action" id="go">START BATTLE</button>
</div></div>

<div class="overlay" id="result"><div class="box">
 <div style="letter-spacing:3px">BATTLE RESULT</div><div id="winner"></div>
 <div class="final"><div>PLAYER 2<br><span id="f2">0</span></div><div>PLAYER 1<br><span id="f1">0</span></div></div>
 <button class="action" id="again">BACK TO SONG SELECT</button>
</div></div>

<script>
(() => {
"use strict";

const SONGS=[
 ["NEON DREAM",112,"★★★"],["ELECTRIC SHOCK",124,"★★★★"],
 ["GALAXY RUSH",132,"★★★★"],["BLAZING SOUL",140,"★★★★★"],
 ["CYBER PUNK",148,"★★★★★"],["STARLIGHT",105,"★★"],
 ["INFINITY",136,"★★★★★"],["NIGHT DRIVE",120,"★★★"]
];
const K={1:["q","w","e","r"],2:["o","p","[","]"]};
const L={1:["Q","W","E","R"],2:["O","P","[","]"]};
const C={1:["#20eaff","#20aaff","#9b75ff","#45ffb0"],2:["#ff35bd","#ff4f76","#c86cff","#ff63e8"]};
const DURATION=180000;
let selected=0,playing=false,start=0,last=0,spawnClock=0,raf=0;

const S={
 1:{score:0,combo:0,notes:[],holds:{}},
 2:{score:0,combo:0,notes:[],holds:{}}
};
const $=id=>document.getElementById(id);

function renderSongs(){
 const g=$("songgrid"),b=$("songs");g.innerHTML="";b.innerHTML="";
 SONGS.forEach((s,i)=>{
  const p=document.createElement("button");
  p.className="pick"+(i===selected?" selected":"");
  p.innerHTML="<b>"+s[0]+"</b><br><small>BPM "+s[1]+" · "+s[2]+"</small>";
  p.onclick=()=>{selected=i;renderSongs()};
  g.appendChild(p);

  const q=document.createElement("button");
  q.className="song"+(i===selected?" selected":"");
  q.innerHTML="<b>"+s[0]+"</b><br><small>BPM "+s[1]+" · 03:00</small>";
  q.onclick=()=>{selected=i;renderSongs()};
  b.appendChild(q);
 });
}
function fmt(n){return Math.floor(n).toLocaleString("en-US").padStart(7,"0")}
function hud(){
 $("s1").textContent=fmt(S[1].score);$("s2").textContent=fmt(S[2].score);
 $("c1").textContent=S[1].combo;$("c2").textContent=S[2].combo;
}
function msg(p,text,cls){
 const e=$("m"+p);e.className="msg m"+p+" "+cls;e.textContent=text;
 void e.offsetWidth;e.classList.add("show");
}
function clearNotes(){
 [1,2].forEach(p=>{S[p].notes.forEach(n=>n.remove());S[p].notes=[];S[p].holds={}});
}
function reset(){
 clearNotes();
 [1,2].forEach(p=>{S[p].score=0;S[p].combo=0;S[p].notes=[];S[p].holds={}});
 hud();$("clock").textContent="03:00";$("fill").style.width="0%";
}
function interval(t){
 const x=Math.min(t/DURATION,1);
 return Math.max(350,60000/(SONGS[selected][1]*(.58+x*.72)));
}
function travel(t){return 1350-Math.min(t/DURATION,1)*180}
function spawn(p,lane,hold,travelMs){
 const e=document.createElement("div");
 e.className="note"+(hold?" hold":"");e.style.color=C[p][lane];
 e.dataset.p=p;e.dataset.key=K[p][lane];e.dataset.lane=lane;e.dataset.spawn=performance.now();
 e.dataset.travel=travelMs;e.dataset.hold=hold?"1":"0";
 if(hold){
  const len=90+Math.random()*130;e.dataset.len=len;
  e.innerHTML='<div class="body" style="height:'+len+'px"></div><div class="arrow">'+L[p][lane]+"</div>";
 }else e.innerHTML='<div class="arrow">'+L[p][lane]+"</div>";
 $("n"+p).appendChild(e);S[p].notes.push(e);
}
function makePattern(t){
 const x=Math.min(t/DURATION,1);
 let count=1;
 if(x>.28 && Math.random()<(x-.28)*1.2)count=2;
 if(x>.62 && Math.random()<(x-.62)*.9)count=3;
 for(let p=1;p<=2;p++){
  let used=[];
  for(let i=0;i<count;i++){
   let lane=Math.floor(Math.random()*4),guard=0;
   while(used.includes(lane)&&guard++<12)lane=Math.floor(Math.random()*4);
   used.push(lane);
   spawn(p,lane,Math.random()<(.025+x*.13),travel(t));
  }
 }
}
function geometry(side,t,lane){
 const l=.22*(1-t),r=1-.22*(1-t);
 return {x:(l+(r-l)*(lane+.5)/4)*side.clientWidth,w:(r-l)/4*side.clientWidth};
}
function remove(p,e){
 e.classList.add("hit");setTimeout(()=>e.remove(),120);
 S[p].notes=S[p].notes.filter(n=>n!==e);
}
function miss(p,e){
 S[p].combo=0;S[p].score=Math.max(0,S[p].score-20);msg(p,"MISS","miss");remove(p,e);hud();
}
function finishHold(p,e){
 if(!e||!e.isConnected)return;
 delete S[p].holds[e.dataset.key];
 S[p].combo++;S[p].score+=120+Math.min(180,S[p].combo*2);
 msg(p,"GREAT","holdtxt");remove(p,e);hud();
}
function update(now){
 [1,2].forEach(p=>{
  const side=$("side"+p),h=side.clientHeight,line=h-68;
  S[p].notes.slice().forEach(e=>{
   if(!e.isConnected)return;
   const prog=(now-Number(e.dataset.spawn))/Number(e.dataset.travel);
   const t=Math.max(0,Math.min(1,prog)),g=geometry(side,t,Number(e.dataset.lane));
   const y=-55+prog*(h+90);
   e.style.top=y+"px";e.style.left=(g.x-g.w*.44)+"px";e.style.width=Math.max(30,g.w*.88)+"px";
   if(e.dataset.active==="1"){
    if(y-Number(e.dataset.len)>=line)finishHold(p,e);
   }else if(y>=line+48)miss(p,e);
  });
 });
}
function closest(p,k){
 const side=$("side"+p),line=side.clientHeight-68;
 let best=null,d=1e9;
 S[p].notes.forEach(e=>{
  if(!e.isConnected||e.dataset.key!==k||e.dataset.active==="1")return;
  const r=e.getBoundingClientRect(),sr=side.getBoundingClientRect();
  const y=r.top-sr.top+r.height/2,dd=Math.abs(y-line);
  if(dd<d){d=dd;best=e}
 });
 return {e:best,d:d};
}
function hit(p,k){
 const q=closest(p,k);if(!q.e||q.d>48)return;
 const e=q.e;
 if(e.dataset.hold==="1"){
  e.dataset.active="1";S[p].holds[k]=e;
  S[p].combo++;S[p].score+=100+Math.min(150,S[p].combo*2);
  msg(p,"PERFECT","perfect");hud();
 }else{
  const perfect=q.d<=22;
  S[p].combo++;S[p].score+=(perfect?100:60)+Math.min(150,S[p].combo*2);
  msg(p,perfect?"PERFECT":"GREAT",perfect?"perfect":"great");remove(p,e);hud();
 }
}
function release(p,k){
 const e=S[p].holds[k];if(!e)return;
 const side=$("side"+p),line=side.clientHeight-68;
 const r=e.getBoundingClientRect(),sr=side.getBoundingClientRect();
 const y=r.top-sr.top+r.height/2;
 if(y-Number(e.dataset.len)>=line)finishHold(p,e);
 else{S[p].combo=0;msg(p,"MISS","miss");remove(p,e);hud()}
 delete S[p].holds[k];
}
function loop(now){
 if(!playing)return;
 const elapsed=now-start,remain=Math.max(0,DURATION-elapsed),sec=Math.ceil(remain/1000);
 $("clock").textContent=String(Math.floor(sec/60)).padStart(2,"0")+":"+String(sec%60).padStart(2,"0");
 $("fill").style.width=Math.min(100,elapsed/DURATION*100)+"%";
 spawnClock+=last?now-last:16;
 if(spawnClock>=interval(elapsed)){spawnClock=0;makePattern(elapsed)}
 update(now);last=now;
 if(elapsed>=DURATION){end();return}
 raf=requestAnimationFrame(loop);
}
function startGame(){
 $("menu").style.display="none";$("result").style.display="none";reset();
 playing=true;start=performance.now();last=0;spawnClock=0;
 $("game").focus();raf=requestAnimationFrame(loop);
}
function end(){
 playing=false;cancelAnimationFrame(raf);clearNotes();
 $("f1").textContent=S[1].score.toLocaleString();$("f2").textContent=S[2].score.toLocaleString();
 const w=$("winner");
 if(S[1].score>S[2].score){w.textContent="PLAYER 1 WINS!";w.style.color="#20eaff"}
 else if(S[2].score>S[1].score){w.textContent="PLAYER 2 WINS!";w.style.color="#ff35bd"}
 else{w.textContent="DRAW!";w.style.color="white"}
 $("result").style.display="flex";
}

document.addEventListener("keydown",e=>{
 const k=e.key.toLowerCase();
 let p=K[1].includes(k)?1:(K[2].includes(k)?2:0);if(!p)return;
 e.preventDefault();
 const el=document.querySelector('.key[data-p="'+p+'"][data-k="'+CSS.escape(k)+'"]');
 if(el)el.classList.add("down");
 if(playing)hit(p,k);
});
document.addEventListener("keyup",e=>{
 const k=e.key.toLowerCase();
 let p=K[1].includes(k)?1:(K[2].includes(k)?2:0);if(!p)return;
 e.preventDefault();
 const el=document.querySelector('.key[data-p="'+p+'"][data-k="'+CSS.escape(k)+'"]');
 if(el)el.classList.remove("down");
 if(playing)release(p,k);
});
$("go").onclick=startGame;
$("again").onclick=()=>{$("result").style.display="none";$("menu").style.display="flex";renderSongs()};
$("game").onclick=()=>$("game").focus();
renderSongs();hud();
})();
</script>
</div>
</body>
</html>
"""

app = '''import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NEON DUEL", layout="wide")

st.markdown("""
<style>
html,body,[data-testid="stAppViewContainer"],[data-testid="stApp"]{background:#000!important}
[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],
[data-testid="stStatusWidget"]{display:none!important}
.block-container{padding:0!important;max-width:100%!important}
iframe{border:0!important;width:100%!important}
</style>
""", unsafe_allow_html=True)

GAME_HTML = %s
components.html(GAME_HTML, height=900, scrolling=False)
''' % repr(HTML)

path.write_text(app, encoding="utf-8")
print(path)

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

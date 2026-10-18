from pathlib import Path
import re
p=Path("index.html")
c=p.read_text(encoding="utf-8")
if "PORTFOLIO_REFRESH_2026" in c:
    print("Already refreshed")
    raise SystemExit(0)
c=re.sub(r'<link rel="icon" href="data:image/svg\\+xml;base64,[^"]+" type="image/svg\\+xml">','<link rel="icon" href="/favicon.svg" type="image/svg+xml">',c)
c=c.replace('<meta name="theme-color" content="#090b1a">','<meta name="theme-color" content="#163a32">')
c=c.replace('>Missions<','>Projects<').replace('>Skill tree<','>Expertise<').replace('>Quest log<','>Experience<')
c=c.replace('SYSTEM ONLINE','OPEN TO OPPORTUNITIES').replace('PLAYER 01 / ANALYTICS & APPLIED AI','ANALYTICS / APPLIED AI').replace('MISSION SELECT','SELECTED WORK').replace('Three missions.<br><em>Real-world builds.</em>','Selected projects.<br><em>Real-world results.</em>').replace('All missions <sup>3</sup>','All projects <sup>4</sup>').replace('Start exploring','Explore projects').replace('Open mission','View project')
c=re.sub(r'<button id="toggle-fx"[^>]*>FX ON</button>','',c)
c=c.replace("document.getElementById('toggle-fx').addEventListener(", "document.getElementById('toggle-fx')?.addEventListener(")
gym='''<article class="project project-small gym-card" data-categories="apps"><div class="small-visual gym-visual"><span class="gym-symbol">GH</span><span class="mono">PERSONAL FITNESS / SOFTWARE</span></div><div class="project-body"><div class="project-meta"><span>FITNESS TECH</span><span>04 / PROJECT</span></div><h3>Gym Helper</h3><p>A practical fitness companion built around useful gym workflows and a streamlined experience.</p><div class="chips"><span>Fitness</span><span>Application</span></div><div class="project-links"><a href="https://github.com/Rahul-Ratusaria/gym_helper" target="_blank" rel="noopener">View GitHub ↗</a></div></div></article>'''
start=c.index('<section id="work"')
needle='  </div><div class="exploration">'
idx=c.index(needle,start)
c=c[:idx]+gym+'\n'+c[idx:]
css="""/* PORTFOLIO_REFRESH_2026: elegant design */
:root{--bg:#0e211b;--surface:#18372c;--line:#37594a;--ink:#f5efe3;--muted:#bfcbbf;--acid:#ddcba7}
body{font-size:18px;line-height:1.7;background:var(--bg)}.header{background:#0e211bf2}.brand span,em{color:var(--acid)}
.hero{grid-template-columns:minmax(0,850px);min-height:580px;padding-top:90px}.hero-art{display:none}.hero h1{font-size:clamp(64px,8vw,112px)}.intro{max-width:660px;font-size:20px;color:#cdd7cc}.button.primary{background:var(--acid);color:#18372c}.button.primary:hover{background:#f1dfb9}
.project-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}.project-feature,.project-small,.project-small:last-child{grid-column:span 1;display:flex;flex-direction:column}.project{background:#18372c;border-color:#446154;border-radius:13px}.project:hover{border-color:#ddcba7}.project-visual,.small-visual,.project-small:last-child .small-visual{height:220px;min-height:220px;border:0;overflow:hidden}.forge-flow{transform:scale(.73);transform-origin:center top}.project .screen-button img{max-height:130px;object-fit:contain}.project-body{padding:24px;flex:1;display:flex;flex-direction:column}.project-body p{font-size:16px;line-height:1.65;color:#cad4c9}.project-links{margin-top:auto;padding-top:20px}.project h3{font-size:clamp(25px,3vw,33px)}.section-intro{font-size:18px;color:#c9d5c9}.filters button.active{background:#345247;color:#f2dfb9;border-color:#ad9a76}.exploration,.achievement-toast,.fx-toggle{display:none!important}
.gym-visual{background:radial-gradient(circle at 70% 20%,#466b53,#1c3f32 65%)!important;display:flex!important;align-items:center;justify-content:center;flex-direction:column;gap:10px}.gym-symbol{font:70px Georgia,serif;color:#eddfc2;border:1px solid #c2ad88;border-radius:50%;height:140px;width:140px;display:grid;place-items:center;letter-spacing:-.12em;padding-right:10px}.gym-visual .mono{font-size:12px;color:#e3d4b5}
@media(max-width:800px){.project-grid{grid-template-columns:1fr}.project-feature,.project-small,.project-small:last-child{grid-column:1}.hero{min-height:0;padding-top:65px}.hero h1{font-size:clamp(60px,11vw,90px)}}@media(max-width:520px){.wrap{width:calc(100% - 36px)}.project-body{padding:20px}.intro{font-size:18px}}
"""
c=c.replace('</style>',css+'</style>',1)
p.write_text(c,encoding="utf-8")
print("Refreshed portfolio:",len(c),"characters")

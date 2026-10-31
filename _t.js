const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const f of ['luxury/index.html','luxury-site/magazine/index.html']) for(const [w,q] of [[1300,'?lang=it'],[390,'?lang=fr']]){const pg=await b.newPage({viewport:{width:w,height:900}});const errs=[];pg.on('pageerror',e=>errs.push(e.message));
await pg.goto('file://'+process.cwd()+'/'+f+q);await pg.addStyleTag({content:'html{scroll-behavior:auto!important}'});await pg.waitForTimeout(800);
const r1=await pg.evaluate(()=>document.querySelectorAll('#cal li').length);
await pg.click('#catFilters button[data-k="sea"]');const r2=await pg.evaluate(()=>document.querySelectorAll('#cal li').length);
const ov=await pg.evaluate(()=>document.documentElement.scrollWidth-innerWidth);
if(w==1300&&f.startsWith('luxury/')){await pg.click('#catFilters button[data-k="all"]');await pg.evaluate(()=>document.getElementById('season').scrollIntoView());await pg.waitForTimeout(300);await pg.screenshot({path:'_s.png'});}
console.log(f,w,r1,r2,ov,errs);}
await b.close();})();

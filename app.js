
(function () { // this is to ensure that different browsers can support the animation
    var requestAnimationFrame = window.requestAnimationFrame
    || window.mozRequestAnimationFrame
    || window.webkitRequestAnimationFrame
    || window.msRequestAnimationFrame;
    window.requestAnimationFrame = requestAnimationFrame;
  })();

  let pageWidth = window.innerWidth;
  let pageHeight = window.innerHeight;
  let main = document.querySelector('header');
  
  let crystal;
  let crystals = [];
  const MAX_CRYSTALS = 0;

  // creates max crystals
  for(let i = 0; i < MAX_CRYSTALS; i++) {
      crystal = new Crystal(pageWidth, pageHeight);
      crystals.push(crystal);
      let crys = document.createElement('div');
      crys.setAttribute('class', 'crystal');
      crys.setAttribute('style', crystal.x + crystal.y + crystal.radius + 
      crystal.background + crystal.width + crystal.height + crystal.border);
      main.appendChild(crys);
  }

  let theCrystals = document.querySelectorAll('.crystal');

  function MoveCrystals() {
      for(let i = 0; i < MAX_CRYSTALS; i++) {
          crystals[i].Move();
          theCrystals[i].setAttribute('style', crystals[i].x +crystals[i].y + 
          crystals[i].radius + crystals[i].background + crystals[i].width +crystals[i].height +crystals[i].border);
        
          if(crystals[i].yPos < -10)
          crystals[i].Reset();
          theCrystals[i].setAttribute('style', crystals[i].x +crystals[i].y + 
          crystals[i].radius + crystals[i].background + crystals[i].width +crystals[i].height +crystals[i].border);
      
  } // MoveCrystals()
  }
  
  function Update() {
      MoveCrystals();
      requestAnimationFrame(Update);
  }

  window.addEventListener('load', function() {
      Update();
  });
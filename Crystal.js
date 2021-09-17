class Crystal {

    constructor(pageWidth, pageHeight) {
        this.xPos = Math.floor(Math.random() * pageWidth);
        this.x = 'left: ' + this.xPos + 'px;';
        this.yPos = Math.floor(Math.random() * pageHeight); // 0 - your page height
        this.y = 'top: ' + this.yPos + 'px;';
        this.size = Math.floor(Math.random() * 5) + 4; // 0 - 7 => 4 - 11 called shifting/ size of the crystals
        this.sizePlus = this.size - 0.5;
        this.width = 'width: ' + this.size + 'px;';
        this.height = 'height: ' + this.sizePlus + 'px;';
        this.background = 'background:url(./img/assets/crs.png);';  // change to image do url/image/ do 20px x 20px 
        this.border = 'border-top: 1px solid #ff0;';
        this.radius = 'border-radius: 10%;';
        this.speed = this.size * .09; // 10 * .2 = 2   5 *.2 = 1
        this.dir = Math.floor(Math.random() * 3);
        this.color = "color: #0f0;";
        
}
Move() {
    this.yPos  -= this.speed;
    this.y = 'top: ' + this.yPos + 'px;';
}

    Reset() {
        this.xPos = Math.floor(Math.random() * pageWidth);
        this.x = 'left: ' + this.xPos + 'px;';
        this.yPos = Math.floor(Math.random() * pageHeight); // 0 - your page height
        this.y = 'top: ' + this.yPos + 'px;';
        this.size = Math.floor(Math.random() * 7) + 6; // 0 - 7 => 4 - 11 called shifting
        this.sizePlus = this.size - 0.5;
        this.width = 'width: ' + this.size + 'px;';
        this.height = 'height: ' + this.sizePlus + 'px;';
        this.speed = this.size * .06; // 10 * .2 = 2   5 *.2 = 1
       
}
}
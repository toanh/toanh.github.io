function resizeIFrameToFitContent( iFrame, width, height ) {
    iFrame.width = 960;
    iFrame.height = 820;
    scaleX = width / iFrame.width;
    scaleY = height / iFrame.height;
    scale = Math.min(scaleX, scaleY);
    dx = iFrame.width / 2 * (1 - scale) - (width/2 - (iFrame.width/2) * scale);
    dy = iFrame.height / 2 * (1 - scale);     
    iFrame.style ="transform:translate(-" + dx + "px, -" + dy + "px) scale("+scale+");"          
}      
window.addEventListener('resize', function(e) {
    resizeIFrameToFitContent( document.getElementById( 'pyangelo' ), e.target.innerWidth, e.target.innerHeight );
} );   
window.addEventListener('DOMContentLoaded', function(e) {     
  var iframe = document.getElementById( 'pyangelo' );    
    resizeIFrameToFitContent(iframe, iframe.clientWidth, iframe.parentNode.parentNode.clientHeight);
} );
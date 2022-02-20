/**
 * @param {number[]} height
 * @return {number}
 */

var trap = function(height) {
    if (!height){
        return 0
    };
    let ln = height.length;
    lmax = new Array(ln);
    rmax = new Array(ln); 


    let RMAX = 0;
    for (let i = ln-1; i > -1 ; i--) {
        rmax[i] = RMAX;
        if (height[i]> RMAX) {
            RMAX = height[i];            
        };        
    }

    let LMAX = 0;
    let level;
    let water = 0;

    for (let i=0; i < ln; i++){
        lmax[i] = LMAX;
        if (height[i]>LMAX) {
            LMAX=height[i];
        }
        if (lmax[i]>rmax[i]){
            level = rmax[i]
        } else{
            level = lmax[i]
        }

        //console.log(level);        
        
        if (height[i]<level){
            water += level - height[i];
        }
        //console.log('loop2')

    }
    console.log(lmax, rmax);
    
    console.log('end')
    return water
};


console.log(trap([10, 0, 1, 2, 3, 4, 5, 6, 7]))


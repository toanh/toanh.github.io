function outputf(n) {
    var text = "";
    var color = "rgb(255,255,255)";
    var bgcolor = "rgb(0,0,0)";
    var italics;
    var bold;
    var underlined;
                  
    i = 0;
    while (n.length > 0)
    {
        if (n[0] == "\u001b")
        {
            i++;
            if (text.length > 0)
                pyConsole.appendChild(createColouredTextSpanElement(text, color, bgcolor, italics, bold, underlined));                
            text = "";
            
            var escPattern = /\[ (\d+);2;(\d+);(\d+);(\d+) m/;                          
            var match = n.match(escPattern);
            
            if (typeof(match) !== 'undefined')
            {
                code = parseInt(match[1]);
                if (code == 0)
                {
                    // reset
                    color = "rgb(255,255,255)";
                    bgcolor = "rgb(0,0,0)";                    
                    bold = false;
                    italics = false;
                    underlined = false;
                }
                else if (code == 38)
                {
                    color = "rgb(" + parseInt(match[2]) + "," + parseInt(match[3]) + "," + parseInt(match[4]) + ")"; 
                }
                else if (code == 48)
                {
                    bgcolor = "rgb(" + parseInt(match[2]) + "," + parseInt(match[3]) + "," + parseInt(match[4]) + ")"; 
                }
                else if (code == 1)
                {
                    // bold
                    bold = true;
                }
                else if (code == 3)
                {
                    // italics
                    italics = true;
                }
                else if (code == 4)
                {
                    // underlined
                    underlined = true;
                }                
                i = match.index + match[0].length;
            }
            n = n.substring(i);
        }
        else
        {
            text += n[0];
            n = n.substring(1);
        }                
    }
    if (text.length > 0)
        pyConsole.appendChild(createColouredTextSpanElement(text, color, bgcolor, italics, bold, underlined));                           
    
    pyConsole.scrollTop = document.getElementById("console").scrollHeight;
}

function inputf(n) {
    inputPromise = new Promise((function(n, e) {                    
                inputElement = document.createElement("span");
                inputElement.setAttribute("contenteditable", "true");
                inputElement.style.color = "rgb(255,255,255)";
                inputElement.style.fontSize = "14pt";
                inputElement.style.outlineStyle = "none";
                pyConsole.appendChild(inputElement);
                inputElement.focus();
                inputElement.addEventListener("keyup", (function(e) {
                    e.preventDefault();
                    if (e.key ==="Enter") {
                        userResponse = inputElement.innerText.replace(/\n+$/, "");
                        inputElement.remove();
                        inputElement = null;
                        outputf(userResponse);
                        outputf("\n");
                        n(userResponse);
                    }
                }))
            }));
    return inputPromise;
}
    
function createColouredTextSpanElement(n, color, bgcolor, italics, bold, underlined) {
    let t = document.createTextNode(n);        
    let e = document.createElement("span");
    e.style.color = color;        
    e.style.fontSize = "14pt";
    
    if (typeof(bgcolor) !== 'undefined')
    {
        e.style.backgroundColor = bgcolor;
    }
    
    if (typeof(italics) !== 'undefined')
    {
        if (italics)
        {
            e.style.fontStyle = "italic";
        }
        else
        {
            e.style.fontStyle = "normal";
        }
            
    }
    
    if (typeof(bold) !== 'undefined')
    {
        if (bold)
        {
            e.style.fontWeight = "bold";
        }
        else
        {
            e.style.fontWeight = "normal";
        }    
    }    

    if (typeof(underlined) !== 'undefined')
    {
        if (underlined)
        {
            e.style.textDecorationLine = "underline";
        }
        else
        {
            e.style.textDecorationLine = "none";
        }    
    }  
    e.appendChild(t);        
    return e;
}

function doGoto(name, code)
{
    var destCode = code;
    if (name == "<stdin>")            
    {
        console.log(code);
        var labels = {};
        
        var blocks = [];
                        
        // grabbing all the blocks and their character indices in the code
        var casePattern = /case \d+:/g;                
        var matches = code.matchAll(casePattern);
        var numBlocks = 0;
        var start = 0;
        var end = 0;
        for (match of matches)
        {
            if (numBlocks == 0)
            {
                start = match.index;
            }
            else
            {
                end = match.index;
                blocks.push([start, end - start]);
                start = end;
                
            }
            numBlocks++;
        }
        if (numBlocks > 0)
        {
            blocks.push([start, code.length - start - 1]);
        }
        
        // pass 1:
        // finding all the label blocks, grabbing their block numbers
        // and populating the lookup table with them
        for (i = 0; i < blocks.length; i++)
        {
            block = code.substr(blocks[i][0], blocks[i][1]);
            var blockNumberPattern = /case (\d+)/g;  
            var blockNumberMatches = block.matchAll(blockNumberPattern);
            for (blockNumberMatch of blockNumberMatches)
            {
                var labalNamePattern = /label (.+)/g;
                var labalNameMatches = block.matchAll(labalNamePattern);
                for (labalNameMatch of labalNameMatches)
                {
                    labels[labalNameMatch[1].trim()] = blockNumberMatch[1];
                    
                    // deleting suspensions code associated with label code
                    var suspensionsPattern = /var \$loadname[\S\s]+?\$blk=(\d+);/g;
                    var suspensionsMatches = block.matchAll(suspensionsPattern);   

                    for (suspensionMatch of suspensionsMatches)
                    {
                        var nextBlock = parseInt(blockNumberMatch[1]) + 1;
                        var linenoPattern = /currLineNo = (\d+);/g;
                        var linenoMatches = block.matchAll(linenoPattern);   
                        for (linenoMatch of linenoMatches)                                
                        {
                            var suspCode = "if (Sk.breakpoints('<stdin>.py'," + linenoMatch[1] + ",0)) {var $susp = $saveSuspension({data: {type: 'Sk.delay'}, resume: function() {}}, '<stdin>.py'," + linenoMatch[1] + ",0);$susp.$blk = " + nextBlock + ";$susp.optional = true;return $susp;}$blk=" + nextBlock + ";";
                            destCode = destCode.replace(suspensionMatch[0], suspCode);      
                        }                                
                    }
                    
                    // deleting suspensions code in the next block too
                    if (i < blocks.length - 1)
                    {
                        block = code.substr(blocks[i + 1][0], blocks[i + 1][1]);
                        var suspensionsPattern = /if \(\$ret[\s\S]+=\$ret;/g;
                        var suspensionsMatches = block.matchAll(suspensionsPattern);   

                        for (suspensionMatch of suspensionsMatches)
                        {
                            
                            destCode = destCode.replace(suspensionMatch[0], "");                                                          
                        }                            
                    }
                }
            }
        }
        
        // pass 2:
        // fill in goto statements
        for (i = 0; i < blocks.length; i++)
        {
            block = code.substr(blocks[i][0], blocks[i][1]);
            var gotoPattern = patt2 = /\/\/\s+goto (.+)[\s\S]+/g;
            var gotoMatches = block.matchAll(gotoPattern);
            for (gotoMatch of gotoMatches)
            {
                var lineNo = labels[gotoMatch[1].trim()];
                // replace everything from the case statement onwards (exclusively) with the blk jump
                destCode = destCode.replace(gotoMatch[0], "$blk=" + lineNo + ";/* goto */continue;");
            }
        }                                
    }
    
    return destCode;
}
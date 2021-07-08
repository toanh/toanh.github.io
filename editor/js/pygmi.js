// preprocess the code to relax language grammar rules for newbies!
function pygmify(code)
{
    pass1 = code;

    // forever loop
    var forever_pattern = /^(\s*)(forever).*$/gm;                
    var matches = code.matchAll(forever_pattern);
    for (match of matches)
    {
        pass1 = pass1.substr(0, match.index) + pass1.substr(match.index).replace(match[0], match[1] + "while True");
        //pass1 = pass1.replace(match[0], match[1] + "while True");
    }    

    // until loop
    var until_pattern = /^(\s*)(until)(.*)$/gm;                
    matches = code.matchAll(until_pattern);
    for (match of matches)
    {
        pass1 = pass1.substr(0, match.index) + pass1.substr(match.index).replace(match[0], match[1] + "while not" + match[3]);
        //pass1 = pass1.replace(match[0], match[1] + "while not" + match[3]);
    }      
    


    pass2 = pass1;
    // no colons   
    var if_elif_else_while_for_def_class_pattern = /^(\s*)(if|elif|else|while|for|def|class)(.*)$/gm;                
    matches = pass1.matchAll(if_elif_else_while_for_def_class_pattern);
    for (match of matches)
    {
        if (match[0].trim().slice(-1) != ":")
        {
            pass2 = pass2.substr(0, match.index) + pass2.substr(match.index).replace(match[0], match[0] + ":");
        }
    }    

    
    return pass2;
}
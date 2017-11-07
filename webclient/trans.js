jQuery(document).ready(function(){
    function translate(arg){
        var s = jQuery(arg).text().trim();
        jQuery.ajax({ 
            type:'GET',
            url:'action.php',
            dataType:'json',
            data:{t:s},
            success:function(data){
                if(data == null){
                    jQuery(arg).text("待翻译");
                }else{
                    jQuery(arg).text(data);  
                }                            
            }
        });
    }

    //default.htm页面
    translate("#tabNavigate div");
    translate("#tabFind div");
    translate("#runBoxText");
    translate("#queryPanelTitle1");
    translate("#queryTiming-button");
    translate("#addDefineGroup");
    translate("#removeDefineGroup");
    translate(".queryBalloon");
    translate(".topmenu span");
    translate("#PluginListBox span a:eq(2)");
    translate("#crcFindButton a");
    translate(".initialMsg a");
    translate("#yuimenuitemlabel");
    jQuery("#ontFormFindName table option").each(function(){
        translate(this);
    });
    jQuery("#crcFindStrategy option").each(function(){
        translate(this);
    });
    jQuery("#menubutton2select option").each(function(){
        translate(this);
    }); 
    jQuery("#crcFindCategory option").each(function(){
        translate(this);
    }); 
    jQuery("#ontFindDisp a").each(function(){
        translate(this);
    });
    jQuery("#topBar a:lt(2)").each(function(){
        translate(this);
    });
    jQuery("#topBar a:gt(2)").each(function(){
        translate(this);
    });
    jQuery(".tabBox div").each(function(){
        translate(this);
    });
    jQuery("#ontFormFindName option").each(function(){
        translate(this);
    });
    jQuery("#newBox a").each(function(){
        translate(this);
    });
    jQuery(".qryButtonDate a").each(function(){
        translate(this);
    });
    jQuery(".qryButtonExclude a").each(function(){
        translate(this);
    });
    jQuery("#menubutton1select option").each(function(){
        translate(this);
    });
    jQuery("#anaPluginView option").each(function(){
        translate(this);
    });
    jQuery(".yui-nav li a").each(function(){
        translate(this);
    });
    jQuery(".queryLabel").each(function(){
        translate(this);
    });
    jQuery(".qryButtonOccurs .occurs").each(function(){
        translate(this);
    });
});
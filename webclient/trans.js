
function translate(arg){
    var s = jQuery(arg).text().trim();
    var t = JSON.stringify({"src": s, "domain":"metadata"});
    jQuery.ajax({ 
        type:'POST',
        url:'http://47.94.148.72:1262/trans',  
        dataType:'json',
        data:t,
        contentType:'application/x-www-form-urlencoded',
        success:function(data){
        	var r = data['exception'];

        	if(r == true){
        		jQuery(arg).text("待翻译"); 
        	}else{
        		jQuery(arg).text(data['result']);
        	}
                                       
        }
    });
}

// function translate(arg){
//     var s = jQuery(arg).text().trim();
//     jQuery.ajax({ 
//         type:'POST',
//         url:'action.php',
//         dataType:'json',
//         data:{t:s},
//         success:function(data){
//             if(data == null){
//                 jQuery(arg).html("待翻译");
//             }else{
//                 jQuery(arg).html(data);  
//             }                            
//         }
//     });
// }

function buttonExcute(arg){
 jQuery(arg).each(function(){
     translate(this);
 });
}

//文章中去除html标签
function delHtmlTag(str){  
  return str.replace(/<[^>]+>/g,"");//去掉所有的html标记  
}  

i2b2.events.afterLogin.subscribe(function(){
    //default.htm页面
    jQuery("#menubutton1select option,#queryBalloonBox .queryBalloon,#optionsHistory span,#optionsQT span,#optionsOntNav span,#optionsOntFind span,#ontFindCoding option,#ontFindCategory option,.temporalControl a,.temporalControl a,#temporalbuilder_0 option,#addDefineGroup-button,#groupCount span,#queryBalloonAnd1,#queryBalloonAnd2,#queryBalloon1,#queryPanelTitle1,#queryPanelTitle2,#queryPanelTitle3,.qryButtonOccurs .occurs,.queryLabel,.yui-nav li a,#anaPluginView option,.qryButtonExclude a,.qryButtonDate a,#newBox a,#ontFormFindName option,.tabBox div,#topBar a:lt(2),#topBar a:gt(2),#ontFindDisp a,#crcFindCategory option,#crcFindStrategy option,.initialMsg a,#crcFindButton a,#PluginListBox span a:eq(2),.topmenu span,#tabNavigate div,#tabFind div,#runBoxText,#ontFormFindName table option").each(function(){
        translate(this);
    });

    //改变密码弹出框
    jQuery(".hd,#modifier-viewer-body tr td:even()").each(function(){
        translate(this);
    });

    // jQuery("#modifier-viewer-body center input").each(function(){
    //     transButton(this);
    // });

    //帮助
    // jQuery("div").delegate("#helpLink","click",function(){
    //     jQuery("#treeDiv1 .ygtvcontent a").each(function(){
    //         translate(this);
    //     });
    // });
});

jQuery(document).ready(function(){
    jQuery("#menubutton2select option,#addDefineGroup,#removeDefineGroup").each(function(){
        translate(this);
    });

    //点击插件按钮
    var flag = true;
    jQuery("#pluginsMenu").on("click",function(){
        if(flag){
            jQuery(".txtBoundBox div,#anaPluginCats option").each(function(){
                translate(this);
            });
            flag = false;
        }             
    });
    var flag1 = true;
    jQuery(".initialMsg a").on("click",function(){
        if(flag1){
            jQuery(".txtBoundBox div,#anaPluginCats option,.txtBoundBox.NAME").each(function(){
                translate(this);
            });
            flag1 = false;
        }
    });
    jQuery(".txtBoundBox.NAME").on("click",function(){
        jQuery(".txtBoundBox.NAME").each(function(){
            translate(this);
        });    
    });
    jQuery("#viewMode-Analysis a:eq(0)").on("change",function(){   
        jQuery("#anaPluginList .txtBoundBox div,#anaPluginCats option").each(function(){
            translate(this);
        });      
    });
    jQuery("#anaPluginCats").on("change",function(){   
        jQuery("#anaPluginList .txtBoundBox div,.txtBoundBox.NAME").each(function(){
            translate(this);
        });      
    });
    jQuery("#anaPluginView").on("change",function(){   
        jQuery("#anaPluginList .txtBoundBox div,#anaPluginList .txtBoundBox.NAME").each(function(){
            translate(this);
        });      
    });
    jQuery("#anaPluginList").on("click",function(){
        jQuery("#anaPluginViewBox .tabBox div,.yui-nav em,.Dem1Set-MainContentPad div,.results-directions,.Dem1Set-MainContentPad h1,.Dem1Set-MainContentPad h2,.Dem1Set-MainContentPad p,.Dem2Set-MainContentPad div,.Dem2Set-MainContentPad h1,.Dem2Set-MainContentPad h2,.Dem2Set-MainContentPad p,.Timeline-MainContentPad div:lt(4),.Timeline-MainContentPad .concptItem,.Timeline-MainContentPad #Timeline-DeleteMsg,.Timeline-MainContentPad h1,.Timeline-MainContentPad h2,.Timeline-MainContentPad p,.WISEsearcher-MainContentPad div:eq(0),#WISEsearcher-caseOptions b,#WISEsearcher-caseOptions li,#WISEsearcher-matchOptions b,#WISEsearcher-excludeOptions b").each(function(){
            translate(this);
        });
        jQuery(".WISEsearcher-MainContentPad span,.WISEsearcher-MainContentPad h1,.WISEsearcher-MainContentPad li,.WISEsearcher-MainContentPad table td,.CAREcncptDem-MainContentPad div:lt(4),.CAREcncptDem-MainContentPad .droptrgtlbl,.CAREcncptDem-MainContentPad .concptItem").each(function(){
            translate(this);
        });
        jQuery("#CAREcncptDem-ConceptHint i,.CAREcncptDem-MainContent .export-directions,.CAREcncptDem-MainContentPad h1,.CAREcncptDem-MainContentPad span,.CAREcncptDem-MainContentPad li,.CAREcncptDem-MainContentPad td,.CAREobsTally-MainContentPad div:lt(4),.CAREobsTally-MainContentPad .droptrgtlbl,.CAREobsTally-MainContentPad .concptItem,#CAREobsTally-ConceptHint i,.CAREobsTally-MainContentPad span,.CAREobsTally-MainContentPad li,#CAREobsTally-Main span,.CAREobsTally-MainContentPad h1,.CAREobsTally-MainContentPad td").each(function(){
            translate(this);
        });
        jQuery(".ExportXLS-MainContentPad div:lt(4),.ExportXLS-MainContentPad .droptrgtlbl,.ExportXLS-MainContentPad .concptItem,#ExportXLS-ConceptHint i,.optionitems b,.optionitems option,.optionitems label,.ExportXLS-MainContentPad h1,.ExportXLS-MainContentPad span,.ExportXLS-MainContentPad ul li,.ExportXLS-MainContentPad li span,.ExportXLS-MainContentPad:eq(2) td,.ExportXLS-MainContentPad ol li span,.ExportXLS-MainContentPad ol li:gt(7)").each(function(){
            translate(this);
        });
    });
 
	//执行查询
    jQuery("#runBoxText").on("click",function(){
        jQuery("#dialogQryRun .bd div:eq(0),#dialogQryRun .bd div:eq(3),#dialogQryRunResultType. span").each(function(){
            translate(this);
        });
    });

    //清空 Add New
    // jQuery(".qryPanelClear,[alt='Add New'],#newBox").click(function(){
    //     setTimeout("buttonExcute('#queryPanelTitle2,#queryPanelTitle3')",0.01);
    // });
 
    //点击清空按钮
    // jQuery("#newBox").click(function(){
    //     setTimeout("buttonExcute('#yui-gen0 .yuimenuitemlabel,#queryTiming-button,#defineTemporal-button,#menubutton1select option,.relationshipAmongEvents option')",0.01);
    // });

    //添加查询时间按钮
    var count = 0;
    jQuery("center .temporalControl a:eq(0)").on("click",function(){
        if(count <= -2){
            count = 0;
        }
        ++count;
        setTimeout("buttonExcute('#temporalbuilder_"+count+" option')",0.01);

       jQuery("center .temporalControl a:eq(1)").on("click",function(){
            count = count - 1;
        });            
    });


    // //导航条款选项
    // function okButton(arg){
    // 	let flag2 = true;
	   //  jQuery(arg).on("click",function(){
	   //  	if(flag2){
	   //  		setTimeout("buttonExcute('.ft button')",.1);
	   //  		flag2 = false;
	   //  	}
	   //  });
    // }
    // okButton("#ontTopTabs [alt='Show Options']");
    // okButton("#crcHistoryBox [alt='Show Options']");
    // okButton("#crcQueryToolBox [alt='Show Options']");
    // okButton("#runBoxText");  
});





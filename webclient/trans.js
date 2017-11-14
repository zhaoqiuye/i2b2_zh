
function translate(arg){
    var s = jQuery(arg).text().trim();
    jQuery.ajax({ 
        type:'POST',
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

function transButton(arg){
    var s = jQuery(arg).val().trim();
    jQuery.ajax({ 
        type:'POST',
        url:'action.php',
        dataType:'json',
        data:{t:s},
        success:function(data){
            if(data == null){
                jQuery(arg).val("待翻译");
            }else{
                jQuery(arg).val(data);  
            }                            
        }
    });
}
i2b2.events.afterLogin.subscribe(function(){
    //default.htm页面
    var en = "#ontFindCategory option,.temporalControl a,.temporalControl a,#temporalbuilder_0 option,#addDefineGroup-button,#groupCount span,#queryBalloonAnd1,#queryBalloonAnd2,#queryBalloon1,#queryPanelTitle1,#queryPanelTitle2,#queryPanelTitle3,.qryButtonOccurs .occurs,.queryLabel,.yui-nav li a,#anaPluginView option,#menubutton1select option,.qryButtonExclude a,.qryButtonDate a,#newBox a,#ontFormFindName option,.tabBox div,#topBar a:lt(2),#topBar a:gt(2),#ontFindDisp a,#crcFindCategory option,#menubutton2select option,#crcFindStrategy option,.initialMsg a,#crcFindButton a,#PluginListBox span a:eq(2),.topmenu span,#tabNavigate div,#tabFind div,#runBoxText,#addDefineGroup,#removeDefineGroup,#ontFormFindName table option";
    jQuery(en).each(function(){
        translate(this);
    });

    //改变密码弹出框
    jQuery(".hd,#modifier-viewer-body tr td:even()").each(function(){
        translate(this);
    });

    jQuery("#modifier-viewer-body center input").each(function(){
        transButton(this);
    });

    //点击清空按钮
    // jQuery(".qryPanelClear a").click(function(){
    //     jQuery(".yuimenuitem a,#queryTiming-button,#queryPanelTitle1,#queryPanelTitle2,#queryPanelTitle3").each(function(){
    //         translate(this);
    //     });
    // });

    // jQuery("#qryToolFooter #newBox").click(function(){
    //     jQuery("#queryTiming-button,#yui-gen0 .yuimenuitemlabel").each(function(){
    //         translate(this);
    //     });
    // });

    // jQuery("#scrollBox a:eq(2)").click(function(){
    //     jQuery("#queryTiming-button,#queryPanelTitle1,#queryPanelTitle2,#queryPanelTitle3").each(function(){
    //         translate(this);
    //     });
    // });

    //点击插件按钮
    jQuery("#pluginsMenu").on("click",function(){
        jQuery(".txtBoundBox div,#anaPluginCats option").each(function(){
            translate(this);
        });
    });

    jQuery("#anaPluginList").on("click",function(){
        jQuery("#anaPluginViewBox .tabBox div,.yui-nav em").each(function(){
            translate(this);
        });
    });

    jQuery(".initialMsg a").on("click",function(){
        jQuery(".txtBoundBox div,#anaPluginCats option").each(function(){
            translate(this);
        });
    });

    //帮助
    jQuery("div").delegate("#helpLink","click",function(){
        jQuery("#treeDiv1 .ygtvcontent a").each(function(){
            translate(this);
        });
    });

    //执行查询
    jQuery("#runBoxText").on("click",function(){
        jQuery("#dialogQryRun .bd div:eq(0),#dialogQryRun .bd div:eq(3),#dialogQryRunResultType span").each(function(){
            translate(this);
        });
    });

    //执行查询的确认按钮
    // jQuery("#dialogQryRun").delegate("#yui-gen9-button","click",function(){
    //     var queryResult = "#infoQueryStatusText span,#chart0 td:even(),.QRMainHeader,.printReportButton span,#queryDetailsTable span,.descHead,#qdHeaderTable td,.eventsRelHdr,.qrPanelItemTable td span:eq(0),.qrPanelItemTable td span:eq(3),.qrPanelItemTable td:eq(1),.qrPanelItemTable td:eq(2),#qrsTitle,.subTitleDivs,.reultsTable .descResultshead";
    //         jQuery(queryResult).each(function(){
    //             translate(this);
    //         });
    // });

    //显示查询状态
    // jQuery(".tabQueryStatus ").on("click",function(){
    //     jQuery("#infoQueryStatusText span").each(function(){
    //         translate(this);
    //     });
    // });

    //图形结果
    // jQuery(".tabQueryGraphs div").on("click",function(){
    //     jQuery("#chart0 .tabQueryGraphs td:eq(1),#chart0 .tabQueryGraphs td:eq(3) span").each(function(){
    //         translate(this);
    //     });
    // });
 
    //查询报表
    
    // jQuery(".tabQueryReport div").on("click",function(){
    //     jQuery(".QRMainHeader,.printReportButton span,#queryDetailsTable span,descHead,#qdHeaderTable td,.eventsRelHdr,.qrPanelItemTable td:eq(1),.eventsRelHdr,.qrPanelItemTable td:eq(2),.eventsRelHdr,.qrPanelItemTable td:eq(3) span,.subTitleDivs,descResultshead").each(function(){
    //         translate(this);
    //     });
    // }); 
    // jQuery(".button-group .first-child #yui-gen9-button").on("click",function(){
    //     alert("22");
    //     jQuery("#infoQueryStatusText span,#chart0 td:even(),.QRMainHeader,.printReportButton span,#queryDetailsTable span,.descHead,#qdHeaderTable td,.eventsRelHdr,.qrPanelItemTable td span:eq(0),.qrPanelItemTable td span:eq(3),.qrPanelItemTable td:eq(1),.qrPanelItemTable td:eq(2),#qrsTitle,.subTitleDivs,.reultsTable .descResultshead").each(function(){
    //         alert("22");
    //         translate(this);
    //     });
    // });


    // jQuery("#menubutton1select option:gt(1)").on("click",function(){
    //     alert("11");
    //     jquery("#queryPanelTimingB1-button,#menubutton1select option").each(function(){
    //         translate(this);
    //     });
    // });
});

jQuery(document).ready(function(){
    jQuery("#menubutton2select option,#addDefineGroup,#removeDefineGroup").each(function(){
        translate(this);
    });
});





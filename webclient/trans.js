
function translate(arg){
    var s = jQuery(arg).text().trim();
    jQuery.ajax({ 
        type:'POST',
        url:'action.php',
        dataType:'json',
        data:{t:s},
        success:function(data){
            if(data == null){
                jQuery(arg).html("待翻译");
            }else{
                jQuery(arg).html(data);  
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

function buttonExcute(arg){
	jQuery(arg).each(function(){
		translate(this);
	});
}
i2b2.events.afterLogin.subscribe(function(){
    //default.htm页面
    jQuery("#queryBalloonBox .queryBalloon,#optionsHistory span,#optionsQT span,#optionsOntNav span,#optionsOntFind span,#ontFindCoding option,#ontFindCategory option,.temporalControl a,.temporalControl a,#temporalbuilder_0 option,#addDefineGroup-button,#groupCount span,#queryBalloonAnd1,#queryBalloonAnd2,#queryBalloon1,#queryPanelTitle1,#queryPanelTitle2,#queryPanelTitle3,.qryButtonOccurs .occurs,.queryLabel,.yui-nav li a,#anaPluginView option,#menubutton1select option,.qryButtonExclude a,.qryButtonDate a,#newBox a,#ontFormFindName option,.tabBox div,#topBar a:lt(2),#topBar a:gt(2),#ontFindDisp a,#crcFindCategory option,#menubutton2select option,#crcFindStrategy option,.initialMsg a,#crcFindButton a,#PluginListBox span a:eq(2),.topmenu span,#tabNavigate div,#tabFind div,#runBoxText,#addDefineGroup,#removeDefineGroup,#ontFormFindName table option").each(function(){
        translate(this);
    });

    //show options确认取消
    var flag = true;
    jQuery("#ontMainBox .opXML").delegate("[title='Show Options']","click",function(){
		if(flag){
    		setTimeout("buttonExcute('.yui-panel-container .ft button')",0.1);
    		flag = false;
    	}
    });
  //   jQuery("#ontMainBox .opXML").delegate("[title='Show Options']","click",function(){
		// if(flag){
  //   		setTimeout("buttonExcute('#optionsOntFind .yui-panel-container .ft button')",0.1);
  //   		let flag = false;
  //   	}
  //   });
  //   jQuery("#crcHistoryBox .opXML").delegate("[title='Show Options']","click",function(){
		// if(flag){
  //   		setTimeout("buttonExcute('#optionsHistory .ft button')",0.1);
  //   		let flag = false;
  //   	}
  //   });
  //   jQuery("#crcHistoryBox .opXML").delegate("[title='Show Options']","click",function(){
		// if(flag){
  //   		setTimeout("buttonExcute('#optionsHistory .yui-panel-container .ft button')",0.1);
  //   		let flag = false;
  //   	}
  //   });
    // jQuery("#crcHistoryBox").delegate("a:eq(2)","click",function(){
    // 	if(flag){
    // 		setTimeout("buttonExcute()",0.1);
    // 		flag = false;
    // 	}
    // });
    // jQuery("#crcQueryToolBox").delegate("a:eq(1)","click",function(){
    // 	if(flag){
    // 		setTimeout("buttonExcute()",0.1);
    // 		flag = false;
    // 	}
    // });

    //改变密码弹出框
    jQuery(".hd,#modifier-viewer-body tr td:even()").each(function(){
        translate(this);
    });

    jQuery("#modifier-viewer-body center input").each(function(){
        transButton(this);
    });

    //点击添加时间关系
    jQuery("center").degelate(".temporalControl","click",function(){
    	alert("11");
    	jQuery(".relationshipAmongEvents:gt(1) option").each(function(){
    		translate(this);
    	});
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







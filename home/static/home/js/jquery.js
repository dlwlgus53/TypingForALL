$(document).ready(function(){
	$(function(){ $(".emojiLoaded").click(function(){ 
			var index = $(this).index();
			console.log($('.emojiLoaded:eq('+index+')').text());
			document.getElementById("txtBox").append($('.emojiLoaded:eq('+index+')').text());
			$("#emojiTxt").css("opacity", '0');
	})});
	$(function(){ $("#sendButton").click(function(){ 
		jQuery("#recording-wrap").show(); 
		if(document.getElementById("txtBox").innerHTML!=""){
		  var sendBox = document.createElement('div'); //말풍선
		  sendBox.className = "balloon"; //말풍선 클래스 이름

		  var sendMessage = document.createElement('span'); // 메세지
  	 	  sendMessage.innerHTML = document.getElementById("txtBox").innerHTML; //메세지 내용
  	 	  sendMessage.className = "sendMessage";
  	 	  document.getElementById("txtBox").innerHTML=""; // 입력창 초기화
 	  	  sendBox.appendChild(sendMessage);
 	  	  document.getElementById("sentArea").appendChild(sendBox);

 	  	}
	 	 
 	  	})});

		$(function(){ $("#mic-cover").click(function(){
			jQuery("#greyBox").show();  
			jQuery("#recording-wrap").show(); 
			jQuery(".recording-message").show(); 
		    });
		});

	$(function(){ $("#hi").focus(function(){ 
		$("#webcam-balloon").css("opacity",1);
		$("#webcam-balloon").css("width","300px");
	
});});
	$(function(){ $("#hi").blur(function(){ 
		$("#webcam-balloon").css("opacity",0);
		// $("#webcam-balloon").css("width","300px");
	
});});

	$(function(){ $(".emojiLoaded").bind('focus blur',function(e){ 
		$(this).toggleClass('changed');
});});
	

	$("#sendButton").bind('focus blur',function(e){ 

		$(".send").toggleClass('changed');

})
});


$(document).ready(function(){
		$(function(){ $("#mic").click(function(){
			jQuery("#greyBox").show();  
			jQuery("#recording-wrap").show(); 
			jQuery(".recording-message").show(); 
		    });
		});


});



	function wrapWindowByMask(){

    $('#mask').show();
    $('.window').show();
}
// [END] s1_save Event 종료
 $(document).ready(function(){
    //검은 막 띄우기
    $('#next').click(function(e){
        e.preventDefault();
        wrapWindowByMask();
    });

	$(".emoji").click(function(){ 
		jQuery("#balloon").show();
		var emojiInput = document.createElement('img');
        emojiInput.className='emoji';
        emojiInput.setAttribute('src', this.src);
        document.getElementById('balloon').appendChild(emojiInput);
        jQuery('.rectangle-speech-border').hide();

	})

    $('#face').click(function(e){
    		if($('#emoji').css("display") == "none"){   // 나이 체크박스 show (Ex. 10대 이하, 20대 이하)
	        	jQuery('#emoji').show();    
	    }
		    else if($('#emoji').css("display") == "block"){   // 나이 체크박스 show (Ex. 10대 이하, 20대 이하)
	        	jQuery('#emoji').hide();    
	    }


});
});

function sentTodjango(title,text)
  {
 
    var data = title + '|' + text ;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '{% url 'noteSAVE' %}', true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send('data=' + encodeURIComponent(data));
    xhr.onreadystatechange = function() {

if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        // 在這裡處理回應

    if (xhr.status === 200) {
            
            // 狀態碼200表示成功
        var response = JSON.parse(xhr.responseText); // 解析JSON回應

            // 在這裡處理回應
 
            // 進行進一步的處理，例如將回應添加到您的網頁中
        
        return chat_what , datas ;
      
    } else {
            // 處理錯誤，例如顯示錯誤信息
            console.error('發生錯誤，狀態碼：' + xhr.status);
    }   
}
};
  } 
 
 
 
 
 
 // 显示对话框
 function showDialog() {
    var dialogBox = document.getElementById("dialog-box");
    var titleInput = document.getElementById("dialog-title");
    var textInput = document.getElementById("dialog-text");
    titleInput.value = "" ;
    textInput.value = "" ;
    dialogBox.style.display = "block";
  }

  // 取消对话框
  function cancelDialog() {
    var dialogBox = document.getElementById("dialog-box");
 
    dialogBox.style.display = "none";
  }
  
  // 保存对话框内容
  function saveDialog() {
    var titleInput = document.getElementById("dialog-title");
    var textInput = document.getElementById("dialog-text");
  
    var title = titleInput.value;
    var text = textInput.value;
    
    // 检查标题是否为空
    if (title.trim() === "") {
      alert("请输入标题！");
      return; // 阻止关闭对话框
    }

    // 在这里可以处理保存逻辑
   
    sentTodjango(title,text);
    // 清除标题和文本输入框的值
    titleInput.value = "";
    textInput.value = "";

    // 关闭对话框
 
     
    cancelDialog();
  }
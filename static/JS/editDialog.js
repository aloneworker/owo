function editDialog() {
    // 創建對話方塊的容器元素
    var dialogContainer = document.createElement("div");
    dialogContainer.style.width = "300px";
    dialogContainer.style.padding = "20px";
    dialogContainer.style.border = "1px solid #ccc";
    dialogContainer.style.backgroundColor = "#fff";
    dialogContainer.style.position = "fixed";
    dialogContainer.style.top = "50%";
    dialogContainer.style.left = "50%";
    dialogContainer.style.transform = "translate(-50%, -50%)";
    
    // 創建標題元素
    var title = document.createElement("h2");
    title.textContent = "這是標題";
    title.contentEditable = true; // 将内容设置为可编辑
    
    // 創建內容元素
    var content = document.createElement("p");
    content.textContent = "這是對話方塊的內容。";
    content.contentEditable = true; // 将内容设置为可编辑
    
    // 創建按鈕容器元素
    var buttonContainer = document.createElement("div");
    buttonContainer.style.display = "flex";
    buttonContainer.style.justifyContent = "space-between";
    
    // 創建關閉按鈕元素
    var closeButton = document.createElement("button");
    closeButton.textContent = "關";
    closeButton.onclick = function() {
        document.body.removeChild(dialogContainer); // 關閉對話方塊
    };

    // 創建Edit按鈕元素
    var editButton = document.createElement("button");
    editButton.textContent = "存";
    editButton.onclick = function(){
        alert('EDIT');
    };
    
    // 向按鈕容器中添加按鈕元素
    buttonContainer.appendChild(closeButton);
    buttonContainer.appendChild(editButton);
    
    // 向容器中添加元素
    dialogContainer.appendChild(title);
    dialogContainer.appendChild(content);
    dialogContainer.appendChild(buttonContainer);
    
    // 將對話方塊容器添加到文檔的 body 中
    document.body.appendChild(dialogContainer);
}
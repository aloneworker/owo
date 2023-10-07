function ajaxpost(name,says,urls)
{
    var dataToSend = [says];
    var xhr = new XMLHttpRequest();
    xhr.open('POST', urls, true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send('talks=' + encodeURIComponent(dataToSend));
    xhr.onreadystatechange = function() {

        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // 在這裡處理回應

            if (xhr.status === 200) {
                who = 'user'
                // 狀態碼200表示成功
                var response = JSON.parse(xhr.responseText); // 解析JSON回應

                // 在這裡處理回應
                var chat_what = response.response;
                var datas = response.datas;
                
                // 進行進一步的處理，例如將回應添加到您的網頁中
                return who ,chat_what ,datas ;
            } else {
                // 處理錯誤，例如顯示錯誤信息
                console.error('發生錯誤，狀態碼：' + xhr.status);
                
            }
        }
    };
    return 'error','',''
}
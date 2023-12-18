function tes(){
    console.log('ok');
}

function creatNotes(Da){
    // 假設 datas 是一個 JavaScript 對象，包含 items 陣列
    var datas = Da;
    // 選擇插入卡片的容器元素
    var container = document.getElementById("lis");
    container.innerHTML = "";
    $.each(datas, function(index, item) {
            var card = $('<div class="card" id="board"></div>');
            var cardBody = $('<div class="card-body"></div>').appendTo(card);

            // 添加日期
            $('<h5 class="card-title" id="date"></h5>').text(item[0]).appendTo(cardBody);

            $.each(item.slice(1), function(index, what) {
                var p = $('<p class="card-text"></p>');
                var span = $('<span class="badge"></span>').addClass(what.typs).text(what.tag).appendTo(p);
                p.append(' ' + what.title);

                if (what.typs == "bg-primary") {
                    p.attr("onclick", "showNote('" + what.title + "')");
                    p.attr("data-bs-toggle", "modal");
                    p.attr("data-bs-target", "#noteModal");
                }

                p.appendTo(cardBody);
            });

            card.appendTo("#lis");
        });
        
}

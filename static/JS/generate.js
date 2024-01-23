        // 立志的话数组，您可以根据需要添加更多的话语
        const inspirationalQuotes = [
            "每一天都是新的开始。",
            "不断学习，不断前进。",
            "坚持就是胜利。",
            "相信自己，你能做到。",
            "只要努力，没有做不到的事。",
            "動力的方法，試圖改變意識。",
            '在腦中投影 "期望的畫面"',
            "期望 要改寫成過去完成式",
            "試著打破自己內心的協定。",
            "在紙上寫下在意的事。",
            "將回憶改成好事。",
            "試著以日記的形式寫幻想的未來。",
            "遇到問題，問一問[潛意識]",
            "雙手合十，集中精神後，著手工作。",
            "開始非常仔細的做眼前的小事",
            "一天擁有跟自己開一次會的時間。",
            "如果認為「理所當然」，就試著懷疑。",


        ];

        // 随机选择一句立志的话
        function generateInspiration() {
            const randomIndex = Math.floor(Math.random() * inspirationalQuotes.length);
            return inspirationalQuotes[randomIndex];
        }

        // 将立志的话显示在页面上的<div>元素内
        function displayInspiration() {
            const divElement = document.getElementById("inspirationDiv");
            const quote = generateInspiration();
            divElement.innerHTML = `<p>${quote}</p>`;
        }


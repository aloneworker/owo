        // 立志的话数组，您可以根据需要添加更多的话语
        const inspirationalQuotes = [
            "每一天都是新的开始。",
            "不断学习，不断前进。",
            "坚持就是胜利。",
            "相信自己，你能做到。",
            "只要努力，没有做不到的事。",
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


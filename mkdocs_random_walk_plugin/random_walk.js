document.addEventListener("DOMContentLoaded", function () {
    setRandomLink();
  });
  
  window.addEventListener("pageshow", function (event) {
    if (event.persisted) {
      setRandomLink();
    }
  });
  
  document.addEventListener("visibilitychange", function() {
      if (document.visibilityState === "visible") {
        setRandomLink();
      }
  });
  
  function setRandomLink() {
      if (window.allNotePaths && window.allNotePaths.length) {
        // 获取随机链接
        let randomLink = window.allNotePaths[Math.floor(Math.random() * window.allNotePaths.length)];
    
        // 去掉后缀名
        let linkWithoutExtension = randomLink.split('.').slice(0, -1).join('.');
    
        // 检测当前网页的 URL 是否为本地地址
        const isLocal = window.location.href.includes("127.0.0.1") || window.location.href.includes("localhost");
    
        // 根据是否为本地地址修改链接
        if (isLocal) {
          linkWithoutExtension += ".html"; // 本地地址添加 .html
        }
    
        console.log("处理后的随机笔记链接: " + linkWithoutExtension);
        document.getElementById("randomLink").href = linkWithoutExtension;
      }
  }
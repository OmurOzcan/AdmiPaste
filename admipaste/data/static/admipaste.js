function darkStyle() {
    var head = document.head
      , link = document.createElement('link');

    link.type = 'text/css';
    link.rel  = 'stylesheet';
    link.href = "/static/admipaste-dark.css";
    link.id   = "darkStyle";

    head.appendChild(link)
}

(function() {
    var languageSelector = document.getElementById("languageselector");
    var darkButtonSelector = document.getElementById("darkToggle");
    var isDark = document.cookie.replace(/(?:(?:^|.*;\s*)darkTheme\s*\=\s*([^;]*).*$)|^.*$/, "$1");

    if (isDark == "") {
        document.cookie = "darkTheme=no";
    }

    if (languageSelector != null) {
        for (var language in Prism.languages) {
            if (language !== "extend" && language !== "insertBefore" && language !== "DFS") { //I guess it has these "functions" side by side with Languages.
                languageSelector.innerHTML += "<option value='" + language + "'>" + language + "</option>";
            }
        }
    }

    darkButtonSelector.onclick = function() {
        if (isDark === "no") {
            document.cookie = "darkTheme=yes;path=/";
            isDark = document.cookie.replace(/(?:(?:^|.*;\s*)darkTheme\s*\=\s*([^;]*).*$)|^.*$/, "$1");
            window.location.reload(true);
        } else {
            var darkStyleSel = document.getElementById("darkStyle");

            if (darkStyleSel !== null) {darkStyleSel.parentNode.removeChild(darkStyleSel);}
            document.cookie = "darkTheme=no;path=/";
            isDark = document.cookie.replace(/(?:(?:^|.*;\s*)darkTheme\s*\=\s*([^;]*).*$)|^.*$/, "$1");
            window.location.reload(true);
        }
    };
})();
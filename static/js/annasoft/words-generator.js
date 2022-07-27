var stopWordsList = [];

function beginCollectWords(){
    let inputPhrases = document.getElementById('input_key_phrase').value.split('\n');
    let main_window = document.getElementById('main_window');
    main_window.innerHTML = "";
    stopWordsList = [];
    showStopWordsList();
    let html = '';
    inputPhrases.forEach((item) => {
        let words = item.split(' ');
        let string = '';
        words.forEach((word) => {
            string += `<a class="as-main-wordlist" onclick="event.preventDefault();addStopWordWord('${word}');showStopWordsList();markWords('${word}');" style="padding-right: 5px;" href="#">${word}</a>`;
        });
        html += `<div>${string}</div>`;
    });
    main_window.innerHTML += html;
    if (main_window.innerHTML != '') {
        main_window.style.overflowY = 'scroll';
    };
};

function showStopWordsList() {
    let stopWordsListDiv = document.getElementById('stopWordsList');
    stopWordsListDiv.innerHTML = "";
    let html = "";
    stopWordsList.forEach((stopWord) => {
        html += `<div style="padding-right: 5px;">${stopWord}</div>`;
    });
    stopWordsListDiv.innerHTML += html;

};

function addStopWordWord(word) {
    if (contains(stopWordsList, word) == true) {
        stopWordsList.splice(stopWordsList.indexOf(word), 1);
    } else if (contains(stopWordsList, word) == false) {
        stopWordsList.push(word);
    };
};

function markWords(word) {
    let main_window = document.getElementById('main_window');
    let links =  main_window.getElementsByTagName('a');
    
    for (var i = 0; i < links.length; i++) {

        if (links[i].innerHTML == word) {
            if (contains(stopWordsList, word) === false) {
                links[i].style.backgroundColor = 'transparent';
            } else if (contains(stopWordsList, word) === true) {
                links[i].style.backgroundColor = '#E79090';
            };
            
        }; 
    };
};

function getStopWordList() {
    let stopWordListTextarea =  document.getElementById('stopWordList');
    stopWordListTextarea.value = "";
    let html = "";
    stopWordsList.forEach((stopWord) => {
        html += `${stopWord}` + '\n';
    });
    stopWordListTextarea.value += html;
    
};

function getWorkingWordList() {

    let workingWordListTextarea =  document.getElementById('workingWordList');
    let main_window = document.getElementById('main_window');
    workingWordListTextarea.value = "";
    let parent =  main_window.getElementsByTagName('div');
    let html = "";

    for (var i = 0; i < parent.length; i++) {
        let links =  parent[i].getElementsByTagName('a');
        string = "";
        for (var n = 0; n < links.length; n++) {
            if (contains(stopWordsList, links[n].innerHTML) == false) {
                string += links[n].innerHTML + " ";
            };
        };
        if (string != "") {
            html += `${string.trim()}` + '\n';
        };
    };

    workingWordListTextarea.value += html;
};

function deleteDouble() {

    let workingWordListPhrases =  document.getElementById('workingWordList').value.split('\n');
    let workingWordListPhrasesNew =  [];
    let workingWordListWithoutDoubles =  document.getElementById('workingWordListWithoutDoubles');

    let html = "";
    workingWordListPhrases.forEach((item) => {
        if (item != "") {
            if (contains(workingWordListPhrasesNew, item) == false) {
                workingWordListPhrasesNew.push(item);
                html += item + '\n';
            };
        };
    });
    workingWordListWithoutDoubles.value += html;
};

function contains(arr, elem) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === elem) {
            return true;
        };
    };
    return false;
};
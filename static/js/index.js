
const request = window.superagent;

const DATA_STORE = {
    input: sessionStorage.input ? sessionStorage.input : '',
    search_word: sessionStorage.input ? sessionStorage.input : '',
    resultList: [],
};


Vue.component('result-list', {
  props: ['resultItem'],
  template: '<li><a v-bind:href="\'/word/\' + resultItem.id" >{{ resultItem.word }} </a></li>'
});



new Vue({
    el: '#search-box',
    data: DATA_STORE,
    created: function (){
        getWords(this.search_word);
    },
    methods: {
        change: function () {
            this.search_word = this.input;
            console.log(this.input);
            sessionStorage.input = this.input;
            getWords(this.search_word);
        }
    }
});


function getWords(search_word){
    request.get('/words_filter/' + search_word)
    .then(res=>{
        console.log(res);
        DATA_STORE.resultList = res.body;
    })
    .catch(err=>{
        console.error(err);
        alert(err);
    })
}
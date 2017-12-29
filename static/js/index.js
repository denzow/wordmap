const DATA_STORE = {
    input: '',
    search_word: '',
    resultList: [
    ],
};


Vue.component('result-list', {
  props: ['resultItem'],
  template: '<li>{{ resultItem.word }}</li>'
});



new Vue({
  el: '#search-box',
  data: DATA_STORE,
  methods: {
    change: function () {
      this.search_word = this.input;
      // TODO access api

    }
  }
});
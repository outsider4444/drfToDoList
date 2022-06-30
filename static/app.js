Vue.createApp({
    el: '#app',
    data: {
        tasks: []
    },

    routes: [
    {
      path: '/blog',
      name: 'blog',
      component: Blog,
    }
  ],

    created: function () {
        const vm = this;
        axios.get('/api/')
            .then(function (response) {
                vm.tasks = response.data
            })
    }
})
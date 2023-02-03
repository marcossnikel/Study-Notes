[Official Documentation](https://router.vuejs.org/guide/)


Vue Router is a routing library for Vue.js that allows you to add routing to your single-page applications (SPAs). It works by mapping URLs to components, so that when a user visits a specific URL, the corresponding component is displayed.

Here's a high-level overview of how it works:

1.  Installation: First, you need to install the Vue Router library in your Vue.js project. You can do this using npm or yarn.
    
2.  Configuration: Next, you need to configure your routes. You do this by creating an instance of the Vue Router and defining your routes as an array of objects, each of which maps a URL path to a component.
    
3.  Integration: After configuring your routes, you need to integrate the Vue Router into your Vue.js application. You can do this by using the `router` option when creating a new Vue instance or by using the `Vue.use` function.
    
4.  Navigation: Once the Vue Router is integrated into your application, you can navigate between routes by using the `<router-link>` component or programmatically using the `router` instance.
    
5.  URL updates: When a user visits a URL, the Vue Router updates the URL and renders the corresponding component. It also updates the history stack in the browser, so that the user can use the back and forward buttons to navigate through their history.
    

The Vue Router also supports advanced features such as named routes, dynamic routes, nested routes, and lazy loading of components. By using these features, you can build complex, scalable routing systems for your Vue.js applications.


## HOW TO USE VUE ROUTER

1. Installation
``` 
 npm install vue-router
```

2. Configuration

```javascript
import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import About from './components/About.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About }
  ]
})

const app = createApp({
  setup() {
    return {
      router
    }
  }
})

```

3. Integration

```javascript
app.mount('#app')
```

4. Usage in templates:

```HTML
<template>
  <div id="app">
    <h1>Welcome to my App</h1>
    <p>
      <router-link to="/" class="router-link">Home</router-link>
      <router-link to="/about" class="router-link">About</router-link>
    </p>
    <router-view />
  </div>
</template>

```

#
In this example, we first import the Vue Router library and use it in our Vue 3 application. We then define two routes, each of which maps a URL path to a component. The `router-link` component is used to create links between routes, and the `router-view` component is used to render the component associated with the current route. When a user visits `/`, the `Home` component is displayed, and when they visit `/about`, the `About` component is displayed.


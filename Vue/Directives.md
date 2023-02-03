[Oficial Documentation](https://vuejs.org/api/built-in-directives.html#built-in-directives)


# Here are some of the directives.

1.  **v-bind:** Used to bind an expression to an attribute of an HTML element. For example, `v-bind:src` can be used to bind an image source.
    
2.  **v-on:** Used to bind a DOM event to a method or expression in the Vue instance. For example, `v-on:click` can be used to call a method when an element is clicked.
    
3.  **v-model:** A shorthand for `v-bind` and `v-on` combined. It creates a two-way data binding between a form input and a Vue instance property.
    
4.  **v-if:** Used to conditionally render an element based on the truthiness of an expression.
    
5.  **v-else:** Used in conjunction with `v-if` to render an element when the condition in `v-if` is falsy.
    
6.  **v-show:** Similar to `v-if`, but instead of removing the element from the DOM, it uses CSS to toggle the element's visibility.
    
7.  **v-for:** Used to loop over an array and render multiple elements. For example, `v-for="item in items"` can be used to render a list of items.
    
8.  **v-once:** When used, the expression it binds to will only be evaluated once and the result will be cached.
    
9.  **v-html:** Used to render HTML content within an element.
    
10.  **v-text:** Used to bind a text content to an element. It is similar to `v-html`, but instead of rendering HTML content, it renders plain text.
    
11.  **v-pre:** When used, it prevents the contents of an element from being compiled by the Vue template compiler.
    
12.  **v-cloak:** Used to hide un-compiled mustache expressions until the Vue instance has finished loading.
    
13.  **v-is:** Used to dynamically bind a component to an element based on the truthiness of an expression.
    
14.  **v-slot:** Used to specify a custom template for a component's content.
    
15.  **v-bind:class:** Used to bind a class to an element based on the truthiness of an expression.
    
16.  **v-bind:style:** Used to bind inline styles to an element based on the value of an expression.
    
17.  **v-on:click:** Used to bind a click event to a method in the Vue instance.
    
18.  **v-on:submit:** Used to bind a submit event to a method in the Vue instance.
    
19.  **v-model.lazy:** A modifier for `v-model` that makes it update on change events instead of input events.
    
20.  **v-model.number:** A modifier for `v-model` that automatically converts the input value to a number.


## Those directivities can also be some short hands approaches, like those.

1.  **v-bind:** `:`
2.  v-on: `@`
3.  v-model: No shorthand
4.  v-if: No shorthand
5.  v-else: No shorthand
6.  v-show: No shorthand
7.  v-for: No shorthand
8.  v-once: No shorthand
9.  v-html: No shorthand
10.  v-text: No shorthand
11.  v-pre: No shorthand
12.  v-cloak: No shorthand
13.  v-is: No shorthand
14.  v-slot: No shorthand
15.  **v-bind:class:** `.`
16.  v-bind:style: No shorthand
17.  **v-on:click:** `@click`
18.  **v-on:submit:** `@submit`
19.  v-model.lazy: No shorthand
20.  v-model.number: No shorthand
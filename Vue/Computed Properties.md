[Official Documentation](https://vuejs.org/guide/essentials/computed.html)

-  In Vue.js, a computed property is a function that returns a value that is dependent on one or more reactive data properties. Computed properties are cached based on their dependencies, so if none of their dependencies change, the computed value is returned from the cache, rather than re-computing the value.

## Here is an example of how you can use a computed property in Vue:

```HTML
<template>
  <div>
    <p>{{ fullName }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      firstName: 'John',
      lastName: 'Doe'
    }
  },
  computed: {
    fullName() {
      return `${this.firstName} ${this.lastName}`
    }
  }
}
</script>

```

-  In this example, the `fullName` computed property is defined as a function that concatenates the `firstName` and `lastName` data properties. When either of these data properties change, the `fullName` computed property will be re-computed, and the updated value will be displayed in the template.

## Best practices for using computed properties in Vue.js include:

1.  Caching: As described above, computed properties are cached based on their dependencies, so if none of their dependencies change, the computed value is returned from the cache, rather than re-computing the value. This makes computed properties a great choice for values that are expensive to compute, or that are used frequently in your application.
    
2.  Dependencies: Make sure that you only include the minimum number of dependencies required for your computed property to work. This will ensure that the computed property is re-computed only when necessary, and will keep your application running efficiently.
    
3.  Separation of Concerns: Use computed properties to separate logic that is used to display data from the data itself. This makes your code more maintainable and easier to understand.
    
4.  Read-Only: Computed properties are typically read-only, which means that you should not modify them directly. Instead, modify the data properties that the computed property depends on, and let Vue take care of re-computing the computed property for you.
In Vue, props (short for properties) are used to pass data from a parent component to its child components. The child component receives the data as a property, which it can then use in its template, computed properties, or methods.

Props are declared in the child component using the `props` option. This option takes an array of strings or objects that specify the names and types of the props the component accepts.

Here's an example of a child component that accepts a prop named "message":

<template>
  <div>{{ message }}</div>
</template>

<script>
export default {
  props: ['message']
}
</script>

And here's an example of how you might use this component in a parent component:

<template>
  <child-component :message="'Hello, World!'" />
</template>

<script>
import ChildComponent from './ChildComponent.vue'

export default {
  components: {
    ChildComponent
  }
}
</script>

In this example, the parent component passes the string "Hello, World!" as the value of the "message" prop to the `ChildComponent`.
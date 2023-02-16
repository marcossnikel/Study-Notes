[Solving Prop Drilling React](https://blog.logrocket.com/solving-prop-drilling-react-apps/)
[What is Prop Drilling](https://www.alura.com.br/artigos/prop-drilling-no-react-js)
[What is Prop Drilling 2](https://pt.stackoverflow.com/questions/424755/o-que-%C3%A9-prop-drilling)



Descrpition and example about prop drilling in Vue by our friend CHAT GPT:


- Prop drilling, also known as "props passing," is a technique in which data is passed from a parent component to a child component through multiple levels of components. The data is passed from parent to child through props, hence the name "prop drilling."

- Prop drilling can become cumbersome when there are multiple levels of components, as the data has to be passed down through each level. This can make the code harder to understand and maintain.

For example, consider the following code:

<!-- ParentComponent.vue -->
<template>
  <ChildComponentA :data="data" />
</template>

<script>
import ChildComponentA from './ChildComponentA.vue'

export default {
  components: {
    ChildComponentA
  },
  data() {
    return {
      data: { ... }
    }
  }
}
</script>

<!-- ChildComponentA.vue -->
<template>
  <ChildComponentB :data="data" />
</template>

<script>
import ChildComponentB from './ChildComponentB.vue'

export default {
  components: {
    ChildComponentB
  },
  props: ['data']
}
</script>

<!-- ChildComponentB.vue -->
<template>
  <div>{{ data.message }}</div>
</template>

<script>
export default {
  props: ['data']
}
</script>


- In this example, the data is passed from the `ParentComponent` to `ChildComponentB` through two intermediate components, `ChildComponentA`. This can become unwieldy if there are many more levels of components involved.
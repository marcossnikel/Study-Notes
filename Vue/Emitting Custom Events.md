[DOCUMENTATION](https://vuejs.org/guide/components/events.html)

In Vue.js, `emit` is used to trigger custom events on a component. It allows the parent component to listen for and respond to events that are emitted by its child components.

The `emit` method is called on a Vue instance and takes two arguments: the first is the name of the event, and the second is the data that should be passed along with the event.

Here's an example of a child component that emits a custom event named "increment" whenever a button is clicked:
<template>
  <div>
    <button @click="handleClick">Increment</button>
  </div>
</template>

<script>
export default {
  methods: {
    handleClick() {
      this.$emit('increment', 1)
    }
  }
}
</script>

And here's an example of a parent component that listens for the "increment" event emitted by the child component:

<template>
  <div>
    <child-component @increment="handleIncrement" />
    <div>{{ count }}</div>
  </div>
</template>

<script>
import ChildComponent from './ChildComponent.vue'

export default {
  components: {
    ChildComponent
  },
  data() {
    return {
      count: 0
    }
  },
  methods: {
    handleIncrement(value) {
      this.count += value
    }
  }
}
</script>








### User Card Component
```HTML
<script>

export default {

  props: {

    name: {

      type: String,

      default: "Marko Niko",

    },

    food: {

      type: String,

      default: "Lunch",

    },

  },

};

</script>

  

<template>

  <div>

    <h1>User : {{ name }}</h1>

    <p>Favorite Food: {{ food }}</p>

  </div>

</template>
```


### App.Vue
```HTML
<script>

import Counter from "./components/BaseCounter.vue";

import LearningListCounter from "./components/LearningListCounter.vue";

import OnePieceComponent from "./components/OnePieceComponent.vue";

import StatisticsModule from "./components/StatisticsModule.vue";

import UserCard from "./components/UserCard.vue";

  

export default {

  components: {

    Counter,

    OnePieceComponent,

    LearningListCounter,

    StatisticsModule,

    UserCard,

  },

  

  data: () => ({

    persons: {

      chars: [

        {

          name: "Luffy",

          age: 18,

          powers: ["Gum", "Haki", "Haoshoku", "Lightning"],

        },

        {

          name: "Zoro",

          age: 22,

          powers: ["Sword", "Haki", "Strengh", "Haoshoku"],

        },

        {

          name: "Nami",

          age: 22,

          powers: ["Lightning", "Zeus"],

        },

        {

          name: "Sanji",

          age: 28,

          powers: ["Kick", "Haki", "DNA"],

        },

        {

          name: "Robin",

          age: 31,

          powers: ["Knowledge", "Akuma no Mi", "Vision"],

        },

        {

          name: "Usopp",

          age: 23,

          powers: ["Vision", "Toxic Plants"],

        },

        {

          name: "Katakuri",

          age: 54,

          powers: [

            "Vision Haki",

            "Akuma no Mi",

            "Knowledge",

            "Vision",

            "Haoshoku",

          ],

        },

      ],

    },

    userData: {

      name: "marko",

      preferredFramework: "vue",

      favoriteFood: "meat",

      favoriteNumber: [7, 14, 21],

    },

  }),

  computed: {},

};

</script>

  

<template>

  <div>

    <user-card :name="userData.name" :food="userData.favoriteFood" />

    <counter />

    <one-piece-component :charsProp="persons.chars" />

    <learning-list-counter />

    <statistics-module :characters="persons.chars" />

  </div>

</template>
```


- Emits : equivalent of props , props says something like "this is what i´m expecting to send down" and emits are "this is what i´m gonna send up." -> Follows the one way data chain.
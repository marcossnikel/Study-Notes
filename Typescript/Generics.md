TypeScript generics allow you to write reusable, flexible, and type-safe code. They allow you to define a function, class, or interface that can work with multiple types, rather than being tied to a specific type.

In other words, generics provide a way to define a type placeholder that can be replaced with a real type when the code is compiled. The type placeholder can be any valid TypeScript type, including custom types, and is defined within angle brackets (`<T>`).

Here's an example of a generic function in TypeScript:

```typescript
function identity<T>(arg: T): T {
  return arg;
}

```

In this example, the `identity` function takes a single argument of type `T` and returns a value of the same type. To use this function, you need to specify the type that you want to use in place of `T`. For example:

```typescript
let output = identity<string>("hello");  // output has type string
let output2 = identity<number>(123);  // output2 has type number

```

Generics can also be used with classes and interfaces. Here's an example of a generic class:

```typescript
class GenericNumber<T> {
  zeroValue: T;
  add: (x: T, y: T) => T;
}

let myGenericNumber = new GenericNumber<number>();
myGenericNumber.zeroValue = 0;
myGenericNumber.add = function (x, y) { return x + y; };

```

In this example, the `GenericNumber` class can work with any type, as long as it's specified when creating an instance of the class. The `zeroValue` property and the `add` method both use the type `T`.

These are just a few examples of how you can use generics in TypeScript. With generics, you can write code that is flexible, reusable, and type-safe, making it easier to develop and maintain large applications.
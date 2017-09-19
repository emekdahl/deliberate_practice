function reverseWords(str) {
  return str.split("").reverse().join("").split(" ").reverse().join(" ");
}

reverseWords("This is an example!"); // returns  "sihT si na !elpmaxe"
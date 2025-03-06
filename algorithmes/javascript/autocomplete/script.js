import { TrieNode, insert, search } from './trie.js';
const root = new TrieNode();

document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("qryInput");
  const btn = document.getElementById("btn");
  const suggestions = document.getElementById("suggestions-container");
  const err = document.getElementById("err");
  let id = 0;
  
  btn.addEventListener("click", () => {
    let searchqry = input.value;
    insert(root, searchqry, id++);
    input.value = "";
    err.innerHTML = "Type Something ...";
    suggestions.innerHTML = "";
  });
  
  input.addEventListener("input", (event) => {
    console.log(event.target.value);
    if (event.target.value !== "") {
      err.innerHTML = "";
      let words = search(root, event.target.value);
      suggestions.innerHTML = "";
      words.forEach(element => {
        let li = document.createElement("li");
        li.textContent = element;
        li.classList.add("suggestion-item");
        suggestions.append(li);
      });
    } else {
      err.innerHTML = "Type Something ...";
      suggestions.innerHTML = "";
    }
  });
});

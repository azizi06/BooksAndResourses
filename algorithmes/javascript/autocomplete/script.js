import { TrieNode, insert, search } from './trie.js';
import { dictionaire_francais } from './dictionnaire_francais.js';
import { dictionnaire_anglais } from './dictionnaire_anglais.js';
const root = new TrieNode();
let words = ["algeria","azizi","word","tree","trend","trie","try","google","great","good"]
dictionnaire_anglais.forEach((element)=>{
  console.log(element)
  insert(root,element);
})
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

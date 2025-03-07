export class TrieNode {
    constructor(letter) {
      this.letter = letter;
      this.isWord = false;
      this.word = "";
      this.children = Array(26).fill(null);
    }
  }
  
  export function insert(root, qry) {
    if (qry === undefined || qry === null) return;
    let curr = root;
    qry = qry.toLowerCase();
    for (let c of qry) {
      let index = c.charCodeAt(0) - "a".charCodeAt(0);
      if (curr.children[index] === null) {
        curr.children[index] = new TrieNode(c);
      }
      curr = curr.children[index];
    }
    curr.isWord = true;
    curr.word = qry;
  }
  
  export function search(root, key) {
    let curr = root;
    
    key = key.toLowerCase();
    for (let c of key) {
      let index = c.charCodeAt(0) - "a".charCodeAt(0);
      if (curr.children[index] === null) return [];
      curr = curr.children[index];
    }
    let words = [];
    let nodes = [curr];
    let i =0;

    while (nodes.length && i <= 30) {
      let node = nodes.pop();
      if (node.isWord) words.push(node.word);
      for (let child of node.children) {
        if (child !== null) nodes.push(child);
      }
      i++
    }
    return words;
  }
  
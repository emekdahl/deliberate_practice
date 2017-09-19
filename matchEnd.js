function solution(str, ending) {
  pop_len = -ending.length;
  //console.log('The pop length is ', pop_len);
  str_seg = str.slice(pop_len);
  //console.log('The string segment is ', str_seg);
  
  if(str_seg === ending){
    return true;
  } else {
    return false;
  }
}

solution('abc','bc');
function solution(str, ending) {
  var popLen = -ending.length;
  //console.log('The pop length is ', popLen);
  var strSeg = str.slice(popLen);
  //console.log('The string segment is ', strSeg);
  
  if (strSeg === ending) {
    return true;
  } else {
    return false;
  }
}

solution('abc','bc');
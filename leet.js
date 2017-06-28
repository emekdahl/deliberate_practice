function toLeetSpeak(str) {
  //split the String
  var splitStr = str.split('');
  var strArray = [];
  var leet = {
    A : '@',
    B : '8',
    C : '(',
    D : 'D',
    E : '3',
    F : 'F',
    G : '6',
    H : '#',
    I : '!',
    J : 'J',
    K : 'K',
    L : '1',
    M : 'M',
    N : 'N',
    O : '0',
    P : 'P',
    Q : 'Q',
    R : 'R',
    S : '$',
    T : '7',
    U : 'U',
    V : 'V',
    W : 'W',
    X : 'X',
    Y : 'Y',
    Z : '2',
    ' ' : ' '
  };
  
  for (var i = 0; i < str.length; i++) {
    strArray.push(leet[splitStr[i]]);
  }
  return strArray.join('');
}

toLeetSpeak('LEET');
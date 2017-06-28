
    var items = [
    {id: 1, body: 'foo'},
    {id: 2, body: 'bar'},
    {id: 3, body: 'foobar'}
    ];

//var result = new Map(arr.map((i) => [i.key, i.val]));
    // var ids = items.map((i) => [i,i.id]);
    var ids = items.map(function(item) {
      return item.id;
    });
    console.log(ids);

    var otherIds = items.map(item => item.id);
    console.log(otherIds);
 
  
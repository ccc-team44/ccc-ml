function(keys, values, rereduce) {
  let result = 0;
  if (rereduce) {
    values.forEach(function (v) {
      result += v;
    });
  } else {
    values.forEach(function (vObj) {
      result += vObj.followers;
    });
  }
  return (result);
}
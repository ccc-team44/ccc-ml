function(doc) {
  if( doc.text) {
    emit(doc._id, {
        text: doc.text,
        screen_name: doc.screen_name
    });
  }
}
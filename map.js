function (doc) {
  emit(doc.user.id,
    {followers: doc.user.followers_count});
}
# test_parent
* Test

  ```
  $ git clone git@github.com:hyunjun/test_parent.git
  Cloning into 'test_parent'...
  remote: Counting objects: 18, done.
  remote: Compressing objects: 100% (10/10), done.
  remote: Total 18 (delta 3), reused 17 (delta 2), pack-reused 0
  Receiving objects: 100% (18/18), done.
  Resolving deltas: 100% (3/3), done.
  Checking connectivity... done.
  $ cd test_parent/

  test_parent $ git submodule init
  Submodule 'test_child' (git@github.com:hyunjun/test_child.git) registered for path 'test_child'
  test_parent $ git submodule update
  Cloning into '/Users/jun/programming/test_parent/test_child'...
  Submodule path 'test_child': checked out
  'afe0b94c9b70fe1ed67f4958d129b9bb78708e54'

  test_parent jun$ python parent_module/src/parent_module.py
  foo
  bar
  baz
  ```

{
  "targets": [
    {
      "target_name": "hello-world",
      "sources": [ "main.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}

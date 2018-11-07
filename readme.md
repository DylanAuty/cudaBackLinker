# cudaBackLinker

A python script to deal with things that want CUDA 9.0 when 10.0 is installed. Does this by symlinking all CUDA 10.0 lib files to 9.0, leaning heavily on an assumption of backwards compatibility.

## Usage
`python3 cudaBackLinker.py /path/to/cuda/lib64`

or 

`python3 cudaBackLinker.py -h` if you get stuck.

CUDA lib64 is normally at `/usr/local/cuda/lib64` but may be somewhere else for you.

## When to use this
* Getting errors like [this](https://github.com/tensorflow/tensorflow/issues/15604) complaining about not being able to find `lib<something>.so.9.0`? 
* Feeling like using unsupported versions of CUDA despite what the docs for your framework are telling you to do? 

Then this may be useful. It also will probably break something else somewhere else, so **if something goes wrong then downgrade to the recommended version of CUDA first.**

## Why (not) to use this

NVIDIA claim that CUDA driver is backwards compatible, but that the runtime *may* not be ([here](https://docs.nvidia.com/deploy/cuda-compatibility/index.html)) and ([here](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html)). Even so, if you want to try then this may make your life easier. It may also make your life way harder. Your mileage may vary.


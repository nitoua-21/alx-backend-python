![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/f088970b450e82c881ea.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20241104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241104T185440Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5f4cd0bba489480282f468fe3947180c1d17610e8936ee1c2051b418e15f191f)

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

    $ python -m unittest path/to/test_file.py
    

Resources
---------

**Read or watch:**

*   [unittest — Unit testing framework](/rltoken/a_AEObGK8jeqPtTPmm-gIA "unittest — Unit testing framework")
*   [unittest.mock — mock object library](/rltoken/PKetnACd7FfRiU8_kpe5EA "unittest.mock — mock object library")
*   [How to mock a readonly property with mock?](/rltoken/2ueVPK1kWZuz525FvZ1v2Q "How to mock a readonly property with mock?")
*   [parameterized](/rltoken/mI7qc3Y42aZ7GTlLXDxgEg "parameterized")
*   [Memoization](/rltoken/x83Hdr54q4Vax5xQ2Z3HSA "Memoization")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/NfT-nNKrNHGrDMY-Qm-1Dg "explain to anyone"), **without the help of Google**:

*   The difference between unit and integration tests.
*   Common testing patterns such as mocking, parametrizations and fixtures

Requirements
------------

*   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `pycodestyle` style (version 2.5)
*   All your files must be executable
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
*   All your functions and coroutines must be type-annotated.


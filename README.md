# nose-progress

Give you tests a progress before testcase name

Like this:

(venv) F:\Work>nosetests -v -s unite_progress.py --with-scheduling

[1/3] test_progress ... ok

[2/3] test_sample (unite_progress.TestSequenceFunctions) ... ok

[3/3] test_shuffle (unite_progress.TestSequenceFunctions) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.004s

OK

Use

nosetests --with-scheduling

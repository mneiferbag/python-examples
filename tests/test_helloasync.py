def test_helloasync(capsys):
    import mncpyexamples.asynchello.helloasync as helloasync
    helloasync.run_main()
    captured = capsys.readouterr()
    assert captured.out == "Hello ...\n... World!\n"

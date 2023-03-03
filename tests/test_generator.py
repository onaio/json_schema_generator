import json
import subprocess


def capture(command):
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    return out, err, proc.returncode


def test_no_param():
    command = ["json_schema_generator"]
    out, err, exitcode = capture(command)
    # command line error
    assert exitcode == 2
    # empty byte type success return
    assert out == b""
    # appropriate byte type errors
    assert b"usage: json_schema_generator [-h] --source sample.json" in err
    assert b"error: the following arguments are required: --source" in err


def test_param_not_file():
    command = ["json_schema_generator", "--source", "random"]
    out, err, exitcode = capture(command)
    assert exitcode == 2
    assert out == b""
    assert b"No such file or directory: 'random'" in err


def test_invalid_json_file():
    command = [
        "json_schema_generator",
        "--source",
        "tests/fixtures/invalid_json_syntax.json",
    ]
    out, err, exitcode = capture(command)
    assert exitcode == 1
    assert out == b""
    assert b"Error: Source file could not be read. Pass in a valid JSON file" in err


def test_not_json_array():
    command = [
        "json_schema_generator",
        "--source",
        "tests/fixtures/not_json_array.json",
    ]
    out, err, exitcode = capture(command)
    assert exitcode == 1
    assert out == b""
    assert (
        b"Error: Source file validation failed. Pass in a valid list of JSON objects"
        in err
    )


def test_success():
    command = [
        "json_schema_generator",
        "--source",
        "sample_files/sample.json",
    ]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert err == b""
    assert json.loads(out) == json.load(open("sample_files/schema.json"))

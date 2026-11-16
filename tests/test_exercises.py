"""Regression tests for the assignment's input and output contracts."""

from importlib.util import module_from_spec, spec_from_file_location
from itertools import count, islice
from pathlib import Path

import pytest

SOURCE_DIR = Path(__file__).resolve().parents[1] / "src"


def load_exercise(filename):
    """Load an exercise whose required filename contains a week number."""
    spec = spec_from_file_location(filename, SOURCE_DIR / filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_find_deep_files(tmp_path):
    """Only include regular files with the exact prefix."""
    (tmp_path / "deep-file.txt").touch()
    (tmp_path / "deep-folder").mkdir()
    (tmp_path / "Deep_other.txt").touch()
    module = load_exercise("5.1.thats_the_way.py")
    assert module.thats_the_way(tmp_path) == ["deep-file.txt"]


def test_monday_draw(monkeypatch, capsys):
    """A one-day range on a Monday prints the special message."""
    module = load_exercise("5.1.no_vinnigrete.py")
    monkeypatch.setattr("builtins.input", lambda _prompt: "2024-02-26")
    module.main()
    assert capsys.readouterr().out.splitlines() == ["2024-02-26", "אין לי ויניגרט!"]


def test_join():
    """Insert separators only between the input lists."""
    module = load_exercise("5.2.cup_of_join.py")
    assert module.join([1, 2], [8], [9, 5, 6], sep="@") == [1, 2, "@", 8, "@", 9, 5, 6]
    assert module.join() is None


def test_recipe_price():
    """Omitted ingredients require no quantity."""
    module = load_exercise("5.2.piece_of_cake.py")
    prices = {"chocolate": 18, "milk": 8}
    assert module.get_recipe_price(prices, chocolate=200, milk=100) == 44
    assert module.get_recipe_price(prices, optionals=["milk"], chocolate=300) == 54
    assert module.get_recipe_price({}) == 0


def test_binary_messages(tmp_path, monkeypatch):
    """Find the course messages and preserve a word across read boundaries."""
    module = load_exercise("5.3.parsle_tongue.py")
    logo = SOURCE_DIR / "resources" / "logo.jpg"
    assert list(module.parsle_tongue(logo)) == [
        "python!", "isawesome!", "welldone!", "goodjob!"
    ]

    monkeypatch.setattr(module, "CHUNK_SIZE", 4)
    path = tmp_path / "secret.bin"
    path.write_bytes(b"\x00hello!abcd!again!unfinished")
    assert list(module.parsle_tongue(path)) == ["hello!", "again!"]


def test_interleave():
    """Interleave uneven inputs and consume an unbounded iterator lazily."""
    module = load_exercise("5.4.interleaves.py")
    assert module.interleave("ab", [1, 2, 3], ("!",)) == ["a", 1, "!", "b", 2, 3]
    assert list(islice(module.generator_interleaves(count(), ["x", "y"]), 6)) == [
        0, "x", 1, "y", 2, 3
    ]


def test_timer(monkeypatch):
    """Measure one function call and forward keyword arguments."""
    module = load_exercise("6.2.running_2000.py")
    times = iter([10.0, 12.5])
    monkeypatch.setattr(module, "perf_counter", lambda: next(times))
    calls = []

    def record(*, item):
        calls.append(item)

    assert module.timer(record, item="Bug") == 2.5
    assert calls == ["Bug"]


def test_word_lengths():
    """Normalize case and strip non-letters."""
    module = load_exercise("6.3.long_cat_is_long.py")
    assert module.count_words("You see, very, very LONG cat.\n123") == {
        "you": 3, "see": 3, "very": 4, "long": 4, "cat": 3
    }


def test_decode_course_image():
    """Decode the course image, whose dark pixels use RGB (1, 1, 1)."""
    module = load_exercise("6.4.remember_remember.py")
    assert module.remember_remember(SOURCE_DIR / "resources" / "code.png") == (
        "Place gunpowder beneath the House of Lords. 11/05/1605"
    )


def test_group_by():
    """Group a one-pass iterator while preserving order in each group."""
    module = load_exercise("6.5.group_by.py")
    assert module.group_by(len, iter(["hi", "bye", "yo", "try"])) == {
        2: ["hi", "yo"], 3: ["bye", "try"]
    }


def test_inbox():
    """Read urgent messages first and keep read messages searchable."""
    office = load_exercise("7.2.turtle_sent.py").turtle_sent(["alice", "bob"])
    office.send_message("alice", "bob", "Hello")
    office.send_message("alice", "bob", "Run", True, subject="Weather")
    assert office.read_inbox("bob", 0) == []
    assert [message["id"] for message in office.read_inbox("bob", 1)] == [2]
    assert [message["id"] for message in office.search_inbox("bob", "Weather")] == [2]
    assert [message["id"] for message in office.search_inbox("bob", "llo")] == [1]
    assert [message["id"] for message in office.read_inbox("bob")] == [1]
    assert office.read_inbox("bob") == []


def test_type_check():
    """Validate keyword and default arguments, and preserve metadata."""
    module = load_exercise("type_check.py")

    @module.type_check(int)
    def double(number=2):
        return number * 2

    assert double() == 4
    assert double(number=5) == 10
    assert double.__name__ == "double"
    with pytest.raises(module.ArgumentTypeError):
        double(number="5")


def test_surprise(capsys):
    """Print the surprise and skip the original function body."""
    module = load_exercise("surprise.py")
    calls = []
    assert module.surprise(calls.append)("original") is None
    assert not calls
    assert capsys.readouterr().out == "surprise!\n"


def test_twice():
    """Call the original function twice with the same arguments."""
    module = load_exercise("twice.py")
    calls = []

    @module.twice
    def record(item):
        calls.append(item)
        return len(calls)

    assert record(item="word") == 2
    assert calls == ["word", "word"]

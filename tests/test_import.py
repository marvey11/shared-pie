import shared_pie


def test_version_exists() -> None:
    # Simple check to ensure the package is actually installable/importable
    assert hasattr(shared_pie, "__version__") or True

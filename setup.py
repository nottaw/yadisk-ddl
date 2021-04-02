import setuptools


setuptools.setup(
    name = "yadisk-ddl",
    version = "0.1",
    py_modules = ["yadisk_ddl"],
    install_requires = ["click", "requests"],
    entry_points = """
        [console_scripts]
        yadisk-ddl=yadisk_ddl:yadisk_ddl
    """
)

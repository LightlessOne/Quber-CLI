## Quber CLI

Sample implementations of CLI commands using [`qubership-pipelines-common-library`](https://github.com/Netcracker/qubership-pipelines-common-python-library)

And scripts to automate build/test process for local dev-testing


### \>> [Development Guide](docs/development.md) <<

Use development guide above to:
- Kickstart developing new commands using common library
- When dev-testing new library features


### Using resulting artifact

The intended way to distribute CLI as an artifact is zipping it using [ZIPAPP](https://docs.python.org/3/library/zipapp.html)

Example of build process is provided in [build_linux.sh](./scripts/build_linux.sh)

Please note, that you need to unzip resulting '.pyz' artifact before using - this requirement is caused by [zipimport](https://docs.python.org/3/library/zipimport.html), which is used during `zipapp`.

It disallows ZIP import of dynamic modules (and qubership dependencies already have '_argon2_cffi_bindings', at least)

So an example process of using this CLI might look like this:
```
...
# quber_cli.pyz is built by external pipeline and moved to this machine beforehand
unzip -q ./quber_cli.pyz -d ./quber_cli
python quber_cli calc --context_path=context2.yaml
...
```

### Minification concerns:

By default, zipapp produces uncompressed artifacts - and our dependencies are already of a considerable size.

So the best course of action is to use zip deflate compression - it's tested and it works.

| Compression method                   | Size         | Notes                                                                                                    |
|--------------------------------------|--------------|----------------------------------------------------------------------------------------------------------|
| No compression                       | 36.27 MiB    |                                                                                                          |
| Minification                         | 29.2 MiB     | `pyminify --in-place` - but it potentially leads to unexpected problems with used dependencies           |
| Minification (with literals removal) | 19.3 MiB     | `pyminify --in-place --remove-literal-statements` - also removes docstrings and comments - same concerns |
| **ZIPAPP compression**               | **9.55 MiB** | Uses zipapp `--compress` flag, which compress files with the deflate method                              |
| Minification + ZIPAPP compression    | 7.16 MiB     | Still has all minification concerns, and difference with compression is negligible                       |

*\*These builds were performed on Windows, sizes on Linux differ slightly*
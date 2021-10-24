## Upload Package Guide

1. Go to Package file where `setup.py` file exist.

```bash
cd datascienv
```

2. Generate the wheel file and dist env.

```bash
python setup.py sdist bdist_wheel
```

3. Once `dist/*` folder generated successfully. Time to upload with twine

```bash
twine upload dist/*
```

4. Your package uploaded successfully.

![](img\success.jpg)

5. When you want to update the package must update version in `setup.py` file.

![](img\version.jpg)

6.  update package on `pypi`.

* For build package again follow the step 2 and then use below command to upload packages.

```bash
twine upload --repository-url https://upload.pypi.org/legacy/ dist/* --skip-existing
```


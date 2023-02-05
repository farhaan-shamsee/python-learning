# Input types in Python

Below code will ask for input and convert into float and show the output.

```python
print('The sum is %.1f' % (float(input('Enter first number: ')) + float(input('Enter second number: '))))
```

## Taking input from command line

For this we use argv function from sys library.

```python
sys.argv[1]
```

The 1st arg is always file name that is at 0th position.

Rest are the inputs passed from command line.

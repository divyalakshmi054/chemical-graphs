# Graph Verification
Application to verify graphs against various models

## Usage

```sh
./UserInterface/CLI.py <template file> <input file> [-p,--position] [-e,--error FLOAT FLOAT] [-r,--rate FLOAT] 
```
### Parameters
- **[template file]**: 2 column CSV file of float values containing the perfect graph
- **[input file]**: 2 column CSV file of float values containing the input graph
- **-p, --position**: Enable only if position is to be checked along with slope. Not enabling will only compare slope
- **-e, --error**: Permissible error margin along `x` and `y` coordinate
- **-r, --rate**: Floating point value between 0 and 1 for rate of completion. High value will result in faster completion but lower accuracy.

### Example Usage
```
./UserInterface/CLI.py UserInterface/input.csv UserInterface/template.csv -p -e 2 2 -r 0.5
```

## Future Updates

- Database of some sample perfect graphs for easy access
- Webapp for interactive UI and graph plotting
- Testing code
- Docker
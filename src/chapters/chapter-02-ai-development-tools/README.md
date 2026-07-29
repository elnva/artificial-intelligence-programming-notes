# Chapter 02 — AI Development Tools

> Book chapter: **Chapter 2 — AI Development Tools**.
>
> Book Chapter 1 is read-only background, so the hands-on work in this repo starts at Chapter 2. Folder names match book chapter numbers from here on.

## Goal

By the end of this chapter you will:

- Know what every category of AI tool the chapter discusses is for, in your own words: hardware, programming language, IDE, virtual environment, dataset, framework.
- Have a working Python 3.10 virtual environment with the core scientific libraries installed (NumPy, pandas, Matplotlib, Jupyter, scikit-learn).
- Have hand-typed every Python micro-example the chapter introduces — Hello World, comments, variables, loops, conditionals, functions, input, the `math` library, plotting with Matplotlib, and reading/writing CSV and Excel files with pandas.
- Have a short shortlist of which datasets and frameworks you intend to revisit later, written into your `notes.md`.

## Modernization vs. the book

The book targets Python 3.6.8 on Windows with IDLE and Notepad++. We modernize three things while keeping the lessons intact:

| Book | This repo | Why |
| ---- | --------- | --- |
| Python 3.6.8 | Python 3.10.20 (via pyenv) | 3.6 is end-of-life; 3.10 is the lowest version still supported by current TensorFlow / scikit-learn / OpenCV. |
| Windows IDLE | macOS terminal + VS Code | You are on a Mac, and VS Code is the most widely used Python editor today. |
| Global `pip install ...` | `venv` per project | Avoids polluting the system Python and version conflicts between projects. |

If a code example in the book breaks on 3.10, note it in `notes.md` and we patch it in chat.

## Chapter outline (book sections you will cover)

- 2.1 AI Hardware Tools — CPU, GPU, FPGA, IPU
- 2.2 AI Software Tools — programming languages and library landscape
- 2.3 Introduction to Python — installation and the standard scientific stack
- 2.4 Python Development Environments + a quick Python tour (Hello World, loops, ifs, functions, input, math, plotting, CSV/Excel)
- 2.5 AI Datasets — where to get data
- 2.6 Python AI Frameworks — Scikit-Learn, TensorFlow, Keras, PyTorch and friends
- 2.7 Summary
- 2.8 Chapter Review Questions

## How to read the steps

Each step has four parts:

1. **Teach** — a short explanation of what the step is about and why it matters.
2. **Do** — the concrete action you take.
3. **Expected** — what you should see if it worked.
4. **Tell me when done** — your cue to ping Claude so the next step gets unlocked.

Do not skim ahead. The point is to absorb each idea before moving on.

## Steps

### Step 1 — Read book sections 2.1 and 2.2 (hardware and software landscape)

- **Teach**: Before touching any code, you should be able to answer two questions in plain language: "what hardware does AI run on, and why does it matter?" and "why is Python the dominant language for AI today?" Section 2.1 walks through standard CPUs, GPUs, FPGAs, and Graphcore's IPU; section 2.2 surveys C/C++, Java, C#, Python, MATLAB, R, Julia, and Go for AI work.
- **Do**: Read book pages covering 2.1 and 2.2. In `notes.md` (next to this README), under **Insights**, write two or three sentences in your own words: one on the hardware spectrum (CPU vs. GPU vs. specialized accelerators) and one on why Python won for AI despite being interpreted and slower than C++.
- **Expected**: A few short bullet points in `notes.md`. No code yet.
- **Tell me when done**: reply with `step 1 done`.

### Step 2 — Confirm the Python virtual environment is alive

- **Teach**: A virtual environment (`venv`) gives this project its own isolated Python and its own set of installed libraries, so installing TensorFlow here does not touch any other project on your laptop. Section 2.4 of the book recommends Virtualenv; Python's built-in `venv` is the modern equivalent and ships with Python itself. The book uses Python 3.6.8; we use Python 3.10.20 via pyenv.
- **Do**: Open a terminal in the repo root and run:
  ```bash
  cd ~/src/artificial-intelligence-programming-notes
  python -m venv .venv
  source .venv/bin/activate
  python --version
  pip install --upgrade pip
  ```
  If `.venv` already exists from earlier attempts, you can skip the `python -m venv` line.
- **Expected**: `python --version` prints `Python 3.10.20`. Your shell prompt now shows `(.venv)` somewhere on the line.
- **Tell me when done**: reply with `step 2 done`.

### Step 3 — Install the core scientific stack

- **Teach**: The book installs eight libraries up front and uses them throughout the rest of the chapter: NumPy for arrays, pandas for tabular data, Matplotlib for plots, Jupyter for notebooks, IPython for an enhanced interactive shell, SciPy for scientific algorithms, SymPy for symbolic math, and a tester. We will install the same set, plus scikit-learn since the book installs it on the next page. We will also install `xlsxwriter` because one of the chapter examples writes Excel files. We pin nothing yet — pinning happens later when something actually breaks.
- **Do**: With `(.venv)` active, run:
  ```bash
  pip install numpy pandas matplotlib jupyter ipython scipy sympy scikit-learn xlsxwriter
  pip list
  ```
  Then save the current state to `requirements.txt`:
  ```bash
  pip freeze > requirements.txt
  ```
- **Expected**: `pip list` shows all the libraries above (and many transitive deps). `requirements.txt` is no longer the empty placeholder.
- **Tell me when done**: reply with `step 3 done`.

### Step 4 — Pick your editor

- **Teach**: The book's section 2.4 lists ten editors / IDEs (Notepad++, TextPad, Sublime, Atom, PyCharm, Spyder, VS Code, Jupyter, Google Colab, Kaggle). For this chapter we keep things simple: use VS Code with the official Python extension. Later chapters will use Jupyter when notebooks are clearer than scripts; the book itself bounces between IDLE, Jupyter, Colab, and Kaggle, and you will see all of them.
- **Do**: Make sure you have VS Code installed (`code --version` in the terminal). Open the repo with `code .` from inside the repo root. If the Python extension is not installed, install it from the Extensions panel. Then click the Python interpreter selector in the bottom-right of VS Code and pick the one whose path ends in `.venv/bin/python`.
- **Expected**: VS Code shows `Python 3.10.20 ('.venv': venv)` in the bottom status bar.
- **Tell me when done**: reply with `step 4 done`.

### Step 5 — Hello World (Example 2.1)

- **Teach**: Every language tour starts here. The point is not the greeting; the point is that Python prints to standard output with a single function call and no boilerplate — no `main`, no semicolons, no compile step. This is also your first chance to confirm the editor → save → run loop works.
- **Do**: In `examples/` (next to this README), open the file `01-hello.py`. Type a one-line `print` statement that outputs `Hello World!`. Run it with:
  ```bash
  python src/chapters/chapter-02-ai-development-tools/examples/01-hello.py
  ```
- **Expected**: Terminal prints `Hello World!`.
- **Tell me when done**: reply with `step 5 done`.

### Step 6 — Comments and variables (Examples 2.2, 2.3)

- **Teach**: The book splits this into two tiny files. First (`02-hello2.py`) it shows Python's two comment forms: `#` for a single line, triple quotes `'''...'''` for a block. Then (`03-hello3.py`) it shows that variables don't need type declarations, that `+` adds numbers and concatenates strings, and that you don't need a semicolon at the end of a line. This is where Python's pythonic mindset starts: dynamic typing, line-by-line execution, almost no boilerplate.
- **Do**:
  1. Open `02-hello2.py`. Write a single-line `#` comment, then a triple-quoted block comment, then a single `print` of `Hello World`.
  2. Open `03-hello3.py`. Define three integer variables, sum two of them, print the result with a label. Then two single-character string variables, concatenate with `+`, print. Then two longer string variables, join them with a space, print.
- **Expected**: Two files run cleanly. `02-hello2.py` prints one line; `03-hello3.py` prints three.
- **Tell me when done**: reply with `step 6 done`.

### Step 7 — Loops: `for`, nested `for`, `while` (Examples 2.4, 2.5, 2.6)

- **Teach**: Python uses indentation, not braces, to express block structure. Four spaces is the convention. The book shows three loop forms in three files: a flat `for` over `range(5)` (`04-loop.py`), a nested `for` over `range(5)` × `range(5)` printing `i*j` (`05-loop2.py`), and a `while` that increments a counter until it fails the condition (`06-loop3.py`).
- **Do**: Open the three files in order and write each loop. End each script with a `print("Finished")` so you can see the loop exit.
- **Expected**: All three files run cleanly. If Python complains about indentation, that is the lesson — fix it and rerun.
- **Tell me when done**: reply with `step 7 done`.

### Step 8 — Conditionals (Example 2.7)

- **Teach**: `if`, `elif`, `else` — same shape as the loops, no parentheses around the condition, colon ends the line, indented body. The book's example grades a number into Excellent / Good / OK.
- **Do**: Open `07-ifelse.py`. Set a variable `x = 60`, branch on `x >= 70` → Excellent, `x >= 60` → Good, otherwise OK. Run it. Then change `x` to 75 and 50 and run again to confirm all three branches fire.
- **Expected**: Output changes between the three labels depending on `x`.
- **Tell me when done**: reply with `step 8 done`.

### Step 9 — Functions and Exercises 2.1, 2.2 (Examples 2.8, 2.9)

- **Teach**: Functions in Python use `def name(args):`. Example 2.8 (`08-funcs.py`) shows a two-argument `add` that takes `x` and `y` and returns the sum. Example 2.9 (`09-array.py`) introduces lists (what Python calls arrays) and walks through one to find the maximum value. Functions are where the book's exercises start, so this step also asks you to do two of them.
- **Do**:
  1. Open `08-funcs.py`. Define `add(x, y)` that returns `x + y`. Call it once and print the result.
  2. Open `09-array.py`. Define `maxarray(xs)` that loops through a list and returns the largest element. Test on `[0, 1, 2, 3, 4, 5]`.
  3. **Exercise 2.1** — Open `exercises/ex-2-1-minarray.py`. Write `minarray(xs)` that returns the minimum.
  4. **Exercise 2.2** — Open `exercises/ex-2-2-sortarray.py`. Write `sortarray(xs)` that returns the list sorted ascending. Try a hand-rolled loop sort first, then `sorted()`. Note in `notes.md` which you preferred and why.
- **Expected**: All four files run; outputs are sensible.
- **Tell me when done**: reply with `step 9 done`.

### Step 10 — Input from the keyboard, type conversion, Exercises 2.3, 2.4 (Examples 2.10, 2.11, 2.12)

- **Teach**: `input()` reads a line of text from the keyboard. Everything it returns is a string, so for arithmetic you must convert with `int()` or `float()`; to embed a number back into a printed string, use `str()`. The book's third file in this set (`12-inputlist.py`) introduces `split()` and `map()` to read a whole list of numbers in one line.
- **Do**:
  1. Open `10-input.py`. Ask the user's name with `input()`, greet them by concatenating strings.
  2. Open `11-input2.py`. Ask for a number, convert with `int()`, square it with `**`, print as a sentence.
  3. Open `12-inputlist.py`. Ask for several space-separated numbers, parse them into a list of integers via `list(map(int, s.split()))`.
  4. **Exercise 2.3** — Open `exercises/ex-2-3-square-float.py`. Same as `11-input2.py` but with `float()`.
  5. **Exercise 2.4** — Open `exercises/ex-2-4-record.py`. Read a name (string), age (int), marks (float). Print all three back.
- **Expected**: Each program prompts you, accepts your input, prints a meaningful result.
- **Tell me when done**: reply with `step 10 done`.

### Step 11 — The `math` library and Exercise 2.5 (Example 2.13)

- **Teach**: Python's standard library is huge. `math` is the first module you meet. You import it with `import math` and use dotted access — `math.pi`, `math.sqrt`, `math.factorial`, `math.floor`, `math.ceil`, `math.sin`. The point: most things you need already exist; you find them, you don't reinvent them.
- **Do**:
  1. Open `13-math.py`. With `r = 5`, compute the circumference of a circle (`2 * math.pi * r`). Compute `math.sqrt(5)`, `math.factorial(7)`, `math.floor(16.4)`, `math.ceil(16.4)`. Print each labeled.
  2. **Exercise 2.5** — Open `exercises/ex-2-5-sines.py`. Read a list of floats from the keyboard (reuse the `split`/`map` pattern from step 10, but with `float`), compute `math.sin` of each, print the results.
- **Expected**: Five labeled numeric outputs in `13-math.py`; one line per input number in the exercise.
- **Tell me when done**: reply with `step 11 done`.

### Step 12 — Plotting with Matplotlib and Exercise 2.6 (Examples 2.14, 2.15)

- **Teach**: Matplotlib is Python's most popular plotting library. The book introduces it in two steps: a single sine curve (`14-plot.py`), then a two-line plot of sine and cosine with custom colors, markers, and a legend (`15-plot2.py`). NumPy comes in here too — `np.linspace`, `np.sin`, `np.cos` give you vectorized math over arrays without writing a loop.
- **Do**:
  1. Open `14-plot.py`. Use `np.linspace(0, 2*np.pi, 100)` (cleaner than the book's manual scaling), compute `y = np.sin(x)`, plot, set title and axis labels, show.
  2. Open `15-plot2.py`. Plot sine in blue with `s` markers and cosine in red with `o` markers between `-π` and `π`, add a legend.
  3. **Exercise 2.6** — Open `exercises/ex-2-6-three-curves.py`. On the same axes, plot `y = 3x + 4`, `y = 2x² + 1`, and `y = x³ + 9` over a range you pick, with three different colors and a legend.
- **Expected**: Three plot windows pop up (or three inline figures if you switch to a notebook). Legends visible, colors distinct.
- **Tell me when done**: reply with `step 12 done`.

### Step 13 — Reading and writing CSV with pandas (Examples 2.16, 2.17)

- **Teach**: CSV is the lingua franca of tabular data. pandas wraps the messy parts: `pd.DataFrame(...)` builds a table from a dict of columns, `df.to_csv(path, index=False)` writes it, `pd.read_csv(path)` reads it back. The `index=False` argument suppresses pandas' default row-index column, which is almost always what you want when handing the file to anyone else.
- **Do**:
  1. Open `16-data.py`. Build a DataFrame with two columns `Name` and `Age` (four rows, your choice). Print it. Save it to `test.csv` next to the script with no index column.
  2. Open `17-data2.py`. Read `test.csv` back into a new DataFrame. Print it. Confirm it round-trips.
- **Expected**: A `test.csv` file appears next to your scripts. The two prints look the same.
- **Tell me when done**: reply with `step 13 done`.

### Step 14 — Reading and writing Excel with pandas (Examples 2.18, 2.19)

- **Teach**: Same DataFrame, different file format. Excel needs a third-party engine; we already installed `xlsxwriter` in step 3. The pattern is `pd.ExcelWriter(path, engine='xlsxwriter')` for writing and `pd.read_excel(path, sheet_name=...)` for reading.
- **Do**:
  1. Open `18-excel.py`. Reuse the DataFrame from step 13. Save it to `test.xlsx` with `sheet_name='Sheet1'`.
  2. Open `19-excel2.py`. Read `test.xlsx` back and print it.
- **Expected**: `test.xlsx` opens in Numbers/Excel and shows the four rows. The Python read prints the same data.
- **Tell me when done**: reply with `step 14 done`.

### Step 15 — Datasets and frameworks tour (sections 2.5 and 2.6)

- **Teach**: This section is read-only. The book lists ~12 public datasets (UCI, CIFAR-10, ImageNet, COCO, Kaggle, Google Open Images, LFW, Quandl, US Data.gov, EU Open Data Portal, UK Data Service, World Bank Open Data) and ~9 Python AI frameworks (Scikit-Learn, TensorFlow, Keras, PyTorch, Caffe2, PaddlePaddle, H2O, plus DeepMind's open repos). You don't install any of them yet. The point is to know the map.
- **Do**: Read sections 2.5 and 2.6. In `notes.md`, under **Insights**, write a short shortlist: pick **two datasets** and **two frameworks** you are most curious about, one sentence each on why. This becomes a hint for which later chapters excite you most.
- **Expected**: Four bullets in `notes.md`.
- **Tell me when done**: reply with `step 15 done`.

### Step 16 — Chapter review and recap

- **Teach**: Section 2.8 has chapter review questions. Answering them in your own words consolidates the chapter. We also fill the **Recap** section at the bottom of this file with three takeaways.
- **Do**:
  1. Open `notes.md`. Under a new heading **Chapter 2 review answers**, write a short answer (one to three sentences each) to every review question in section 2.8.
  2. Fill the **Recap** section below with three bullets — your three biggest takeaways from this chapter.
  3. Update `docs/plan.md` row for Chapter 02 from `in-progress` to `done`.
- **Expected**: `notes.md` has answers, this file has a recap, the roadmap shows `done`.
- **Tell me when done**: reply with `step 16 done` — that closes the chapter.

## Exercises

The book embeds six exercises in Chapter 2 (Exercises 2.1 through 2.6). They are folded into the steps above so you do them in context rather than as a batch at the end:

- Exercise 2.1 → Step 9
- Exercise 2.2 → Step 9
- Exercise 2.3 → Step 10
- Exercise 2.4 → Step 10
- Exercise 2.5 → Step 11
- Exercise 2.6 → Step 12

Each exercise file lives in `exercises/` (sibling of this README) with the naming pattern `ex-2-N-<short-name>.py`.

## Recap

Filled in at the end of the chapter. Three bullets, your three biggest takeaways:

- (key idea 1)
- (key idea 2)
- (key idea 3)

When the recap is written, all examples and exercises are typed, and Chapter 2 review answers are in `notes.md`, change the row in [`../../../docs/plan.md`](../../../docs/plan.md) for Chapter 02 from `in-progress` to `done`.

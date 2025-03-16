from flask import Flask, request, render_template_string

app = Flask(__name__)

# QuickSort function
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuickSort with Flask</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="card shadow-lg p-4">
            <h2 class="text-center text-primary">QuickSort with Flask</h2>
            <p class="text-center">Enter numbers separated by commas to sort them using QuickSort.</p>
            
            <form method="post" class="mt-3">
                <div class="input-group mb-3">
                    <input type="text" class="form-control" name="numbers" placeholder="e.g., 3,1,4,1,5,9" required>
                    <button type="submit" class="btn btn-primary">Sort</button>
                </div>
            </form>

            {% if sorted_numbers is not none %}
                <div class="alert {% if sorted_numbers == 'Invalid input! Please enter numbers separated by commas.' %}alert-danger{% else %}alert-success{% endif %}" role="alert">
                    <h4 class="alert-heading">Result:</h4>
                    <p>{{ sorted_numbers }}</p>
                </div>
            {% endif %}
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    sorted_numbers = None
    if request.method == "POST":
        numbers_str = request.form["numbers"]
        try:
            numbers = list(map(int, numbers_str.split(",")))
            sorted_numbers = quicksort(numbers)
        except ValueError:
            sorted_numbers = "Invalid input! Please enter numbers separated by commas."
    return render_template_string(HTML_TEMPLATE, sorted_numbers=sorted_numbers)

if __name__ == "__main__":
    app.run(debug=True)

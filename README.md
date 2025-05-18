<h1>🌱 Soil Assessment Tool – Tkinter GUI</h1>
This is a user-friendly desktop app developed in Python using Tkinter that allows you to evaluate soil fertility based on pH and moisture levels. It includes support for acidic and normal (neutral to alkaline) plants, provides suggestions for soil correction, and features a Dark Mode toggle for better visibility.

<h2>🧪 Features</h2>
Analyze soil pH and moisture to generate a fertility score out of 100.

Get personalized recommendations for improving soil quality.

Choose between acidic and normal plant types.

Built-in warnings for extreme dryness or excess moisture.

Sleek and responsive UI with light/dark mode support.



<h2>🛠️ Requirements</h2>
Python 3.x

Tkinter (comes pre-installed with Python)

Optional: py package (though it seems unused — safe to remove unless needed)

Install missing dependencies (if any):

bash
Copy
Edit
pip install py
<h2>🚀 How to Run</h2>
Save the file as soil_assessment_tool.py.

Open terminal or command prompt in the same directory.

Run:

bash
Copy
Edit
python soil_assessment_tool.py
<h2>✍️ Usage Instructions</h2>
Enter pH of your soil (between 0.0 to 14.0).

Enter moisture percentage (0 to 100).

Select plant type: Acidic or Normal.

Click 🌿 Calculate Soil Assessment to view:

Fertility Score (out of 100)

Detailed recommendations

Use the 🌓 Toggle Dark Mode button to switch themes.

<h2>🎯 Fertility Score Logic</h2>
Score is based on ideal ranges of pH and moisture for your selected plant type.

Ideal ranges:

Acidic plants: pH 4.5–5.5, Moisture 20–60%

Normal plants: pH 6.0–7.0, Moisture 20–60%

Out-of-range inputs are scored lower and may generate suggestions to correct soil chemistry.


<h2>📄 License</h2>
This tool is open-source and free for personal, educational, and community agricultural use.

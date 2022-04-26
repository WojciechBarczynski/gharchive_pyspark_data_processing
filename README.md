# gharchive_pyspark_data_processing
## overview
This is the program for processing archive GitHub events from gharchive from a selected month to
visualize basic stats, such as the number of users that saved the repository with a star or the number of pull
request, for selected public GitHub repository.
## hardware  requirements
### minimal
4 GB of RAM memory <br />
1 GB of disc space <br />
internet connection more stable than average CS student<br />

### recommended
at least 6 GB of RAM memory <br />
at least 2 GB of free SSD hard drive disc space <br />
stable internet connection <br />
processor with more computing power than microwave

## software requirements
Windows 10 (recommended) or Linux operating system (It might work on macOS, but I'm too poor to check that.) <br />
Installed Python 3.8+ (tested on 3.10), Java 11 (Spark doesn't support newer versions), Apache Spark and Pyspark, Hadoop winutils.exe,
wget 1.21.3 and all python libraries specified in requirements.txt.  <br />
To run the program properly, please make sure to set up environmental variables for Java, Spark, Hadoop and wget.  <br />
To run all programs correctly, please download: the examples directory and main.py, make_report.py, spark_data_processing.py, report_demo.py and utills.py files.  <br />
Downloading the requirements.txt file will help you with downloading all necessary python libraries in required versions 
(in most IDEs you can automatically download all specified libraries).  <br />
Here is a link to a great Apache Spark and Pyspark installation tutorial: https://youtu.be/AB2nUrKYRhw   <br />

Example of environmental variables setup: <br />
<img src="/assets/environmental_variables.PNG" alt="Environmental variables setup" title="Environmental variables setup">
Example of path variable setup: <br />
<img src="/assets/path_environmental_variables.PNG" alt="Path in environmental variables setup" title="Path in environmental variables setup">
<br />

## program execution:
If you want to process data, generate, save it as CSV file and display an interactive report, run main.py <br />
If you want to display one of the pre-computed interactive reports, run report_demo.py <br />
Note that to display bar charts you have to click on the link displayed on the console after "Dash is running on message" (default is http://127.0.0.1:8050/).

## report display
Here is a quick look at final report: <br />
Console print: <br />
<img src="/assets/docker_report_console.PNG" alt="docker/docker repository report console" title="docker/docker repository report console"> <br />
Dash interactive web page: <br /> 
<img src="/assets/docker_report_charts.PNG" alt="docker/docker repository report dash" title="docker/docker repository report dash"> <br />
Plotly new stars bar chart: <br />
<img src="/assets/docker_plotly_stars_bar_chart.png" alt="docker/docker repository plotly new stars bar chart" 
     title="docker/docker repository plotly new stars bar chart"> <br />
Plotly pull requests bar chart: <br />
<img src="/assets/docker_plotly_pull_requests_bar_chart.png" alt="docker/docker repository plotly pull requests bar chart" 
     title="docker/docker repository plotly pull requests bar chart"> <br />
     
## further development propositions

### "business" changes
Changing existing code to display not only new stars or pull requests, but also to save other GH events, such as PR reviews, would allow diving deeper into 
repository activity analysis. Such change isn't a particularly challenging task, because the current filtering method firstly selects and saves all repository events in 
PySpark DataFrame, so filtering it for other events would be quite fast in comparison with filtering all GitHub events from all public repositories in a selected month,
and it can be done with just a few lines of code.

### refactor existing code
This project doesn't have the cleanest and most beautiful code and I'm aware of that. Some things need changes, such as exception handling in make_report.py or
user input validation and date string formating (I should have created specific classes for handling multiple date formats) in utills.py, and those parts of code
should be refactored before deployment.

### computing changes
Because computations for separate days are independent, parallelizing computations seems to be the obvious next step in performance improvements. Unfortunately,
multithreading in python is hardly possible, because of the CPython interpreter, which doesn't support multi-core execution. There are some workarounds for that,
but not to put a too fine edge on it, if performance is our priority, we should use Scala or Java in the first place for that project.

> *This tutorial will show you how to use the ECOSTRESS Sharpening API
> code on MacOS.*

# Table of Contents

[Prerequisites](#prerequisites)

[What is Sharpening and what is an API?](#what-is-sharpening-and-what-is-an-api)

[What is Copernicus Data Space?](#what-is-copernicus-data-space)

[Creating a Copernicus Login](#creating-a-copernicus-login)

[What is pyDMS?](#what-is-pydms)

[Downloading Code and pyDMS from GitHub](#downloading-code-and-pydms-from-github)

[What is an OAuth client?](#what-is-an-oauth-client)

[Creating a New OAuth Client](#creating-a-new-oauth-client)

[How to Install the Required Packages for your Environment](#how-to-install-the-required-packages-for-your-environment)

[How to Install pyDMS](#how-to-install-pydms)

[Setting up and Running the Code](#_Toc182902956)

# Prerequisites

Before you start this tutorial, make sure you have an Earthdata Login,
Visual Studio Code downloaded and set up, and a Python Environment to
work with. If you need help setting any of these up, please visit
<https://ecostress.jpl.nasa.gov/tutorials> where you can follow along
with the provided tutorials before proceeding with this one. This
tutorial will walk you through an example of sharpening images of Dodger
Stadium in summer of 2024, but you can follow along with whatever area
and time of interest you want.

# What is Sharpening and what is an API?

In remote sensing, image sharpening refers to enhancing the spatial
resolution of satellite images in order to make them look more detailed.
We use high resolution images to train a machine-learning model which is
then used to sharpen low resolution images. In this code, 70-meter
resolution ECOSTRESS data will be sharpened with 20-meter Sentinel-2
data. This tool also uses APIs (Application Programming Interfaces) to
download both ECOSTRESS and Sentinel-2 data in your region and time of
interest. If you have already downloaded ECOSTRESS data that you would
like to sharpen, you can follow the Sharpening Code tutorial that only
uses and API to download Sentinel-2 data.

# What is Copernicus Data Space?

Copernicus Data Space is a European Space Agency platform that provides
open data from the Copernicus Earth observation satellites, including
Sentinel-2 data. We need a Copernicus Data Space login in order to
create and use the Sentinel Hub API. An API, or Application Programming
Interface, is a tool that allows your code to request and retrieve data
from a server or database automatically.

## Creating a Copernicus Login

1.  Start by going to <https://dataspace.copernicus.eu/> or by searching
    the web for **Copernicus Data Space** and clicking on the first
    link. On the website, click the **green profile icon**.

<img src="Sharpening_API_Code-Mac_images/media/image1.png"
style="width:5.42683in;height:1.71759in"
alt="Graphical user interface, application, website Description automatically generated" />

2.  This will take you to the login page. If you already have an
    account, you can log in and move on to the next section of the
    tutorial. If you do not have an account, click the green register
    button.

<img src="Sharpening_API_Code-Mac_images/media/image2.png"
style="width:5.36111in;height:2.12841in"
alt="Graphical user interface, website Description automatically generated" />

3.  Fill out all of the required fields with your personal information,
    including marking off the check boxes at the bottom of the screen.
    When you are done, click the green register button.

<img src="Sharpening_API_Code-Mac_images/media/image3.png"
style="width:3.66204in;height:2.18431in"
alt="Graphical user interface, application Description automatically generated" />

<img src="Sharpening_API_Code-Mac_images/media/image4.png"
style="width:0.69907in;height:0.38648in"
alt="Graphical user interface, application Description automatically generated" />

4.  The window will now display **Thank you for signing up** and prompt
    you to verify your email. Open your email and look for the
    verification email.

<img src="Sharpening_API_Code-Mac_images/media/image5.png"
style="width:4.79167in;height:1.26389in" />

5.  Click the blue **Verify email address** button which will direct you
    back to the Copernicus Data Space website.

<img src="Sharpening_API_Code-Mac_images/media/image6.png"
style="width:5.15278in;height:1.81944in"
alt="Graphical user interface, text, application Description automatically generated" />

6.  In the new window, click where it says **Click here to proceed**. It
    will then let you know that your email address has been verified.

> <img src="Sharpening_API_Code-Mac_images/media/image7.png"
> style="width:3.5758in;height:1.36111in"
> alt="Graphical user interface, application, Word Description automatically generated" /><img src="Sharpening_API_Code-Mac_images/media/image8.png"
> style="width:3.5724in;height:1.06944in"
> alt="Graphical user interface Description automatically generated" />

# What is pyDMS?

pyDMS is a Python library that implements the Data Mining Sharpened
(DMS) algorithm, that is used to sharpen low resolution satellite
imagery using high resolution data. We want to use this in our code, so
we need to download and install it. We can download it from GitHub,
which is an online platform used to store and share code.

## Downloading Code and pyDMS from GitHub

1.  To access the pyDMS package and the code used in this tutorial, go
    to
    <https://github.com/ECOSTRESS-Tutorials/ECOSTRESS-Sharpening-Tutorial>.

<img src="Sharpening_API_Code-Mac_images/media/image9.png"
style="width:5.50026in;height:2.20833in" />

2.  At the top right, click the green button that says **\<\> Code**. In
    the dropdown select **Download ZIP**. A zip file containing
    everything in the GitHub repository will begin downloading.

<img src="Sharpening_API_Code-Mac_images/media/image10.png"
style="width:2.375in;height:1.86419in"
alt="Graphical user interface, text, application Description automatically generated" />

3.  Once the zip file has been downloaded, **double click** on it to
    un-zip it. This new folder will now function as your **project
    folder**. You can move it wherever you would like, but I am going to
    move mine to my documents.

<img src="Sharpening_API_Code-Mac_images/media/image11.png"
style="width:3.60657in;height:2.14352in"
alt="Graphical user interface, application, Word Description automatically generated" />

# What is an OAuth client?

An OAuth client requests access to data on behalf of the user without
needing their password. Instead, OAuth creates a secure token, or
temporary key, that can be used to access the data for as long as you
allow it. This ensures that your account details stay safe when
downloading data.

## Creating a New OAuth Client

1.  Open Visual Studio Code and get connected to your project folder by
    selecting **File \> Open Folder.** In the pop-up finder window,
    select your project folder and click **Open**.

<img src="Sharpening_API_Code-Mac_images/media/image12.png"
style="width:2.34542in;height:1.90278in"
alt="Graphical user interface, text, application Description automatically generated" />

2.  In the **EXPLORER** tab on the left, hover over the project folder
    and click the **new file icon**.

<img src="Sharpening_API_Code-Mac_images/media/image13.png"
style="width:2.98428in;height:1.625in"
alt="Graphical user interface, text Description automatically generated" />

3.  Name this new file **.env** and press enter.

<img src="Sharpening_API_Code-Mac_images/media/image14.png"
style="width:2.89235in;height:1.70023in"
alt="Graphical user interface, text Description automatically generated" />

4.  Next, in a browser window, go to <https://dataspace.copernicus.eu/>
    or by search for **Copernicus Data Space** and log in. Then, click
    the **green profile icon**.

<img src="Sharpening_API_Code-Mac_images/media/image15.png"
style="width:1.17963in;height:0.66204in"
alt="Graphical user interface, application Description automatically generated" />

5.  In the new window, find the box that says **Dashboards** and click
    the link that says **Sentinel Hub**.

<img src="Sharpening_API_Code-Mac_images/media/image16.png"
style="width:2.01107in;height:1.68982in"
alt="Graphical user interface, text, application Description automatically generated" />

6.  In the Dashboard window, click **User Settings** in the bottom
    right.

<img src="Sharpening_API_Code-Mac_images/media/image17.png"
style="width:2.81019in;height:2.5694in"
alt="Graphical user interface, application Description automatically generated" />

7.  Look for the box titled **OAuth clients** and click the green
    **+Create** button.

<img src="Sharpening_API_Code-Mac_images/media/image18.png"
style="width:3.41204in;height:1.73518in"
alt="Graphical user interface, application Description automatically generated" />

8.  In the pop-up, type in a **Client name**. This name is just a way to
    identify the client for your organization and clarity. For example,
    I am going to name mine **ECOSTRESS_Sharpening**. Once you have
    entered a name, press the green **+Create** button.

<img src="Sharpening_API_Code-Mac_images/media/image19.png"
style="width:5.65175in;height:2.64352in"
alt="Graphical user interface, text, application, email, Teams Description automatically generated" />

9.  A pop-up will appear with your Client ID and Secret. <u>Do not close
    this window because you will not be able to view it again once it is
    gone!</u> Navigate back to Visual Studio Code and open the **.env**
    file that you created. In the **.env** file, type:

    1.  OAUTH_CLIENT_ID=your-client-id

    2.  OAUTH_CLIENT_SECRET=your-client-secret

<img src="Sharpening_API_Code-Mac_images/media/image20.png"
style="width:6.19444in;height:2.83846in"
alt="Graphical user interface, text Description automatically generated" />

10. Replace **your-client-id** with the Client ID that was given in the
    Copernicus Data Space OAuth creation by copying and pasting. Do the
    same with **your-client-secret**. Save your .env file. You can now
    close the OAuth pop-up window.

<img src="Sharpening_API_Code-Mac_images/media/image21.png"
style="width:3.53241in;height:1.76998in"
alt="Graphical user interface, application Description automatically generated" />

<img src="Sharpening_API_Code-Mac_images/media/image22.png"
style="width:4.00417in;height:0.71399in"
alt="Graphical user interface Description automatically generated" />

## How to Install the Required Packages for your Environment

1.  If you followed the creating an environment tutorial, you will need
    to install a few more packages to the ECOSTRESS environment you
    created. If you are working with a different environment, or using
    the ECOSTRESS environment from a previous tutorial, you can look at
    the different packages installed within your environment to see what
    you have and what you need.

    1.  To do this, open the **terminal** and type **mamba activate**
        followed by the name of your environment. Press enter to run.
        You will know your environment has been activated when its name
        shows up in parentheses.

<img src="Sharpening_API_Code-Mac_images/media/image23.png"
style="width:4.13543in;height:2.69907in"
alt="Graphical user interface, text, application Description automatically generated" />

2.  Then type **conda list** and press **enter** to run. This will list
    all the packages in your environment.

<img src="Sharpening_API_Code-Mac_images/media/image24.png"
style="width:3.51755in;height:2.29167in"
alt="Graphical user interface, text, application, email Description automatically generated" />

3.  Compare this to the list of packages on the **requirements.txt**
    document that you downloaded from the GitHub as part of the main
    project folder. Take note of which ones you still need to install.

<img src="Sharpening_API_Code-Mac_images/media/image25.png"
style="width:5.78241in;height:1.72422in"
alt="Graphical user interface, application Description automatically generated" />

2.  To install the remaining packages, first make sure that your
    environment is activated (its name should be listed at the start of
    the terminal command line in parentheses). If it is not activated,
    type **mamba activate** followed by the name of your environment and
    run it.

<img src="Sharpening_API_Code-Mac_images/media/image23.png"
style="width:3.48284in;height:2.27315in"
alt="Graphical user interface, text, application Description automatically generated" />

3.  Then, type **mamba install -c conda-forge** followed by the name of
    all the packages you need to install. If you used the Creating an
    Environment ECOSTRESS tutorial, you can copy and paste this into the
    terminal and run it to get all the remaining packages installed:

**mamba install -c conda-forge gdal libgdal shapely geopandas
sentinelhub numba python-dotenv**

<img src="Sharpening_API_Code-Mac_images/media/image26.png"
style="width:4.76389in;height:3.11434in"
alt="Text Description automatically generated with low confidence" />

1.  However, it is best to list the packages in your own environment and
    make sure you are missing the same ones as me. If you are missing
    different ones, you can modify the command accordingly.

<!-- -->

4.  It may ask you to **Confirm changes y/n** for which you can type
    **y** and press enter.

<img src="Sharpening_API_Code-Mac_images/media/image27.png"
style="width:4.6707in;height:3.05093in"
alt="Text Description automatically generated with medium confidence" />

5.  It should look something like this when it is done:

<img src="Sharpening_API_Code-Mac_images/media/image28.png"
style="width:3.38208in;height:2.19907in"
alt="Text, table Description automatically generated with medium confidence" />

## How to Install pyDMS

1.  Open the terminal and activate your environment by typing **mamba
    activate** followed by the name of your environment.

<img src="Sharpening_API_Code-Mac_images/media/image29.png"
style="width:3.43466in;height:2.24537in"
alt="Graphical user interface, text, application Description automatically generated" />

2.  Then, change the directory to the pyDMS_main folder by typing the
    command **cd** followed by a space and the path to the folder.

<img src="Sharpening_API_Code-Mac_images/media/image30.png"
style="width:3.4573in;height:2.25463in"
alt="Graphical user interface, text, application Description automatically generated" />

1.  To copy the path to the folder, go to **View \> Show Path Bar**.
    Then in your finder, navigate to the folder. Find where the folder
    is listed in the path bar on the bottom of the window. Right click
    it and select **Copy “pyDMS_main” as Pathname**.

<img src="Sharpening_API_Code-Mac_images/media/image31.png"
style="width:1.47454in;height:2.85691in"
alt="Graphical user interface, application Description automatically generated" />
<img src="Sharpening_API_Code-Mac_images/media/image32.png"
style="width:4.71759in;height:2.84568in"
alt="Graphical user interface, application Description automatically generated" />

3.  Then, in the terminal type **python setup.py install** and run it.
    Now you have an environment set up to run the downscaling code with.

<img src="Sharpening_API_Code-Mac_images/media/image33.png"
style="width:4.97685in;height:3.24559in"
alt="Graphical user interface, text, application, email Description automatically generated" />

<span id="_Toc182902956" class="anchor"></span>

## Setting up and Running the Code

1.  In **Visual Studio Code**, open the
    **Sharpening_ECOSTRESS_S2_API.ipynb** Jupyter Notebook. At the top
    of the file there is a lot of information about how the code works
    that you can read if you are interested. Scroll down to the block of
    code that is used to **import libraries**. Click into the code and
    press **Shift + Enter** to run it.

    1.  At the top of the window, a pop up will appear prompting you to
        **select a kernel** to run your code with. Click on **Python
        Environments …**

<img src="Sharpening_API_Code-Mac_images/media/image34.png"
style="width:3.02315in;height:0.58073in"
alt="Graphical user interface Description automatically generated with medium confidence" />

2.  Select the **ECOSTRESS** environment that you created, or another
    one if you have a different one you want to use.

<img src="Sharpening_API_Code-Mac_images/media/image35.png"
style="width:3.03241in;height:0.92527in"
alt="Graphical user interface, text, application, email Description automatically generated" />

3.  You will know it is done running when a green check mark appears on
    the bottom left of the cell.

<img src="Sharpening_API_Code-Mac_images/media/image36.png"
style="width:4.39581in;height:1.79167in"
alt="Text Description automatically generated" />

2.  Next, scroll down to the section of the code under **OAuth
    Copernicus Data Space.** If you followed this tutorial and set up
    your OAuth in a **.env** file, you should be able to press **Shift +
    Enter** to run this block of code. If you set up your OAuth in
    another way, you may need to adjust the code accordingly.

<img src="Sharpening_API_Code-Mac_images/media/image37.png"
style="width:4.81944in;height:1.16573in"
alt="Text Description automatically generated" />

3.  Next, find the block of code under **Type your NASA Earthdata login
    and password** and press **Shift + Enter** to run it.

<img src="Sharpening_API_Code-Mac_images/media/image38.png"
style="width:6.20833in;height:1.0984in"
alt="Text Description automatically generated" />

1.  At the top of the Visual Studio Code window, an input box will
    appear prompting you to **Enter NASA Earthdata Login Username:**.
    Type in your username and press enter.

<img src="Sharpening_API_Code-Mac_images/media/image39.png"
style="width:4.76389in;height:0.58785in" />

2.  Then, it will prompt you to **Enter NASA Earthdata Login
    Password:**. Type this in and press enter.

<img src="Sharpening_API_Code-Mac_images/media/image40.png"
style="width:4.76389in;height:0.55833in" />

4.  In the next block of code, find the variable called
    **s2_output_folder**. Set this variable to the path of an output
    folder for the Sentinel 2 imagery. I am going to do this by creating
    a **new folder** in my **project folder** and copying its path into
    the code. Make sure the path still has **r** in front and is wrapped
    in quotes.

<img src="Sharpening_API_Code-Mac_images/media/image41.png"
style="width:4.73611in;height:2.50417in"
alt="Graphical user interface, application, Word Description automatically generated" />  
Example:

<img src="Sharpening_API_Code-Mac_images/media/image42.png"
style="width:6.5in;height:0.53264in" />

5.  Then find the variable titled **eco_output_folder** and set it to
    the path of an output folder for the ECOSTRESS imagery. Again, I am
    going to create a **new folder** for this in the main **project
    folder** and copy its path into the code. Make sure the path still
    has **r** in front and is wrapped in quotes.

<img src="Sharpening_API_Code-Mac_images/media/image43.png"
style="width:4.80121in;height:2.54167in"
alt="Graphical user interface, application, Word Description automatically generated" />

Example:<img src="Sharpening_API_Code-Mac_images/media/image44.png"
style="width:6.5in;height:0.34916in" />

6.  Finally, find the variable titled **dst_dir**. Set it to a path of a
    folder to store the final sharpened images. Once again, I am going
    to create a **new folder** for this in the main **project folder**
    and copy its path into the code. Make sure the path still has **r**
    in front and is wrapped in quotes.

<img src="Sharpening_API_Code-Mac_images/media/image45.png"
style="width:4.70671in;height:2.48611in"
alt="Graphical user interface, application Description automatically generated" />

Example:

<img src="Sharpening_API_Code-Mac_images/media/image46.png"
style="width:6.5in;height:0.45972in" />

7.  Once all your variables are set, press **Shift + Enter** to run the
    code. At the top of the window, another input box will appear asking
    you to enter a **task name**. This is just the name of the request
    that will be named in AppEEARS. Enter a name and then press enter.

Example:

<img src="Sharpening_API_Code-Mac_images/media/image47.png"
style="width:4.69907in;height:0.56228in" />

8.  Scroll down to the next block of code under **Set the parameters for
    the products to be downloaded** and find the variable titled
    **aoi_coords_wgs_84**. We need to set this variable equal to the
    coordinates of a bounding box for our study area. To get these
    coordinates, click on the link in the code or search the web for
    **bboxfinder.com**.

<img src="Sharpening_API_Code-Mac_images/media/image48.png"
style="width:3.65087in;height:2.33796in"
alt="Map Description automatically generated" />

9.  On the website, **zoom into** your area of interest on the map. Then
    click the **draw a shape icon**. Click on the map to create a box
    around your area of interest and click on the first point you made
    to close the box.

<img src="Sharpening_API_Code-Mac_images/media/image49.png"
style="width:3.78353in;height:2.4213in"
alt="Map Description automatically generated" />

10. Then, at the bottom of the screen, **copy** the coordinates listed
    after **Box**. Go back to Visual Studio Code and **Paste** these
    coordinates into the variable.

Example:

<img src="Sharpening_API_Code-Mac_images/media/image50.png"
style="width:4.21759in;height:0.98771in"
alt="Timeline Description automatically generated with medium confidence" />

<img src="Sharpening_API_Code-Mac_images/media/image51.png"
style="width:6.03241in;height:0.68638in" />

11. Next, you can set the resolution of the Sentinel 2 data by adjusting
    the variable called **s2_res**. For now, I will leave it at 20.

<img src="Sharpening_API_Code-Mac_images/media/image52.png"
style="width:0.83796in;height:0.36661in"
alt="Graphical user interface, text, application Description automatically generated" />

12. You can also specify the **collection** of ECOSTRESS images that you
    want to use. At the time of this tutorial’s creation, collection 2
    is still being processed, so I am going to set this to **1**. Please
    refer to <https://ecostress.jpl.nasa.gov/data> for information about
    collection processing.

<img src="Sharpening_API_Code-Mac_images/media/image53.png"
style="width:1.02292in;height:0.38477in"
alt="Graphical user interface Description automatically generated with medium confidence" />

13. Finally, we need to change the **interval** variable to represent
    the start and end date for which we are interested in getting data.
    Make sure to enter these dates in the **“YYYY-MM-DD”** format.

Example:

<img src="Sharpening_API_Code-Mac_images/media/image54.png"
style="width:3.21759in;height:0.45475in"
alt="A screenshot of a computer Description automatically generated with medium confidence" />

14. Once all of the variables are set, run this block of code by
    pressing **Shift + Enter.**

<img src="Sharpening_API_Code-Mac_images/media/image55.png"
style="width:6.07309in;height:1.63701in"
alt="Text Description automatically generated" />

15. Continue to the next block of code and press **Shift + Enter** to
    run it. The bounding box is limited to **2500 pixels**, so if you
    get an error about this you will need to **reduce** the size of your
    bounding box and re-run that block of code.

<img src="Sharpening_API_Code-Mac_images/media/image56.png"
style="width:5.78241in;height:1.04652in"
alt="Text Description automatically generated" />

16. Run the next **four** blocks of code including:

    1.  **Download the S2 image with the previously defined
        parameters.**

<img src="Sharpening_API_Code-Mac_images/media/image57.png"
style="width:4.64727in;height:1.56944in"
alt="Text Description automatically generated" />

2.  **Authentication and Token Retrieval for NASA AppEEARS API**

<img src="Sharpening_API_Code-Mac_images/media/image58.png"
style="width:4.78797in;height:1.85648in"
alt="Text Description automatically generated" />

3.  **Locate ECOSTRESS products and search for the layers of interest in
    our case: LST and QC**

<img src="Sharpening_API_Code-Mac_images/media/image59.png"
style="width:4.83796in;height:1.78994in"
alt="Text Description automatically generated" />

4.  **Formulate the AppEEARs request**

<img src="Sharpening_API_Code-Mac_images/media/image60.png"
style="width:4.50936in;height:1.9213in"
alt="A screenshot of a computer Description automatically generated with medium confidence" />

17. Then find the next block of code under **Ping the API** and press
    **Shift + Enter** to run it. This code will check in with the
    AppEEARS request every 30 seconds and give you a report such as
    **queued** or **processing**. This code may take a while to run
    since it takes time for the requests to be fulfilled. You can leave
    this part of the code to run and come back later.

<img src="Sharpening_API_Code-Mac_images/media/image61.png"
style="width:4.92986in;height:1.47685in"
alt="Text Description automatically generated" />

1.  You will know you are ready to proceed when the code output says
    **done**.

<img src="Sharpening_API_Code-Mac_images/media/image62.png"
style="width:0.66263in;height:0.70833in"
alt="Graphical user interface, text, application Description automatically generated" />

18. Run the block of code under **Download the ordered files** to
    download the ECOTRESS files to your computer.

<img src="Sharpening_API_Code-Mac_images/media/image63.png"
style="width:5.67145in;height:1.82686in" />

19. From here, your code should be ready to run the next **four**
    modules including:

    1.  **Sort the downloaded files in appropriate sub-directories**

<img src="Sharpening_API_Code-Mac_images/media/image64.png"
style="width:5.5403in;height:1.65972in"
alt="Text Description automatically generated" />

2.  **Preprocessing the QC files**

<img src="Sharpening_API_Code-Mac_images/media/image65.png"
style="width:5.66458in;height:1.86217in"
alt="Text Description automatically generated" />

**Tip**: If you get a Rasterio error similar to this, your files may
have been corrupted. In order to fix this, go to your ECO_Outputs folder
and delete everything. Then go back and run the **Download the ordered
files**, **Sort the downloaded files in appropriate subdirectories,**
and **Preprocessing the QC files** cells. The error should be resolved.

<img src="Sharpening_API_Code-Mac_images/media/image660.png"
style="width:6.08128in;height:1.92535in"
alt="Text Description automatically generated" />

**  
**

3.  **Scaling the ECOSTRESS LST to normal Kelvin Scale**

<img src="Sharpening_API_Code-Mac_images/media/image67.png"
style="width:5.87705in;height:2.39101in"
alt="Text Description automatically generated" />

4.  **Unsampling using pyDMS**

    1.  Use the first block of code under this header if you want to
        process the entire extent of the image.

<img src="Sharpening_API_Code-Mac_images/media/image68.png"
style="width:5.67145in;height:1.43059in"
alt="Text Description automatically generated" />

2.  Use the second block of code under this header if you only want to
    sample part of the image.

<img src="Sharpening_API_Code-Mac_images/media/image69.png"
style="width:6.5in;height:1.13889in"
alt="Text, website Description automatically generated" />

20. Once you have run these modules, you now have sharpened ECOSTRESS
    imagery! In order to see an **image plotted** of the sharpened
    scenes, you can run the block of code under the **Display** section.

<img src="Sharpening_API_Code-Mac_images/media/image70.png"
style="width:5.53638in;height:2.46653in"
alt="Text Description automatically generated" />

1.  Example of **Plot one random sharpened image:**

<img src="Sharpening_API_Code-Mac_images/media/image71.png"
style="width:3.16571in;height:4.85246in"
alt="Graphical user interface, application Description automatically generated" />

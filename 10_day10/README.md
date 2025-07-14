# EXL MLOps training program

## Day 10: CI/CD + End-to-End Project
 - Building CI/CD workflows
 - GitHub Actions for ML
 - Deploying a complete ML pipeline
 - Showcase of student/real-world projects

 ## study material
 - Github action for mlops - https://youtu.be/rX-P0gbb1V0?si=hmH2LOQmygTkU1Od
 - how to setup selfhosted runner - https://youtu.be/O3ym0KNU82w?si=5erR1Ya7ntcJMSXc
 - automate github pipeline with github action - https://youtu.be/AkTOLyAtbLU?si=BTLQpqf9hpfFwjBg




### ######################################################################################################################

adding a self-hosted runner requires that you download, configure, and execute the GitHub Actions Runner. If you do not already have an existing volume licensing agreement for your GitHub purchases, by downloading and configuring the GitHub Actions Runner, you agree to the GitHub Customer Agreement.

Runner image

macOS

Linux

Windows

Download
We recommend configuring the runner under "\actions-runner". This will help avoid issues related to service identity folder permissions and long path restrictions on Windows.

# Create a folder under the drive root
$ mkdir actions-runner; cd actions-runner# Download the latest runner package
$ Invoke-WebRequest -Uri https://github.com/actions/runner/releases/download/v2.326.0/actions-runner-win-x64-2.326.0.zip -OutFile actions-runner-win-x64-2.326.0.zip# Optional: Validate the hash
$ if((Get-FileHash -Path actions-runner-win-x64-2.326.0.zip -Algorithm SHA256).Hash.ToUpper() -ne '539d48815f8ecda6903755025d5b578f919a32692b731d85a9a24419fe4dbd9e'.ToUpper()){ throw 'Computed checksum did not match' }# Extract the installer
$ Add-Type -AssemblyName System.IO.Compression.FileSystem ; [System.IO.Compression.ZipFile]::ExtractToDirectory("$PWD/actions-runner-win-x64-2.326.0.zip", "$PWD")
Configure
# Create the runner and start the configuration experience
$ ./config.cmd --url https://github.com/yogii2356/testgithubaction --token A3AILHO6MJQMTRRRNDTKVSTIOOTCE# Run it!
$ ./run.cmd
Using your self-hosted runner
# Use this YAML in your workflow file for each job
runs-on: self-hosted



## you can take reffrence from here 

https://github.com/yogii2356/testgithubaction/settings/actions/runners/new
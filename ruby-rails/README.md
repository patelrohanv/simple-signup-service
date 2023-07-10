# My Rails Application

This is a simple Ruby on Rails application serving a signup page.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of Ruby and Rails. This application was developed with Ruby version 3.2.2 and Rails version 7.0.4.
* You have a Linux/Mac machine. Windows is also fine, but Linux/Mac is recommended.

## Installing Dependencies

To install the app's dependencies, follow these steps:

1. Install the dependencies:

    ```bash
    bundle install
    ```

2. Create the database:

    ```bash
    rails db:create
    ```

3. Run the database migrations:

    ```bash
    rails db:migrate
    ```

## Using My Rails Application

To use My Rails Application, follow these steps:

1. Start the Rails server:

    ```bash
    rails server -e development
    ```

2. Open your web browser and navigate to `http://localhost:3000`.

## Running Tests

This application uses the built-in Rails testing framework, Minitest. Here's how you can run the tests:

1. **Running All Tests**: If you want to run all tests, use the `rails test` command:

    ```bash
    rails test
    ```

    This command will run all test cases in the `test` directory of the application.

2. **Running Specific Tests**: If you want to run a specific test file, specify the file path after the `rails test` command:

    ```bash
    rails test test/models/user_test.rb
    ```

    This command will only run the test cases in the `user_test.rb` file.

3. **Running a Specific Test Case**: If you want to run a specific test case within a test file, specify the file path and the test case name separated by a colon:

    ```bash
    rails test test/models/user_test.rb:27
    ```

    This command will only run the test case on line 27 in the `user_test.rb` file.

Please replace `user_test.rb` and `27` with your actual test file and test case line number.

## Deployment

This application is containerized using Docker. Here's how you can build and run the Docker image:

1. **Build the Docker Image**: Run the `build_image.sh` script to build the Docker image:

    ```bash
    ./build_image.sh
    ```

    This script builds a Docker image named `rails-signup` using the Dockerfile in the current directory.

2. **Run the Docker Image**: After the image is built, you can run it with the following command:

    ```bash
    docker run -p 3000:3000 rails-signup
    ```

    This command runs the `rails-signup` image and forwards port 3000 in the container to port 3000 on the Docker host. The Rails application will be accessible at `http://0.0.0.0:3000`.

Please ensure that you have Docker installed and that the `build_image.sh` script is executable. If the `build_image.sh` script is not executable, you can make it executable with the following command:

```bash
chmod +x build_image.sh
```


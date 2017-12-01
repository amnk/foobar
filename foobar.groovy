def giturl = 'https://github.com/amnk/hello.git'

job('Test project'){
    scm {
        git(giturl)
    }
    triggers {
        scm('@hourly')
    }
    wrappers {
        release {
            postSuccessfulBuildSteps {
                shell('docker build -t amnk/skael-hello:latest .')
                shell('docker push amnk/skael-hello')

            }
        }
    }
    steps {
        shell('pip install -r foobar/test-requirements.txt')
        shell('cd foobar && python hello_tests.py')
    }
}

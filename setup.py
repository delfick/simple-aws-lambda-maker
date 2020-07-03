from setuptools import setup, find_packages
from simple_aws_lambda_maker import VERSION

# fmt: off

setup(
      name = "simple-aws-lambda-maker"
    , version = VERSION
    , packages = find_packages(include="simple_aws_lambda_maker.*"),

    , install_requires =
      [ "delfick_app==0.9.6"
      , "option_merge==1.6"
      , "input_algorithms==0.6.0"

      , "boto3==1.4.7"
      , "datadiff==2.0.0"
      , "ruamel.yaml==0.15.87"
      , "requests==2.20.0"
      ]

    , entry_points =
      { 'console_scripts' :
        [ 'salm = simple_aws_lambda_maker.executor:main'
        ]
      }

    # metadata for upload to PyPI
    , url = "https://github.com/delfick/simple-aws-lambda-maker"
    , author = "Stephen Moore"
    , author_email = "github@delfick.com"
    , description = "Very simple deploy tool for aws lambda"
    , long_description = open("README.rst").read()
    , license = "MIT"
    , keywords = "aws lambda"
    )

# fmt: on

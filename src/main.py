import argparse
import flask
from flask import Flask
from flask import Response as ResponseBase
import connexion
from swagger_ui_bundle import swagger_ui_3_path
import os
from connexion.resolver import RestyResolver
import prance
from pathlib import Path
from typing import Dict, Any


parser = argparse.ArgumentParser()
parser.add_argument('--host', default='0.0.0.0')
parser.add_argument('--port', type=int, default=9000)
args, _ = parser.parse_known_args()


def aggregate_specs(main_file: Path) -> Dict[str, Any]:
    """This function glues all seperate API Spec YML files together.

    This enales we keep a set of small YML files while being able
    to use something like $ref: 'another.yaml#/components/schemas/Foo'
    in the YML files.
    """
    parser = prance.ResolvingParser(str(main_file.absolute()), lazy=True, strict=True)
    parser.parse()
    return parser.specification


# Use OpenAPI Swagger page, and redirct SwaggerUI to root
options = {'swagger_path': swagger_ui_3_path, "swagger_url": ""}

# Note this app is a wrapper around FlaskAPP, use app.app to access
# the actual Flask app
app = connexion.App(__name__, options=options)
app.add_api(
    aggregate_specs(Path(__file__).parent / "swagger/api.yml"),
    validate_responses=True,
    resolver=RestyResolver('src.api'),
)


def handler(environ, start_response) -> flask.Flask:
    """This function is required by the deployment.

    For more information, check here:
    https://www.alibabacloud.com/help/doc-detail/74756.htm?spm=a2c63.l28256.a3.18.a2543c943bYfKr
    """
    # do something here
    return app(environ, start_response)


if __name__ == "__main__":
    app.run(host=args.host, port=os.environ.get("FC_SERVER_PORT", args.port), debug=False)

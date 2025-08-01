import kfp
from kfp import dsl

def data_processing_op():
    return dsl.containerOp(
        name="Data processing",
        image= "dataguru/my-mlops-app:latest",
        comand= ["python", "src/data_processing.py"]
    )


def model_training_op():
    return dsl.containerOp(
        name="model training",
        image= "dataguru/my-mlops-app:latest",
        comand= ["python", "src/model_training.py"]
    )


@dsl.pipeline(
    name= "mlops pipeline",
    description="this is my first kubeerflow pipeline"
)

def mlops_pipeline():
    data_processing = data_processing_op()
    model_training = model_training_op().after(data_processing)


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        mlops_pipeline, "mlops_pipeline.yaml"
    )

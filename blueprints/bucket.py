from stacker.blueprints.base import Blueprint
from stacker.blueprints.variables.types import CFNString
from troposphere import Ref
from troposphere.s3 import Bucket


class SimpleS3(Blueprint):
    """Touch creates a wait condition handle and nothing else.

    For learning / functional testing.
    """

    VARIABLES = {}

    def dynamic_build(self, inject_bucket_name):
        """

        :type inject_bucket_name: bool
        """
        self.template.description = ("Dynamically adds params to the template "
                                     "based on what is added to create_template")

        t = self.template
        if(inject_bucket_name):

            bucket_param_name = "NameOfBucket"
            t.add_resource(Bucket(
                "TheBucket",
                BucketName=Ref(bucket_param_name),
            ))
            self.VARIABLES.update({
                bucket_param_name: {
                    'type': CFNString,
                    'description': 'The name of the bucket',
                },
            })
        else:
            t.add_resource(Bucket(
                "S3Bucket",
                BucketName=self.context.namespace + "mybucket",
            ))

    def defined_variables(self):
        variables =  super(SimpleS3, self).defined_variables()
        print("--variables:")
        print(variables)
        print("--self.VARIABLES:")
        print(self.VARIABLES)

        return variables


    def create_template(self):
        self.dynamic_build(inject_bucket_name=True)
        # exit(1)

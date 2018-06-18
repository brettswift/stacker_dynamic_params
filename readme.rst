dynamic_params
#############################

1) run pip install -e . ; pip install troposphere
2) change the stacker_bucket param in stacker.yml
3) `stacker build  ./conf/dev.env stacker.yaml --region us-west-2 --recreate-failed -i -t`



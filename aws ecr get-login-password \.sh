aws ecr get-login-password \
  --region eu-west-2 \
| docker login \
    --username AWS \
    --password-stdin 955857273204.dkr.ecr.eu-west-2.amazonaws.com


    VPC_ID=$(aws ec2 describe-vpcs \
  --filters Name=isDefault,Values=false \
  --query "Vpcs[0].VpcId" \
  --output text \
  --region eu-west-2)
echo "Using VPC: $VPC_ID"



export PRIVATE_SUBNETS="subnet-aaa111bbb222ccc subnet-ddd333eee444fff"

export VPC_ID=vpc-7506541d
export CIDR_A=172.31.48.0/24   
export CIDR_B=172.31.49.0/24    



export VPC_ID=vpc-7506541d
export PUBLIC_SUBNET_A=subnet-ca3050b0       
export PUBLIC_SUBNET_B=subnet-9c44f3d0       
export PRIVATE_SUBNET_A=subnet-028d36cf8a06c963e 
export PRIVATE_SUBNET_B=subnet-0810d01cb42cc41e1 
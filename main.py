import os, argparse
from detectFacialFeatures import process
import shutil
import os

def main(args):
  if os.path.exists('./results'):
    shutil.rmtree('./results')
    os.makedirs('results')
  else: 
    os.makedirs('results')
  if args.single: 
    process(args.single, args.m_shape, args.verbose)
  else: 
    for image in os.listdir(args.input):
      if image.endswith('jpg'):
        path = os.path.join(args.input, image)
        process(path, args.m_shape, args.verbose)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='MSHAPE and RECEDING HAIRLINE project')
  parser.add_argument('--single', type=str, default=False, type=str)
  # parser.add_argument('--single', type=str, default=r'C:\Users\Public\ferdy\front_face\black\male_black_hair\male_black_hair10.jpg', type=str)
  parser.add_argument('--input', default=r'C:\Users\Public\ferdy\front_face\black\male_black_hair', type=str)
  parser.add_argument('--m_shape', default=True, type=str)
  parser.add_argument('--verbose', default=False, type=str)
  args=parser.parse_args()
  main(args)

from healthcare import *

def main():
    centers=lee_centros("./data/centrosSanitarios.csv")
    print(f"We have {len(centers)} healthcare centers")
    print("First center    \n", centers[0])
    
if __name__ =="__main__":
    main()
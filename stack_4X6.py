from PIL import Image
import sys

def stack(pic):
    image = Image.open(pic)
    size = image.size
    print(size)
    width ,height = size[0] , size[1]
    new_image = Image.new('RGB',(width*3 ,height*2),(250,250,250))
    for i in range(2):
        for j in range(3):
            new_image.paste(image,(j*width,i*height))
    
    new_file_name = pic+"_new_.jpg"
    new_image.save(new_file_name , "JPEG",quality=100, subsampling=0)
    new_image.show()

if __name__ == '__main__':
    stack(sys.argv[1])
        
    
    
    
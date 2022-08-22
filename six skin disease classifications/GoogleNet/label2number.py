#类名 数字化映射
import os
origin_file_name='6disease_new_origin'
def main():
    classes=os.listdir('./'+origin_file_name)
    label2number=open(origin_file_name+'_label2number.csv','w',encoding='gbk')##将标签信息转换为数字写入文件
    info='index,class\n'
    for index , cla in enumerate(classes):
        print(index , cla )
        tempLine=str(index)+','+str(cla)+'\n'
        info+=tempLine
    label2number.write(info)
    label2number.close()
    return classes
def rename_dir(classes):
    print(os.listdir(origin_file_name))
    fix_name=origin_file_name+'/'
    for index, cla in enumerate(classes):
        src,dist=fix_name+str(cla),fix_name+str(index)
        os.rename(src,dist)
    print(os.listdir(origin_file_name))
if __name__ == '__main__':
    classes=main()
    rename_dir(classes)
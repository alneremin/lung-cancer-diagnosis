

from MIA.TCIA.tciaclient import TCIAClient
from MIA.TCIA.tciaclientimpl import TCIAClientImpl

from MIA.VisualizationTools.get_data_from_XML import *
from MIA.VisualizationTools.utils import *
from PIL.Image import fromarray
import os
import json

# разделяем массив имен пациентов на тренировочную и тестировочную 
# и по категориям class_list
# class_list = [A, B, E, G]
def split_names(names, class_list, prefix):
    splited_names = [[] for _ in range(len(class_list))]
    for name in names:
      indx = class_list.index(str(name.replace(prefix, "")[0]))
      splited_names[indx].append(name)
    
    x_train = []
    x_test = []
    for cat in splited_names:
      separator = round(len(cat) / 5 * 4)
      for element in cat[:separator]:
        x_train.append(element)
      
      for element in cat[separator:]:
        x_test.append(element)

    return {"train": x_train,"test":x_test}

# classfile="VisualizationTools\\category.txt"
# annotation_path="Annotation\\"

def download_data(classfile, path_to_download, annotation_path, patient_count, to_jpg=False):

    apiKey = "7ad8c98d-74f9-4ebf-a59c-c3de09550db4"
    baseUrl = "https://services.cancerimagingarchive.net/services/v3"
    tcia_client = TCIAClient(apiKey=apiKey,baseUrl=baseUrl,resource="TCIA")
    client_impl = TCIAClientImpl(tcia_client)

    # скачиваем аннотации с ресурса
    url = "https://wiki.cancerimagingarchive.net/download/attachments/70224216/Lung-PET-CT-Dx-Annotations-XML-Files-rev10152020.zip"
    queryParameters = {"version":1, "modificationDate":1603823290007, "api":"v2"}
    if not os.path.exists(annotation_path):
        client_impl.download_annotation(url, queryParameters, os.path.split(annotation_path)[0])

    # получаем кол-во классов
    class_list = get_category(classfile)
    num_classes = len(class_list)


    # префикс имени пациента
    prefix = "Lung_Dx-"

    # получаем имена пациентов
    patient_names = client_impl.get_patient(client_impl.collection)

    patient_names_json = split_names(patient_names, class_list, prefix)

    patient_count_current = 0
    # для выборок train/test
    for data_type, names in patient_names_json.items():
      # для каждого пациента
      for name in names:
        # если достигнуто ограничение по скачиванию пациентов, прерываем скачивание
        if patient_count_current >= patient_count:
          return

        # формируем путь до папки со снимками пациента
        path_to_dcm = os.path.join(path_to_download, data_type, name.replace(prefix, "")[0], name)
        if os.path.exists(path_to_dcm):
          continue

        patient_count_current += 1

        try:
          # получаем названия xml-файлов и данные об опухоли
          annotations = XML_preprocessor(os.path.join(annotation_path, name.replace(prefix, "")), num_classes=num_classes).data
        except FileNotFoundError:
          print("patient_xml " + name + " not found")
          continue
        # формализованный результат для SOPInstanceUID #number
        # key = list(annotations.keys())[number]
        # y_train[0] = annotations[key][0][-4:]


        # получаем массив SOPInstanceUID
        annotation_uids = [k[:-4] for k in annotations.keys()]
        #print(annotation_uids)

        # получаем StudyUID пациента
        uids = client_impl.get_patient_study(client_impl.collection, name)
        
        # для каждого снимка пациента
        for study_uid in uids:
          # по StudyUID получаем один или несколько КТ-снимков
          series_uids = client_impl.get_series(client_impl.collection,
                                          name, 
                                          study_uid
                                          )
          # если пути до папки со снимками пациента нет, создаем его
          if not os.path.exists(path_to_dcm):
            os.makedirs(path_to_dcm)

          # загружаем данные (только те, что представлены в XML-аннотациях)
          tcia_client.downloadMissing(SOPInstanceUIDs=annotation_uids, 
                                            rootDirectory=path_to_dcm, 
                                            seriesInstanceUids=series_uids)
          dcm_files = os.listdir(path_to_dcm)

          if to_jpg:
            print(path_to_dcm +  "/*.dcm to " + path_to_dcm +  "/*.jpg")
            # преобразуем dcm в jpg
            for dcm in dcm_files:
              if dcm[-4:] != ".dcm":
                continue
              path_to_dcm_file = os.path.join(path_to_dcm, dcm)
              matrix, frame_num, width, height, ch = loadFile(path_to_dcm_file)
              img_bitmap = MatrixToImage(matrix[0], ch)
              img = fromarray(img_bitmap)
              img.save(path_to_dcm_file[:-4] + ".jpg")
              os.remove(path_to_dcm_file)

# example
if __name__ == "__main__":
  classfile = os.path.join("VisualizationTools", "category.txt")
  path_to_download = "downloads"
  download_data(classfile=classfile,
                path_to_download=path_to_download,
                patient_count=40,
                to_jpg=False)
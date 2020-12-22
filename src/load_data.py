

from TCIA.tciaclient import TCIAClient
from TCIA.tciaclientimpl import TCIAClientImpl

from VisualizationTools.get_data_from_XML import *
import os


# разделяем массив имен пациентов по категориям class_list
# class_list = [A, B, E, G]
def splitNames(names, class_list, prefix):
	splited_names = [[] for _ in range(len(class_list))]
	for name in names:
		indx = class_list.index(str(name.replace(prefix, "")[0]))
		splited_names[indx].append(name)
	# для первого запуска берем не все данные, только первые из каждой категории
	test_array = []
	for cat in splited_names:
		test_array.append(cat[0])
		test_array.append(cat[1])
	return test_array

# classfile="VisualizationTools\\category.txt"
# annotation_path="Annotation\\"

def load_data(classfile, annotation_path):

    apiKey = "7ad8c98d-74f9-4ebf-a59c-c3de09550db4"
    baseUrl = "https://services.cancerimagingarchive.net/services/v3"
    tcia_client = TCIAClient(apiKey=apiKey,baseUrl=baseUrl,resource="TCIA")
    client = TCIAClientImpl(tcia_client)

    # скачиваем аннотации с ресурса
    url = "https://wiki.cancerimagingarchive.net/download/attachments/70224216/Lung-PET-CT-Dx-Annotations-XML-Files-rev10152020.zip"
    queryParameters = {"version":1, "modificationDate":1603823290007, "api":"v2"}
    if not os.path.exists(annotation_path):
    	client.download_annotation(url, queryParameters)

    # получаем кол-во классов
    class_list = get_category(classfile)
    num_classes = len(class_list)


    # префикс имени пациента
    prefix = "Lung_Dx-"

    # получаем имена пациентов
    patient_names = client.get_patient(client.collection)
    patient_names = splitNames(patient_names, class_list, prefix)

    # для каждого пациента выполняем скачивание его КТ-снимков
    for name in patient_names:

        # получаем названия xml-файлов и данные об опухоли
        annotations = XML_preprocessor(annotation_path + name.replace(prefix, ""), num_classes=num_classes).data

        # формализованный результат для SOPInstanceUID #number
        # key = list(annotations.keys())[number]
        # y_train[0] = annotations[key][0][-4:]


        # получаем массив SOPInstanceUID
        annotation_uids = [k[:-4] for k in annotations.keys()]
        #print(annotation_uids)

        # получаем StudyUID пациента
        uid = client.get_patient_study(client.collection, name)
         # по StudyUID получаем один или несколько КТ-снимков
        series_uids = client.get_series(client.collection, name, uid)
        path_to_dcm = "downloads\\" + client.collection + '\\' + name.replace(prefix, "")[0] + '\\' + name + '\\'

        # загружаем данные (только те, что представлены в XML-аннотациях)
        tcia_client.downloadMissing(SOPInstanceUIDs=annotation_uids, 
                                           rootDirectory=path_to_dcm, 
                                           seriesInstanceUids=series_uids)

# example
# load_data(classfile="VisualizationTools\\category.txt", annotation_path="downloads\\Annotation\\")
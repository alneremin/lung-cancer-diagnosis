
import sys
import os

#from tciaclient import TCIAClient

import urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error,sys
import json

import zipfile

class TCIAClientImpl:
    def __init__(self, tcia_client, collection="Lung-PET-CT-Dx"):

        self.tcia_client = tcia_client
        self.collection = collection
        """
        tcia_client2 = TCIAClient(apiKey ="7ad8c98d-74f9-4ebf-a59c-c3de09550db4",
                                   baseUrl="https://services.cancerimagingarchive.net/services/v3",
                                   resource="SharedList")
        """

    # для UID пациента получаем SeriesUids
    def get_series(self, collection, patientId, studyInstanceUid):
        try:
            response = self.tcia_client.get_series(collection = collection,
                                              studyInstanceUid = studyInstanceUid, 
                                              patientId = patientId,
                                              seriesInstanceUid = None,
                                              modality = None,
                                              bodyPartExamined = None,
                                              manufacturerModelName = None,
                                              manufacturer = None,
                                              outputFormat = "json")
            print("\nQuery TCIA - getSeries({}, {}, {}, Null, Null, Null, Null, Null, JSON)".format(collection,studyInstanceUid,patientId))
            series_uids_json = json.load(response)
            series_uids = [] 
            for series_uid in series_uids_json:
                series_uids.append(series_uid)
            return series_uids
        except urllib.error.HTTPError as err:
            print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
            return []
    # получаем имена пациентов
    def get_patient(self, collection):
        try:
            response = self.tcia_client.get_patient(collection = collection,
                                               outputFormat = "json")
            print("\nQuery TCIA - getPatient({}, JSON)".format(collection))
            json_response = json.load(response)
            names = []
            for name in json_response:
                names.append(name["PatientID"])
            names.sort()
            return names
        except urllib.error.HTTPError as err:
            print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
            return []

    # для каждого пациента получаем его UID
    def get_patient_study(self, collection, name):
            try:
                response = self.tcia_client.get_patient_study(collection = collection, patientId = name, outputFormat = "json")
                print("\nQuery TCIA - getPatientStudy({},{}, JSON)".format(collection, name))
                uid = json.load(response)[0]["StudyInstanceUID"]
                return uid
            except urllib.error.HTTPError as err:
                print("Error executing program:\nError Code: ", str(err.code), "\nMessage:", err.read())
                return ""

    # скачиваем и распаковываем аннотации            
    def download_annotation(self, url, queryParameters, path_to_download):
        if not os.path.exists(path_to_download):
            os.mkdir(path_to_download)
        path_to_zip_file = os.path.join(path_to_download,"annotation.zip")
        resp = self.tcia_client.execute_download(url=url, fileName=path_to_zip_file, queryParameters=queryParameters)
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall("path_to_download")


"""
url = "https://wiki.cancerimagingarchive.net/download/attachments/70224216/Lung-PET-CT-Dx-Annotations-XML-Files-rev10152020.zip"
queryParameters = {"version":1, "modificationDate":1603823290007, "api":"v2"}
download_annotation(url, queryParameters)

patient_names = get_patient(collection)[-2:]

for name in patient_names:
    uid = get_patient_study(collection, name)
    series_uids = get_series(collection, name, uid)
    path_to_dcm = collection + '\\' + name + '\\'
    tcia_client.downloadMissing(rootDirectory=path_to_dcm, seriesInstanceUids=series_uids)
"""
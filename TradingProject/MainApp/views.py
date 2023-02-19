from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import serializers,viewsets
from rest_framework.decorators import action
from .models import csvmodel

import csv

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from io import open as io_open

# we cant read the content with csv reader so we have to store it and then read it
fs=FileSystemStorage(location='temp/')


# serializing the data

class csvfileserializer(serializers.ModelSerializer):
    class Meta:
        model= csvmodel
        fields="__all__"


# creating viewset
# class based view
class csvViewSet(viewsets.ModelViewSet):
    queryset=csvmodel.objects.all()
    serializer_class=csvfileserializer

    # setting detail=False so action operates on entire queryset
    @action(detail=False , methods=['POST'])
    def upload_data(self,request):
        # accepting file which has been given as request
        file=request.FILES["file"]

        # reading accepted file
        content=file.read()

        # reading content of the file and storing in file_content
        file_content=ContentFile(content) 

        # saving the file in the temporary folder
        file_name=fs.save(
            "_temp.csv", file_content
        )

        tmp_file= fs.path(file_name)

        # opening the file in the csv
        csv_file=io_open(tmp_file,errors="ignore")

        # reading the file in the csv format
        reader=csv.reader(csv_file)

        # reading the uploaded file from second line as first line is attributes and the desired data starts from second line
        next(reader)

        # creating candle candle object list
        candle_object=[]

        for idk,row in enumerate(reader):

            (
                id,
                date,
                time,
                open,
                high,
                low,
                close,
                volume,
                
            )=row

            candle_object.append(
                csvmodel(           
                    id=id,
                    date=date,
                    time=time,
                    open=open,
                    high=high,
                    low=low,
                    close=close,
                    volume=volume,
                    
                     
                )
            )
        csvmodel.objects.bulk_create(candle_object)

        return Response("succesfully uploaded the data")
            

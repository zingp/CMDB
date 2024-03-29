#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from web.service import idc


class IDCListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'idc_list.html')


class IDCJsonView(View):
    def get(self, request):
        obj = idc.IDC()
        response = obj.fetch_idc(request)
        return JsonResponse(response.__dict__)

    def delete(self, request):
        response = idc.IDC.delete_idc(request)
        return JsonResponse(response.__dict__)

    def put(self, request):
        response = idc.IDC.put_idc(request)
        return JsonResponse(response.__dict__)

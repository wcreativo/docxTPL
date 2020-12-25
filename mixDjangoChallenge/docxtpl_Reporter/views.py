# Imports Django
from django.http.response import HttpResponse
from django.views.generic import TemplateView

# Import DocxTemplate
from docxtpl import DocxTemplate, InlineImage
import io  # This module is quite useful when you want to perform file-related I/O operations (eg. file reading/writing)
import os  # The OS module in python provides functions for interacting with the operating system #

from docx.shared import Pt


def CreateReporter(request):
    # os.path.dirname(path) : It is used to return the directory name from the path given.
    # This function returns the name from the path except the path name.

    # os.path.abspath(path) returns the pathname to the path passed as a parameter to this function

    BASE_DIR = os.path.dirname(__file__)
    doc = DocxTemplate(os.path.join(BASE_DIR, "templates/docxtpl_Reporter/my_word_template.docx"))
    foto = InlineImage(doc, 'media/Firma.png', width=Pt(100))
    context = {'company_name': "World company",
               'foto': foto
               }

    doc_io = io.BytesIO()  # create a file-like object. Call io module and instance BytesIO class
    # Data can be kept as bytes in an in-memory buffer

    doc.render(context)  # render document using dict context
    doc.save(doc_io)  # save data to file-like object
    doc_io.seek(0)  # go to the beginning of the file-like object
    response = HttpResponse(doc_io.read())   

    # Content-Disposition header makes a file downloadable
    response["Content-Disposition"] = "attachment; filename=" + context['company_name'] + ".docx"

    # Set the appropriate Content-Type for docx file
    response["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

    # Now, it is always a good practice to close our buffer handle whenever we have done our work.
    # This is also to make sure that we free whatever memory we’ve allocated for the buffer.
    doc_io.close()
    return response


class HomeReporter(TemplateView):
    template_name = 'docxtpl_Reporter/index.html'

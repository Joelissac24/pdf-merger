import pytest
from PyPDF2 import PdfMerger
from pdf_merger import pdfmerger
import hashlib
import os


def test_fn():
    cwd = os.getcwd()
    fld = "Test_data"
    pdfmerger(cwd, fld)
    actual_pdf = checks(f"{fld}.pdf")
    expected_pdf = checks("output.pdf")
    assert actual_pdf == expected_pdf


def checks(file):
    md5_hash = hashlib.md5()
    a_file = open(file, "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest

import os
from PyPDF2 import PdfMerger
import shutil


def onlypdf(cwd):
    return (pdffiles for pdffiles in os.scandir(cwd) if pdffiles.name.endswith(".pdf"))


def getfiles(path):
    return [files.name for files in os.scandir(path) if os.path.isfile(files)]


def scanner(cwd, my_folders):
    return (
        folder.name
        for folder in os.scandir(cwd)
        if os.path.isdir(folder) and folder.name in my_folders
    )


def pdfmerger(cwd, fld):
    merger = PdfMerger()
    print(f"Merging {fld} Pdf")
    path = f"{cwd}/{fld}"
    file_lst = getfiles(path)
    for splits in file_lst:
        merger.append(f"{path}/{splits}")
    merger.write(f"{fld}.pdf")
    merger.close


def move_to_output(cwd):
    output_path = f"{cwd}/Output"
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    pdfobj = onlypdf(cwd)
    for pdfs in pdfobj:
        src = f"{cwd}/{pdfs.name}"
        dst = f"{output_path}/{pdfs.name}"
        shutil.move(src, dst)
    print(f">>>>>>>>>All Files Moved file<<<<<<<<")


def main():
    cwd = os.getcwd()
    my_folders = ["Clean", "CPO", "CPO-Range", "Cum-Range", "Cumulative"]
    folderobj = scanner(cwd, my_folders)
    for fld in folderobj:
        pdfmerger(cwd, fld)
    move_to_output(cwd)


if __name__ == "__main__":
    main()

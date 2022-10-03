import os
from PyPDF2 import PdfFileMerger
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


def pdfmerger(cwd, merger, folderobj):
    for fld in folderobj:
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
    merger = PdfFileMerger()
    cwd = os.getcwd()
    my_folders = ["Test_data"]
    folderobj = scanner(cwd, my_folders)
    pdfmerger(cwd, merger, folderobj)
    move_to_output(cwd)


if __name__ == "__main__":
    main()

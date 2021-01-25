import datetime
import plistlib

from html_report.artifact_report import ArtifactHtmlReport
from helpers.ilapfuncs import tsv

from artifacts.Artifact import AbstractArtifact


class LastBuild(AbstractArtifact):

    _name = 'Last Build'
    _search_dirs = ('*LastBuildInfo.plist')
    _category = 'IOS Build'
    _core_artifact = True

    def get(self, files_found, seeker):
        versionnum = 0  # noqa
        data_list = []
        file_found = str(files_found[0])
        with open(file_found, "rb") as fp:
            pl = plistlib.load(fp)
            for key, val in pl.items():
                data_list.append((key, val))
                if key == ("ProductVersion"):
                    # ilapfuncs.globalvars()
                    artifacts.artGlobals.versionf = val
                    logfunc(f"iOS version: {val}")
                    logdevinfo(f"iOS version: {val}")

                if key == "ProductBuildVersion":
                    logdevinfo(f"ProductBuildVersion: {val}")

                if key == ("ProductName"):
                    logfunc(f"Product: {val}")
                    logdevinfo(f"Product: {val}")

        report = ArtifactHtmlReport('iOS Build')
        report.start_artifact_report(report_folder, 'Build Information')
        report.add_script()
        data_headers = ('Key', 'Values')
        report.write_artifact_data_table(data_headers, data_list, file_found)
        report.end_artifact_report()

        tsvname = 'Last Build'
        tsv(report_folder, data_headers, data_list, tsvname)


class ITunesBackupInfo(AbstractArtifact):
    _name = 'iTunesBackup'
    _search_dirs = ('*LastBuildInfo.plist')
    _category = 'IOS Build'

    def get(self, files_found, seeker):
        versionnum = 0  # noqa
        data_list = []
        file_found = str(files_found[0])
        with open(file_found, "rb") as fp:
            pl = plistlib.load(fp)
            for key, val in pl.items():
                if (isinstance(val, str)
                        or isinstance(val, int)
                        or isinstance(val, datetime.datetime)):

                    data_list.append((key, val))
                    if key in ('Build Version', 'Device Name', 'ICCID', 'IMEI',
                               'Last Backup Date', 'MEID', 'Phone Number',
                               'Product Name', 'Product Type',
                               'Product Version', 'Serial Number'):
                        logdevinfo(f"{key}: {val}")

                    if key == ('Product Version'):
                        artifacts.artGlobals.versionf = val
                        logfunc(f"iOS version: {val}")

                elif key == "Installed Applications":
                    data_list.append((key, ', '.join(val)))
        report = ArtifactHtmlReport('iTunes Backup')

        report.start_artifact_report(report_folder,
                                     'iTunes Backup Information')
        report.add_script()
        data_headers = ('Key', 'Values')
        report.write_artifact_data_table(data_headers, data_list, file_found)
        report.end_artifact_report()

        tsvname = 'iTunes Backup'
        tsv(report_folder, data_headers, data_list, tsvname)

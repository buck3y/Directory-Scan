'''
Script:  Directory Scan
Author:  buck3y
Date:    April 1, 2026
Version: 
Purpose: Obtains a list of entries found in a specified directory, 
processes each entry within that directory, and reports back 
metadata regarding each entry.
'''

''' IMPORT STANDARD LIBRARIES '''
import os       # File System Methods
import sys      # System Methods
import time     # Time Conversion Methods

''' IMPORT 3RD PARTY LIBRARIES '''
# NONE

''' DEFINE PSEUDO CONSTANTS '''

# NONE

''' LOCAL FUNCTIONS '''

def GetFileMetaData(fileName):
    ''' 
        obtain filesystem metadata
        from the specified file
        specifically, fileSize and MAC Times
        
        return True, None, fileSize and MacTimeList
    '''
    try:
        
        metaData         = os.stat(fileName)       # Use the stat method to obtain meta data
        fileSize         = metaData.st_size         # Extract fileSize and MAC Times
        timeLastAccess   = metaData.st_atime
        timeLastModified = metaData.st_mtime
        timeCreated      = metaData.st_ctime
        
        humanReadableAccess = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeLastAccess))       # Converts the access time into human readable format
        humanReadableModified = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeLastModified))   # Converts the modified time into human readable format
        humanReadableCreated = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeCreated))         # Converts the creation time into human readable format

            
        macTimeList = [humanReadableModified, humanReadableAccess, humanReadableCreated]
        return True, None, fileSize, macTimeList
    
    except Exception as err:
        return False, str(err), None, None

''' LOCAL CLASSES '''
# NONE

''' MAIN ENTRY POINT '''

if __name__ == '__main__':
    
    print("\nWK-2 Solution: Myles Hurlbut - Version One\n")

    targetDIR = input('Enter a Directory Path i.e. c:/ >>> ')
    print()
    
    try:
        fileList = os.listdir(targetDIR)
        for eachFile in fileList:
            print(eachFile)
            path = os.path.join(targetDIR, eachFile)

            success, errInfo, fileSize, macList = GetFileMetaData(path)
            
            if success == True:
                print(f"Success: {path}") 
                print(f"File Size: {fileSize:,}")
                print(f"Modified-Time: {macList[0]}")
                print(f"Access-Time:   {macList[1]}")
                print(f"Created-Time:  {macList[2]}") 
                print("="*50)
            elif success == False:
                print(errInfo)
            else:
                break
            
            
            # Your additional script code here
            
    except Exception as err:
        print(f"\n\nThe directory path '{targetDIR}' does not exist, try again.")        
        print("\n\nScript Aborted     ", "Exception =     ", err)         

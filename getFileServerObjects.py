import os


def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]
 

#File Example for program
#    {
#     name: "God",
#     deleteable: true,
#     key: "God",
#     parent: "Embarcadero De Banes",
#     src: "filepath",
#   },

# folder example
# name: "Sackville", paths: [], parent: "root", deleteable: false },


# Check the print statements at the end to get the content you want.You will need to generate both the file AND directory lists whenever test2 changes
# Takes these outputs and past them in the Directories.ts and Files.ts in the fileServerExperience project located at functions/FileStructure.
def main(): 
    path = os.getcwd()
    serverFilePath = f"{path}/test2/UNSHUT Servers"
    results = [{"key":serverFilePath,"name":"UNSHUT Servers", "paths":[], "parent": None, "deleteable": 0}]
    for subdir, dirs, files in os.walk(serverFilePath):
        #print(subdir)
        subDirPath = subdir.split("/")
        toAdd = subDirPath[-1]

   
        if toAdd == "test1" or toAdd == 'ConvertDirectoryDocX2Html' or toAdd == 'UNSHUT Servers':
            continue
        parentPathRaw= subDirPath[:-1]
        parentPath = "/".join(parentPathRaw)


        results.append({
            "key": subdir,
            "name": toAdd,
            "paths": [],
            "parent": parentPath,
            "deleteable":1 
        })

        allFiles = addFiles(files, subdir);
        results = results + allFiles
        subdirToCompareSplit = subdir.split("/")[:-1]
        subDirToCompare = "/".join(subdirToCompareSplit)
        #Add to parent path array
        for i in range(len(results)):
            item = results[i]
            #Add subdir relationships
            if item["key"] == subDirToCompare:
               item["paths"].append(subdir)
            #Add file relationships
            #print(subdir)
            for file in files:
                if(item["key"] == f"{subdir}"):
                    
                    item["paths"].append(f"{subdir}/{file}")
    dir = []
    f =[]              
    for res in results:
        if( "paths" in res):
            dir.append(res)
        else:
            f.append(res)


    # If you need the directories
    print(dir)

    # If you need the files
      # print(f)


       
  
def addFiles(files, subdir):
    result =[]
    filePath = subdir.split("/")[8:]
    filePath = "/".join(filePath)
    parentFilePath = "/".join(subdir.split("/")[:-1])
    
    for file in files:
 
        result.append({
            "key": f"{subdir}/{file}",
            "name": file.split('.')[0],
            "deletelable": 1,
            "parent":parentFilePath,
            "src": f"{filePath}/{file}.html"

        })
    return result
    
            
            



main()

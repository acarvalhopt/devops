import yaml


def printDuplicateds(list_of_paths):
    seen = set()
    uniq = []
    for path in list_of_paths:
        if path not in seen:
            uniq.append(path)
            seen.add(path)
        else:
            print("Duplicated: " + path)

with open("/Users/andrecarvalho/Documents/gowithflow/git/kong/files/routes/mobime.yml", 'r') as stream:
# with open("test.yml", 'r') as stream:
    try:
        # print(yaml.safe_load(stream))
        documents = yaml.full_load(stream)
        list_of_paths=[]
        for key1, value1 in documents.items():
            if key1 == "routes":
                for v in value1:
                    for key2,value2 in v.items():
                        if key2 == "paths":
                            list_of_paths.append(str(value2))
                        
        # print("[DEBUG] - Before removal of duplicates:")
        # print(list_of_paths)

        without_dup=list(dict.fromkeys(list_of_paths)) #remove duplicates
        # print()
        # print("[DEBUG] - After removal of duplicates:")
        # print(without_dup)
        # print()
        a_set = set(list_of_paths) #Convert to set.
        contains_duplicates = len(list_of_paths) != len(a_set) #Compare lengths.
        print("[DEBUG] - Contains duplicateds: " + str(contains_duplicates))
        if contains_duplicates:
            printDuplicateds(list_of_paths)
    except yaml.YAMLError as exc:
        print(exc)
import Document_Similarity_demo
import glob

def File_extraction():
    
    # File path of the dataset

    file_path="/home/ajay/Documents/5th Semester/NLP/NLP_Lab_2/data/txt_files/"

    scanned_document_text=[]
    

    for filename in glob.glob(file_path+"*.txt"):
        with open(filename) as f:
            
            string=" "

            
            # Reads the whole text in a text file, 'line by line' and stores in the above declared list (scanned_document_text[])
            

            for line in f:
                string=string + str(line)
            scanned_document_text.append(string)
                
    # print(scanned_document_text)

    return scanned_document_text
    # print(len(scanned_document_text))



def main():
    
    all_files=File_extraction()
    
    for document in range(0, len(all_files)-1):
        # print("Hello!")
        print("Cosine similarity of Document {} and Document {} is : ".format(document+1,document+2)+str(Document_Similarity_demo.main(all_files[document],all_files[document+1])))


if __name__=='__main__':
    main()


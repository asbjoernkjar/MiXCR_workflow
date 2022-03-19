import pandas as pd
import re
import argparse


def extract_info(sample, search_dic):
    """report = report file object""" 
    with open(sample) as report:
        c = re.compile(r'\s\d+') #whitespace followed by number
        
        sample = sample.split("/")[-1].split(".report")[0]
        res_dic = {"Sample_ID":sample}

        for line in report.readlines():
            for query in search_dic.keys():
                if query in line:
                    number = int(re.findall(c,line)[0].strip())
                    print(search_dic[query])

                    res_dic[search_dic[query]]=number

    return res_dic


def create_report(  samples ):

    search_dic = {
            "Total sequencing reads:":"Total_reads",
            "Successfully aligned reads:":"Aligned_reads",
            "Reads used in clonotypes, percent of total:":"Used_reads",
            "Reads clustered in PCR error correction, percent of used:":"PCR_correct_dropped_reads",
            "Clonotypes eliminated by PCR error correction:":"PCR_correct_dropped_clonotypes",
            "TRB chains:":"N_clones", #will report second occurence = clonotype count
    }
    out_list = []

    for sample in samples:
        
        info = extract_info(sample,search_dic)
        out_list.append(info)

    df = pd.DataFrame(out_list)
    df["Fraction_Aligned_reads"] = round(df["Aligned_reads"]/df["Total_reads"],4)
    df["Fraction_Used_reads"] = round(df["Used_reads"]/df["Total_reads"],4)
    df["Fraction_PCR_correct_dropped_reads"] = round(df["PCR_correct_dropped_reads"]/df["Total_reads"],4)

    return df




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--sample_id_name', type=str, default="Sample_ID")
    parser.add_argument('--out_path', type=str, required=True)
    parser.add_argument('--samples', nargs='+', required=True)

    args = parser.parse_args()


    out_df = create_report( args.samples)
    
    out_df = out_df.rename(columns={"Sample_ID":args.sample_id_name})
    
    out_df.to_csv(args.out_path, sep="\t", index=False)
    


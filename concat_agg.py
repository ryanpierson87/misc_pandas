def concat_agg(input_df, column_list, key, additional_columns, character= '; '):
    """function that takes an existing DataFrame, a list of columns that you want to be concat_aggregated, 
    the key column you want things to be grouped together by, 
    and any additional columns you want to appear in the resulting dataframe, also the join value""" 
    output = input_df[[key] + additional_columns].drop_duplicates().reset_index(drop=True)
    for col in column_list:
        agg_col = dict_process(input_df, key, col)
        output = dict_column(agg_col, output, key, col, character)
    return output

# do the dictionary process for each dictionary
def dict_process(df, key, col_to_agg):
    """
    function that returns a dictionary with distinct values of 
    one column as the key value and a an array containing all the values of the second column entered
    dict_process(dataframe, key_column, column_to_aggregate)
    """
    dictio = {}
    loop_df = df[[key, col_to_agg]]
    end = len(loop_df)
    for i in range(end):
        dict_key = loop_df.at[i, key]
        dict_val = str(loop_df.at[i, col_to_agg])
        if dict_key not in dictio:
            dictio[dict_key] = []
            dictio[dict_key].append(dict_val)
        else:
            if dict_val not in dictio[dict_key]:
                dictio[dict_key].append(dict_val)
    return dictio

def dict_column(dic, new_df, key, col, character):
    """
    function that takes a dictionary, dataframe, key/join column value and the specific column_name the concatenated dictionary values will be saved as 
    """
    end = len(new_df)
    for i in range(end):
        anchor = new_df.at[i, key]
        #print(dic[anchor])
        if anchor in dic:
            new_df.at[i, col] = character.join(dic[anchor])
            #print(new_df.at[i, key])
    return new_df

def test():
    print("Welcome to Concat Aggregation That You Can Use!")
    


class Query_stacks(object):
    
    def __init__(self) -> None:
        pass
    
    
    def create_table_query(self,table, field_cases ):
        
        writer = ",".join([f"{key} {value}" for key, value in field_cases.items()])
        
        query=f"CREATE TABLE IF NOT EXISTS {table} (
                 {writer}
                );"
        
        return query
    
    def add_table_query(self, table, render_dict:dict ):
        
        names=render_dict["name_of_fields"]
        
        count_of_fields = render_dict["count_of_fields_as_astring"]
        
        query=f"INSERT INTO {table} ({names}) VALUES ({count_of_fields})"
        
        return query
    
    def update_query_id(self, **kwargs):
        
        table = kwargs["table"]
        keyname = kwargs["key_name"]
        find_keyname = kwargs["find_keyname"] 
        set_value = kwargs["set_value "]
        find_for_value = kwargs["find_for_value"]
        
        query=f"Update {table} SET {keyname} = {set_value} WHERE {find_keyname} = {find_for_value} "
        
        return query
        
        
    def query_params(self,fields:dict):
        
        name_of_fields=", ".join(fields.keys())
        values_of_fields=", ".join(fields.values())
        count_of_fields_as_astring=("? , " * len(fields))[:-2] 
        
        return {
                    "name_of_fields":name_of_fields,
                    "values_of_fields":values_of_fields, 
                    "count_of_fields_as_astring":count_of_fields_as_astring
                }
    
    

    
    
        
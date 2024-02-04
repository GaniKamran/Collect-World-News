from Database.orm_query import Query_stacks

import sqlite3
import asyncio
import aiosqlite
import os

class AsyncManagementSQLiteBase(Query_stacks):
    def __init__(self) -> None:
        super().__init__()
        
    async def initialize(self) -> None:
        os.makedirs('Database', exist_ok=True)
        db_path = os.path.join('Database', 'database.db')
        self.conn = await aiosqlite.connect(db_path)
        self.cursor = await self.conn.cursor()

    async def create_table(self,table, field_cases):
        query= self.create_table_query(table, field_cases)
        await self.cursor.execute(query)


    async def add_table(self, table , fields:dict):
 
        render_dict=self.query_params(fields=fields)
        query=self.add_table_query(table,render_dict)
        values_tuple = tuple(fields.values())
        await self.cursor.execute(query, values_tuple )
      

    async def read_table_selected_property(self):
        await self.cursor.execute("SELECT * FROM database")
        data = await self.cursor.fetchmany()
        for row in data:
            data_dict={
                'id':row[1],
                'name':row[0]
            }
        return data_dict
   
    async def sql_commits(self):
        await self.conn.commit()

    async def set_field(self, **kwargs):
        table_name = kwargs["table_name"]
        keyname = kwargs["key_name"]
        find_keyname = kwargs["find_keyname"] 
        set_value = kwargs["set_value "]
        find_for_value = kwargs["find_for_value"]
        query=self.update_query_id(table = table_name,key_name = keyname, find_keyname = find_keyname, set_value=set_value, find_for_value= find_for_value  )
        await self.cursor.execute(query)

    async def close_connection(self):
        await self.cursor.close() 
        await self.conn.close()


async def main():
    data = {"test": "text", "best": "text"}
    t = AsyncManagementSQLiteBase()
    await t.initialize()
    await t.create_table("database", data)
    await t.add_table("database", data)
    await t.read_table_selected_property()
    await t.sql_commits()

    await t.close_connection()
    # await t.set_namejwt("new_jwt")
    
# Run the event loop
asyncio.run(main())
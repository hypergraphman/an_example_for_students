import query_db
from val_project import *

# print(*query_db.select_table(FILMS, *TABLES[FILMS]), sep='\n')
print(*query_db.select_table(GENRES, TITLE), sep='\n')

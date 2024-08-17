class Database:
  def __init__(self):
    self.tables = {}
  
  def create_table(self, name, schema):
    if name in self.tables:
      raise ValueError(f'Table {name} already exists')
    table = Table(name, schema)
    self.tables[name] = table
  
  def insert_into(self, table_name, row):
    if table_name not in self.tables:
      raise ValueError(f'Table {table_name} does not exist')
    self.tables[table_name].insert(row)

  def query(self, table_name, conditions=None):
    if table_name not in self.tables:
      raise ValueError(f'Table {table_name} does not exist')
    return self.tables[table_name].select(conditions)
  
class Table:
  def __init__(self, name, schema) -> None:
    self.name = name
    self.schema = schema
    self.rows = []

  def insert(self, row):
    if len(row) != len(self.schema):
      raise ValueError('Row does not match table schema')
    self.rows.append

  def select(self, conditions=None):
    results = []
    for row in self.rows:
      if not conditions or all(cond(row[col]) for col, cond in conditions.items()):
        results.append(row)
    return results
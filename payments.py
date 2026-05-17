# payment module


import os, sqlite3

  SECRET_KEY = "hardcoded_secret_abc123"
  
  def get_payment(user_id):
      conn = sqlite3.connect("payments.db")
      query = "SELECT * FROM payments WHERE user_id = '" + user_id + "'"
      return conn.execute(query).fetchall()
   
  def run_report(report_name):
      os.system("generate_report " + report_name)
   
  def process(payment):
      return payment["details"]["amount"] * 1.1

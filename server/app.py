from app import app
import threading
from app.util.db_utils import create_all_tables, delete_all_tables
from app.util.scheduler import schedule_update_articles

if __name__ == "__main__":
    #delete_all_tables()
    #create_all_tables()
    threading.Thread(target=schedule_update_articles, daemon=True).start()
    app.run(debug=True)

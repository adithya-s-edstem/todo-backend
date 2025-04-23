from ..models import db

def handle_db_operation(operation):
    try:
        result = operation()
        db.session.commit()
        return result
    except Exception as e:
        db.session.rollback()
        print(f"[ERROR]: Database operation failed: {e}")
        raise e
    finally:
        db.session.close()

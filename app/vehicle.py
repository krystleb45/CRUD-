
from app.database import get_db


def output_formatter(results: tuple):
    out = []
    for result in results:
        result_dict = {}
        result_dict["id"] = result[0]
        result_dict["license_plate"] = result[1]
        result_dict["v_type"] = result[2]
        result_dict["color"] = result[3]
        result_dict["parking_spot_no"] = result[4]
        result_dict["descritpion"] = result[5]
        result_dict["user_id"] = result[6]
        out.append(result_dict)
    return out


def insert(license_plate, v_type, parking_spot_no, user_id, description, color):
    value_tuple = (license_plate, v_type, color,
                   parking_spot_no, user_id, description)
    query = """
        INSERT INTO user (
            license_plate, 
            v_type, 
            color, 
            parking_spot_no,
            user_id,
            description
        ) VALUES (
            ?, ?, ?, ?
        )
    """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    cursor.close()
    return last_row_id


def scan():
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE user_id=?", (pk,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def read(pk):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE id=?", (pk,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def update(pk, license_plate, v_type, color, parking_spot_no, user_id, description):
    value_tuple = (license_plate, v_type, color,
                   parking_spot_no, user_id, description, pk)
    query = """
        UPDATE vehicle
        SET license_plate=?,
        v_type=?,
        color=?,
        parking_spot_no=?,
        user_id=?,
        description=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(query, value_tuple)
    cursor.commit()

import sqlite3

class Parcel:
    def __init__(self) -> None:
        self.con = sqlite3.connect("website\database\parcel_viewer.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute(
            """
CREATE TABLE IF NOT EXISTS Parcels(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    multipolygon BLOB,
    kivapin INTEGER,
    apn TEXT,
    platname TEXT,
    lot TEXT,
    block TEXT,
    tract TEXT,
    owner_name TEXT,
    owner_name2 TEXT,
    owner_occupied BOOL,
    owner_occupied_str TEXT,
    owner_addr TEXT,
    owner_addr2 TEXT,
    owner_city TEXT,
    owner_state TEXT,
    owner_zip TEXT,
    owner_full_address TEXT,
    address TEXT,
    stret_numb TEXT,
    fraction TEXT,
    prefix TEXT,
    street TEXT,
    street_type TEXT,
    suite TEXT,
    full_address TEXT,
    landusecode TEXT,
    landusedesc TEXT,
    assessed_land_value FLOAT,
    assessed_improved_value FLOAT,
    exempt_land_value FLOAT,
    exempt_improved_value FLOAT,
    assessment_effective_date TEXT,
    legal TEXT,
    shape_area FLOAT,
    shape_len FLOAT)
"""
        )

    def search(self, addr_q):
        self.con = sqlite3.connect("website\database\parcel_viewer.db")
        self.cur = self.con.cursor()
        
        query = self.cur.execute(
            f'SELECT id, multipolygon, address FROM Parcels WHERE address LIKE "{addr_q}%" LIMIT 50'
        )
        result = query.fetchall()
        result_dict = [
            {"id": name[0], "multipolygon": name[1], "address": name[2]}
            for name in result
        ]

        self.con.close()
        return result_dict

    def viewer(self, addr_q):
        query = self.cur.execute(
            f'SELECT id, owner_name, owner_name2, landusecode, landusedesc, assessment_effective_date, assessed_land_value, assessed_improved_value, exempt_land_value, exempt_improved_value, full_address FROM Parcels WHERE id = "{addr_q}"'
        )
        result = list(query.fetchone())
        print(result)
        result_dict = {
            "id": result[0],
            "owner_name": result[1],
            "owner_name2": result[2],
            "landusecode": result[3],
            "landusedesc": result[4],
            "assessment_effective_date": result[5],
            "assessed_land_value": result[6],
            "assessed_improved_value": result[7],
            "exempt_land_value": result[8],
            "exempt_improved_value": result[9],
            "full_address": result[10]
        }
        return result_dict

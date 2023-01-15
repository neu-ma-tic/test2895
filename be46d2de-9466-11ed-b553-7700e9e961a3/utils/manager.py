from constant import Database as Db

db = Db()
main_data = db.loads("PlayerProfiles")

async def add_cp(target: int, amount: int) -> dict:
    if not check(target):
        return {"success": False, "ret": "No Profile"}
    
    cp = main_data[str(target)]["cp"]
    main_data[str(target)]["cp"] += amount

    ret = {"success": True, "ret": "Successfully", "old-cp": cp, "cp": main_data[str(target)]["cp"], "added-amount": amount}

    lv_update = await update_lv_cp(target)
    if lv_update["times"] > 0:
        ret["times"] = lv_update["times"]    

    return ret

async def remove_cp(target: int, amount: int) -> dict:
    if not check(target):
        return {"success": False, "ret": "No Profile"}
    
    if main_data[str(target)]["cp"] - amount < 0:
        return {"success": False, "ret": "Negative Value"}
    
    cp = main_data[str(target)]["cp"]
    main_data[str(target)]["cp"] -= amount

    ret = {"success": True, "ret": "Successfully", "old-cp": cp, "cp": main_data[str(target)]["cp"], "removed-amount": amount}

    lv_update = await update_lv_cp(target)
    if lv_update["times"] < 0:
        ret["times"] = lv_update["times"]   

    return ret

async def add_ocp(target: int, amount: int) -> dict:
    if not check(target):
        return {"success": False, "ret": "No Profile"}
    
    if main_data[str(target)]["ocp"] + amount > 4:
        return {"success": False, "ret": "Exceed Limit"}
    
    ocp = main_data[str(target)]["ocp"]
    main_data[str(target)]["ocp"] += amount

    ret = {"success": True, "ret": "Successfully", "old-ocp": ocp, "ocp": main_data[str(target)]["ocp"], "added-amount": amount}

    lv_update = await update_lv_ocp(target)
    if lv_update["times"] > 0:
        ret["times"] = lv_update["times"]    

    return ret

async def remove_ocp(target: int, amount: int) -> dict:
    if not check(target):
        return {"success": False, "ret": "No Profile"}
    
    if main_data[str(target)]["ocp"] - amount < 0:
        return {"success": False, "ret": "Negative Value"}
    
    ocp = main_data[str(target)]["ocp"]
    main_data[str(target)]["ocp"] -= amount

    ret = {"success": True, "ret": "Successfully", "old-ocp": ocp, "ocp": main_data[str(target)]["ocp"], "removed-amount": amount}

    lv_update = await update_lv_ocp(target)
    if lv_update["times"] < 0:
        ret["times"] = lv_update["times"]   

    return ret


async def create_profile(target: int) -> dict:
    if str(target) in main_data:
        return {"success": False, "ret": "Has Profile"}
    
    main_data[str(target)] = {
        "cp-lv":0, "ocp-lv": 0,
        "cp": 0, "ocp": 0
    }

    save()

    return  {"success": True, "ret": "Succesfully"}

async def delete_profile(target: int) -> dict:
    if not check(target):
        return {"success": False, "ret": "No Profile"}
    
    try:
        del main_data[str(target)]
    except Exception as e:
        return {"success": False, "ret": e}
    save()
    return  {"success": True, "ret": "Succesfully"}

async def update_lv_cp(target: int) -> dict:
    if not check(target):
        return {"success": False, "ret": "No Profile"}
    # print("Updating Level")
    
    cp = main_data[str(target)]["cp"]
    o_lv = main_data[str(target)]["cp-lv"]

    if cp >= 30: lv = 5
    elif cp >= 17: lv = 4
    elif cp >= 10: lv = 3
    elif cp >= 5: lv = 2
    elif cp >= 1: lv = 1
    else: lv = 0

    if main_data[str(target)]["cp-lv"] != lv:
        main_data[str(target)]["cp-lv"] = lv
        # print("New Level", lv)
    
    save()
    return {"success": True, "ret": "Succesfully", "times": o_lv - lv, "from": o_lv, "to": lv}

async def update_lv_ocp(target: int) -> dict:
    if not check(target):
        return {"success": False, "ret": "No Profile"}
    # print("Updating Level")
    
    ocp = main_data[str(target)]["ocp"]
    o_lv = main_data[str(target)]["ocp-lv"]

    lv = ocp

    if main_data[str(target)]["ocp-lv"] != lv:
        main_data[str(target)]["ocp-lv"] = lv
        # print("New Level", lv)
    
    save()
    return {"success": True, "ret": "Succesfully", "times": o_lv - lv, "from": o_lv, "to": lv}    

def check(target: int) -> bool:
    return str(target) in main_data

def get_data(target: int) -> dict:
    if not check(target):
        return {"success": False, "ret": "No Profile"}
    
    return {"success": True, "ret": "Succesfully", "data": main_data[str(target)]}

def save() -> None:
    db.dumps("PlayerProfiles", main_data)
    # print("Saved")
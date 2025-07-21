from src.cmdb_loader import load_cmdb_data
from src.csdm_mapper import map_to_csdm
from src.validator import validate_data
from src.servicenow_api import push_to_servicenow

if __name__ == "__main__":
    data = load_cmdb_data("data/cmdb_sample.csv")
    csdm_data = map_to_csdm(data)
    valid_data = validate_data(csdm_data)
    push_to_servicenow(valid_data)

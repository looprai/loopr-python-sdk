# tmp file
# just for testing purpose
from loopr.client import LooprClient

if __name__ == "__main__":
    API_KEY="bb7e239b-e4f5-4cef-a247-9f58517cf237"
    API_ENDPOINT="https://dev-api.loopr.ai/"
    loopr_client = LooprClient(api_key=API_KEY,endpoint=API_ENDPOINT)
    dataset =loopr_client.create_dataset(type="image",name="test-data9", slug="test-data100" )
    print(dataset)
    dataset.delete()
    paired_type = {'query': 'text', 'data': 'image'}
    dataset1 = loopr_client.create_dataset(type="paired", name="text-image-dataa", slug="text-image-dataa", paired_type=paired_type)
    print(dataset1)
    dataset1.delete()

    datasets = loopr_client.get_datasets()
    for data in datasets:
        print(data)

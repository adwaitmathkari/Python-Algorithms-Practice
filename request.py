import requests
import json


headers = {
    'Authorization': 'Key 66cc264da42f469d9ef5e3e5e1038145',
    'Content-Type': 'application/json',
}

data = {
    "inputs": [
        {"data": {
            "image": {"url": "https://cdn.pixabay.com/photo/2018/05/26/10/54/strawberries-3431122__340.jpg"}
            }}]}

url = 'https://api.clarifai.com/v2/models/bd367be194cf45149e75f01d59f77ba7/outputs'

response = requests.post(url, headers=headers, data=json.dumps(data))
# print(response.json())

categories=[]
for concept in response.json()['outputs'][0]['data']['concepts']:   
    categories.append(concept['name'])

print(categories)



a = {
    'status': 
        {'code': 10000, 'description': 'Ok', 'req_id': 'ac58e7a72c6f41d19381a23962d35356'}, 
        
    'outputs': 
    [
        {
            'id': '7ee660d792a24a99aab43c91a85970ff', 
            'status': {'code': 10000, 'description': 'Ok'}, 
            'created_at': '2020-05-17T19:41:58.038995587Z', 
            'model': {'id': 'bd367be194cf45149e75f01d59f77ba7', 
            'name': 'food-items-v1.0', 'created_at': '2016-09-17T22:18:59.955626Z', 
            'app_id': 'main', 
            'output_info': {
                'output_config': {'concepts_mutually_exclusive': False, 'closed_environment': False, 'max_concepts': 0, 'min_value': 0}, 
                'message': 'Show output_info with: GET /models/{model_id}/output_info', 
                'type': 'concept', 
                'type_ext': 'concept'}, 
            'model_version': {
                'id': 'dfebc169854e429086aceb8368662641', 
                'created_at': '2016-09-17T22:18:59.955626Z', 
                'status': {'code': 21100, 'description': 'Model is trained and ready'}, 
                'worker_id': 'a0966e7403e8488fb9f23b17517be638'}, 
                'display_name': 'Food'}, 
            'input': {'id': 'bdac43f6579e4477941bbc3a94873696', 'data': {'image': {'url': 'https://cdn.pixabay.com/photo/2018/05/26/10/54/strawberries-3431122__340.jpg'}}}, 
            'data': {
                'concepts': [
                    {'id': 'ai_JQV7LmzG', 'name': 'berry', 'value': 0.999804, 'app_id': 'main'}, 
                    {'id': 'ai_JXCD9lx9', 'name': 'strawberry', 'value': 0.9995922, 'app_id': 'main'}, 
                    {'id': 'ai_0wh0dJkQ', 'name': 'sweet', 'value': 0.99915063, 'app_id': 'main'}, 
                    {'id': 'ai_rpDBJsjW', 'name': 'pasture', 'value': 0.9516978, 'app_id': 'main'}, 
                    {'id': 'ai_r59dFMqd', 'name': 'juice', 'value': 0.71543944, 'app_id': 'main'}, 
                    {'id': 'ai_v65hxxVH', 'name': 'raspberry', 'value': 0.43285745, 'app_id': 'main'}, 
                    {'id': 'ai_JhvjJBVt', 'name': 'jam', 'value': 0.40522242, 'app_id': 'main'}, 
                    {'id': 'ai_NDbbpCv1', 'name': 'vegetable', 'value': 0.39559364, 'app_id': 'main'}, 
                    {'id': 'ai_C91DX0qm', 'name': 'goji berry', 'value': 0.3313353, 'app_id': 'main'}, 
                    {'id': 'ai_MW9k9bfX', 'name': 'sweet cherry', 'value': 0.21694644, 'app_id': 'main'}, 
                    {'id': 'ai_PWmbd19r', 'name': 'cream', 'value': 0.21157962, 'app_id': 'main'}, 
                    {'id': 'ai_R4G0kcZQ', 'name': 'mint', 'value': 0.1918796, 'app_id': 'main'}, 
                    {'id': 'ai_TtT3b8dX', 'name': 'cherry', 'value': 0.16759583, 'app_id': 'main'}, 
                    {'id': 'ai_VzGdVRcX', 'name': 'collation', 'value': 0.15854235, 'app_id': 'main'}, 
                    {'id': 'ai_PbPLrZH1', 'name': 'milk', 'value': 0.15165347, 'app_id': 'main'}, 
                    {'id': 'ai_NBPwKswX', 'name': 'fruit tea', 'value': 0.1503931, 'app_id': 'main'}, 
                    {'id': 'ai_dFFRXlSP', 'name': 'comestible', 'value': 0.1394642, 'app_id': 'main'}, 
                    {'id': 'ai_J3zjXXZX', 'name': 'fruit salad', 'value': 0.13885131, 'app_id': 'main'}, 
                    {'id': 'ai_RZgNXv7K', 'name': 'aliment', 'value': 0.13168499, 'app_id': 'main'}, 
                    {'id': 'ai_wXt5mZpW', 'name': 'redcurrant', 'value': 0.11094358, 'app_id': 'main'}
                ]
            }
        }
    ]
    
}




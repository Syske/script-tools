import json
import os;

file = open('D:\\workspace\\learning\\script-tools\\edit_project.txt', 'r', encoding='utf8')
content = file.read();
text = json.loads(content)
for stage in text['stage_content']['stages']:
	if 'resources' in stage:
		for resource in stage['resources']:
			if resource['courseType'] == 17:
				print(resource)
				print(resource['title'], resource['course_id'])
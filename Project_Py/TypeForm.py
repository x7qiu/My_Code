import requests
import unicodecsv
import time
import pprint 

API_KEY = 'ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d'
#API_KEY = '12f95bdf19455242579ccc0c0a3402448fb441d8'

# To Do List
# 1) multiple choice handling
# 2) error handling


class TypeForm(object):

    def __init__(self, key):
        self.key = key
        self.uids = []

    def getforms(self):
        url = 'https://api.typeform.com/v1/forms?key=' + self.key
        resp = requests.get(url)
        data = resp.json()
        for item in data:
            self.uids.append(item['id'])
        

    def fetch(self):
        self.getforms()

        qids = {}   # {qid1 : ans1, qid2 : ans2, ...}
        table = {}  # {q1 : ans1, q2 : ans2, ...}

        for uid in self.uids:
            # Send HTTP requests to each form
            url = 'https://api.typeform.com/v1/form/' + uid + '?key=' + self.key
            resp = requests.get(url)
            data = resp.json()


            for forms in data['responses']:
                if forms['completed'] == u'0':      # skip if form not completed
                    continue
                else:
                    answer_info = forms['answers']
                    for (qid, answer) in answer_info.iteritems():
                        if qid not in qids:
                            qids[qid] = [answer]
                        else:
                            qids[qid].append(answer)

            for question_info in data['questions']:
                fid = question_info['field_id']
                qid = question_info['id']
                question = question_info['question']

                if qid in qids:
                    table[question] = qids[qid]
                else:
                    table[question] = ['NaN']
            
            # pause to avoid API access limit
            time.sleep(5)
            

        #pprint.pprint(table)        
        with open('data.csv', 'wb') as outfile:
            writer = unicodecsv.writer(outfile)
            for key, value in table.items():
                ans = ','.join(str(x) for x in value)
                writer.writerow([key, ans])
               
        
                    
            
test = TypeForm(API_KEY)
test.fetch()

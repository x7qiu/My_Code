import requests
import unicodecsv   # To handle unicode in some of the questions and answers
import time         # Use time.sleep() to stay under access limit 
import sys

API_KEY = 'ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d'
#API_KEY = '12f95bdf19455242579ccc0c0a3402448fb441d8'       # my account & test API


class TypeForm(object):
    def __init__(self, key):
        self.key = key
        self.uids = []      # populated in getforms()

    def getforms(self):
        url = 'https://api.typeform.com/v1/forms?key=' + self.key
        try:
            resp = requests.get(url)
        except requests.exceptions.RequestException as e:
            print e
            sys.exit(1)

        data = resp.json()
        for item in data:
            self.uids.append(item['id'])
        

    def fetch(self):
        self.getforms()

        # Use dictionary for fast lookup on potentially large datasets. Ordering is lost.
        # Assume this is not important. If otherwise, can use a python list. 

        qids = {}       # (qid, [answer]) pairs
        table = {}      # (question, [answer]) pairs

        for uid in self.uids:
            url = 'https://api.typeform.com/v1/form/' + uid + '?key=' + self.key
            try:
                resp = requests.get(url)
            except requests.exceptions.RequestException as e:
                print e
                sys.exit(1)
            data = resp.json()

            # qids{} -> {qid1 : ans1, qid2 : ans2, ...}
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

            # table{} -> {quest1 : ans1, quest2 : ans2, ...}
            for question_info in data['questions']:
                fid = question_info['field_id']
                qid = question_info['id']
                question = question_info['question']

                # handle multiple choice questions. (same question with different qids)
                if question in table:
                    if qid in qids:                 # same q, different qid
                        table[question].extend(qids[qid])
                    else:
                        pass
                else:
                    if qid in qids:
                        table[question] = qids[qid]
                    else:
                        table[question] = ['NaN']

            # pause to avoid API access limit
            time.sleep(1)
            
        with open('data.csv', 'wb') as outfile:
            writer = unicodecsv.writer(outfile)
            for question, answers in table.items():
                answers = ','.join(str(x) for x in answers)   # flatten list 
                writer.writerow([question, answers])
               
if __name__ == "__main__":
    test = TypeForm(API_KEY)
    test.fetch()



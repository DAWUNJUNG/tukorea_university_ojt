from fastapi import FastAPI, File, UploadFile

app = FastAPI
supportFileList = ['csv']

@app.post('/learning/file')
async def learnFile(file: UploadFile = File()):
    try:
        if file.content_type not in supportFileList:
            raise Exception('지원 대상 파일이 아닙니다.')

        file.read()

    except Exception as e:
        return {'result': 'fail', 'message': e}


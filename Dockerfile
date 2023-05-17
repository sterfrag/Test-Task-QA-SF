FROM python:3.7

ADD api_server.py .
ADD Dummy_DB.json .
ADD run_server.bat .
ADD Run_TestSuite.bat .
ADD Test_Suite.py .

RUN pip install fastapi
RUN pip install pydantic
RUN pip install typing
RUN pip install asyncio
RUN pip install uvicorn
RUN pip install requests

CMD ["run_server.bat"]
CMD ["Run_TestSuite.bat"]

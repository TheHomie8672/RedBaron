import redbaron
import openai
import time
import random
import concurrent.futures
from redbaron import output_text
from redbaron import *



def ValCheckGPT1():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            openai.Completion.create, 
            engine="text-davinci-003",
            prompt=f"Check the provided input for any errors or mistakes and correct them. Provide ONLY the corrected material." + output_text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.3
        )
    return future.result().choices[0].text.strip()


def ValCheckGPT2():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(
            openai.Completion.create, 
            engine="text-davinci-003",
            prompt=f"Check the provided input for any errors or mistakes and correct them. Provide ONLY the corrected material." + output_text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.3
        )
    return future.result().choices[0].text.strip()

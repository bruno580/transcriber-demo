# -*- coding: utf-8 -*-
import boto3
import argparse
from botocore.exceptions import ClientError

ap = argparse.ArgumentParser(prog="transcriber")
ap.add_argument("--job-name", nargs="?", required=True, help="Job Name")
ap.add_argument("--media-uri", nargs="?", required=True, help="Link to the input media: http://example.com/audio.m4a")
ap.add_argument("--language-code", nargs="?", default="en-US", required=False, help="Language code. Default: en-US")
args = vars(ap.parse_args())

jobname = args['job_name']
mediauri = args['media_uri']
langcode = args['language_code']

def transcribe(jobname,mediauri,langcode):
    try:       
        client = boto3.client('transcribe')
        response = client.start_transcription_job(
            TranscriptionJobName=jobname,
            LanguageCode=langcode,
            MediaFormat='mp4',
            Media={
                'MediaFileUri': mediauri
            }
        )
    except ClientError as e:
        print("Error: %s" % e)

transcribe(jobname,mediauri,langcode)
import io
from google.oauth2 import service_account
from google.cloud import speech, storage

client_credentials = service_account.Credentials.from_service_account_file('./sa_speech.json')
client = speech.SpeechClient(credentials=client_credentials)
print('client created')
storage_client = storage.Client.from_service_account_json('./sa_speech.json') # change to your own service account
bucket = storage_client.get_bucket('punnyozbucketforone')
audio_files = bucket.list_blobs(prefix='wav/')
print('audio_files created')
for audio_file in audio_files:
    gcs_uri = 'gs://punnyozbucketforone/' + audio_file.name
    print(gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US',
        audio_channel_count=1,
    )

    audio = speech.RecognitionAudio(uri=gcs_uri)
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)

    for result in response.results:
        # print('Transcript: {}'.format(result.alternatives[0].transcript))
        # print('Confidence: {}'.format(result.alternatives[0].confidence))

        with open('./transcript_output2/' + audio_file.name.split('.')[0][4:] + '.txt', 'a') as f:
            f.write('{}'.format(result.alternatives[0].transcript))
            f.write('\n')

    

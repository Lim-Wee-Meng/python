import boto3

polly_client = boto3.Session(
                aws_access_key_id=AKIAWDNZVY5V7JVCY7N6,                     
    aws_secret_access_key=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,
    region_name='ap-southeast-1').client('Remy_TTS')

response = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = 'This is a sample text to be synthesized.')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()

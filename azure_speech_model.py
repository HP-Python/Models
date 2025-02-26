import azure.cognitiveservices.speech as speechsdk
import os


class AzureSpeechModel:
    """
    Azure语音模型
    需要pip install azure-cognitiveservices-speech
    创建实例后，调用speek()方法进行语音合成
    """

    def __init__(self):

        speech_key = os.getenv("SPEECH_KEY")
        region = os.getenv("SPEECH_REGION")

        # 设置语音配置
        self.speech_config = speechsdk.SpeechConfig(
            subscription=speech_key, region=region
        )
        # zh-CN-XiaochenMultilingualNeural  # 选择语音角色

        # 设置语音输出为默认扬声器
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        # 创建一个语音合成器
        self.synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config, audio_config=self.audio_config
        )

    def speek(
        self, in_voice_name="zh-CN-XiaochenMultilingualNeural", in_text=None
    ) -> None:
        # 合成语音
        ssml = """<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='zh-CN'>
        <voice name='{}'>
            {}
        </voice>
        </speak>""".format(
            in_voice_name, in_text
        )
        print(ssml)
        _ = self.synthesizer.speak_ssml_async(ssml).get()


if __name__ == "__main__":
    app = AzureSpeechModel()

    text = "在一个遥远的小村庄里"

    app.speek(in_text=text)

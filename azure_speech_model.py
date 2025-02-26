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
        self.speech_config.speech_synthesis_voice_name = (
            "zh-CN-XiaochenMultilingualNeural"  # 选择语音角色
        )

        # 设置语音输出为默认扬声器
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        # 创建一个语音合成器
        self.synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config, audio_config=self.audio_config
        )

    def speek(self, input_text: str) -> None:
        # 合成语音
        _ = self.synthesizer.speak_text_async(input_text).get()


if __name__ == "__main__":
    app = AzureSpeechModel()

    text = "在一个遥远的小村庄里"

    app.speek(input_text=text)

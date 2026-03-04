---
layout: default
title: An Investigation Into Various Approaches For Bengali Long-Form Speech Transcription and Bengali Speaker Diarization
---

# An Investigation Into Various Approaches For Bengali Long-Form Speech Transcription and Bengali Speaker Diarization
**arXiv**：[2603.03158v1](https://arxiv.org/abs/2603.03158) · [PDF](https://arxiv.org/pdf/2603.03158.pdf)  
**作者**：Epshita Jahan, Khandoker Md Tanjinul Islam, Pritom Biswas, Tafsir Al Nafin  

**一句话要点**：提出多阶段方法，结合微调Whisper和自定义分割模型，解决孟加拉语长语音转录与说话人日志任务。

**关键词**：孟加拉语语音识别, 说话人日志, Whisper模型, 低资源语言, 语音活动检测, 多阶段处理

## 3 点简述
- 针对孟加拉语低资源场景，处理小时级录音的转录和说话人日志挑战。
- 采用Whisper Medium微调进行转录，集成pyannote说话人日志模型与自定义分割模型。
- 通过两阶段方法和超参数调优，在私有榜上实现DER 0.27和WER 0.38。

## 摘要（原文）

> Bengali remains a low-resource language in speech technology, especially for complex tasks like long-form transcription and speaker diarization. This paper presents a multistage approach developed for the "DL Sprint 4.0 - Bengali Long-Form Speech Recognition" and "DL Sprint 4.0 - Bengali Speaker Diarization" competitions on Kaggle, addressing the challenge of "who spoke when/what" in hour-long recordings. We implemented Whisper Medium fine-tuned on Bengali data (bengaliAI/tugstugi bengaliai-asr whisper-medium) for transcription and integrated pyannote/speaker-diarization-community-1 with our custom-trained segmentation model to handle diverse and noisy acoustic environments. Using a two-pass method with hyperparameter tuning, we achieved a DER of 0.27 on the private leaderboard and 0.19 on the public leaderboard. For transcription, chunking, background noise cleaning, and algorithmic post-processing yielded a WER of 0.38 on the private leaderboard. These results show that targeted tuning and strategic data utilization can significantly improve AI inclusivity for South Asian languages. All relevant code is available at: https://github.com/Short-Potatoes/Bengali-long-form-transcription-and-diarization.git
>   Index Terms: Bengali speech recognition, speaker diarization, Whisper, ASR, low-resource languages, pyannote, voice activity detection


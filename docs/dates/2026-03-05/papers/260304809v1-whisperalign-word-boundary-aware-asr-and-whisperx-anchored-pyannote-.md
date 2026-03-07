---
layout: default
title: WhisperAlign: Word-Boundary-Aware ASR and WhisperX-Anchored Pyannote Diarization for Long-Form Bengali Speech
---

# WhisperAlign: Word-Boundary-Aware ASR and WhisperX-Anchored Pyannote Diarization for Long-Form Bengali Speech
**arXiv**：[2603.04809v1](https://arxiv.org/abs/2603.04809) · [PDF](https://arxiv.org/pdf/2603.04809.pdf)  
**作者**：Aurchi Chowdhury, Rubaiyat -E-Zaman, Sk. Ashrafuzzaman Nafees  

**一句话要点**：提出WhisperAlign和WhisperX锚定的Pyannote说话人日志方法，以解决孟加拉语长语音识别和说话人日志挑战。

**关键词**：长语音识别, 说话人日志, 孟加拉语语音处理, 时间戳分块, 模型微调, 低资源语音技术

## 3 点简述
- 核心问题：处理长语音、多说话人孟加拉语音频，面临语音活动检测、重叠语音和上下文保持的困难。
- 方法要点：采用Whisper时间戳音频分块策略，结合微调声学模型进行高精度转录；集成Pyannote和WhisperX，微调分割模型以捕捉孟加拉语对话动态。
- 实验或效果：在低资源设置下，显著降低词错误率和说话人日志错误率。

## 摘要（原文）

> This paper presents our solution for the DL Sprint 4.0, addressing the dual challenges of Bengali Long-Form Speech Recognition (Task 1) and Speaker Diarization (Task 2). Processing long-form, multi-speaker Bengali audio introduces significant hurdles in voice activity detection, overlapping speech, and context preservation. To solve the long-form transcription challenge, we implemented a robust audio chunking strategy utilizing whisper-timestamped, allowing us to feed precise, context-aware segments into our fine-tuned acoustic model for high-accuracy transcription. For the diarization task, we developed an integrated pipeline leveraging pyannote.audio and WhisperX. A key contribution of our approach is the domain-specific fine-tuning of the Pyannote segmentation model on the competition dataset. This adaptation allowed the model to better capture the nuances of Bengali conversational dynamics and accurately resolve complex, overlapping speaker boundaries. Our methodology demonstrates that applying intelligent timestamped chunking to ASR and targeted segmentation fine-tuning to diarization significantly drives down Word Error Rate (WER) and Diarization Error Rate (DER), in low-resource settings.


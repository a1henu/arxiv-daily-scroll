---
layout: default
title: WhisperAlign: Word-Boundary-Aware ASR and WhisperX-Anchored Pyannote Diarization for Long-Form Bengali Speech
---

# WhisperAlign: Word-Boundary-Aware ASR and WhisperX-Anchored Pyannote Diarization for Long-Form Bengali Speech
**arXiv**：[2603.04809v1](https://arxiv.org/abs/2603.04809) · [PDF](https://arxiv.org/pdf/2603.04809.pdf)  
**作者**：Aurchi Chowdhury, Rubaiyat -E-Zaman, Sk. Ashrafuzzaman Nafees  

**一句话要点**：提出WhisperAlign方法，结合时间戳分块ASR和微调分割模型，以解决孟加拉语长语音识别和说话人日志任务。

**关键词**：长语音识别, 说话人日志, 时间戳分块, 模型微调, 孟加拉语处理, 低资源语音处理

## 3 点简述
- 核心问题：处理长时、多说话人孟加拉语音频，面临语音活动检测、重叠语音和上下文保持挑战。
- 方法要点：采用Whisper时间戳分块策略进行ASR，并微调Pyannote分割模型以优化说话人边界识别。
- 实验或效果：在低资源设置下，显著降低词错误率和说话人日志错误率。

## 摘要（原文）

> This paper presents our solution for the DL Sprint 4.0, addressing the dual challenges of Bengali Long-Form Speech Recognition (Task 1) and Speaker Diarization (Task 2). Processing long-form, multi-speaker Bengali audio introduces significant hurdles in voice activity detection, overlapping speech, and context preservation. To solve the long-form transcription challenge, we implemented a robust audio chunking strategy utilizing whisper-timestamped, allowing us to feed precise, context-aware segments into our fine-tuned acoustic model for high-accuracy transcription. For the diarization task, we developed an integrated pipeline leveraging pyannote.audio and WhisperX. A key contribution of our approach is the domain-specific fine-tuning of the Pyannote segmentation model on the competition dataset. This adaptation allowed the model to better capture the nuances of Bengali conversational dynamics and accurately resolve complex, overlapping speaker boundaries. Our methodology demonstrates that applying intelligent timestamped chunking to ASR and targeted segmentation fine-tuning to diarization significantly drives down Word Error Rate (WER) and Diarization Error Rate (DER), in low-resource settings.


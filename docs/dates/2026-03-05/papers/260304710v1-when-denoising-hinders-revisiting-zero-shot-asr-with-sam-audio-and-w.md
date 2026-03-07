---
layout: default
title: When Denoising Hinders: Revisiting Zero-Shot ASR with SAM-Audio and Whisper
---

# When Denoising Hinders: Revisiting Zero-Shot ASR with SAM-Audio and Whisper
**arXiv**：[2603.04710v1](https://arxiv.org/abs/2603.04710) · [PDF](https://arxiv.org/pdf/2603.04710.pdf)  
**作者**：Akif Islam, Raufun Nahar, Md. Ekramul Hamid  

**一句话要点**：揭示SAM-Audio降噪预处理在零样本ASR中降低Whisper性能，挑战音频质量提升必有益于识别的假设。

**关键词**：零样本语音识别, 语音增强, 降噪预处理, Whisper模型, 音频质量与识别性能

## 3 点简述
- 核心问题：检验音频质量提升是否直接有益于零样本ASR性能，挑战常见直觉。
- 方法要点：使用SAM-Audio作为预处理，结合Whisper进行零样本转录，系统评估降噪影响。
- 实验或效果：在孟加拉语和英语数据集上，SAM-Audio预处理导致WER和CER增加，性能随模型规模恶化。

## 摘要（原文）

> Recent advances in automatic speech recognition (ASR) and speech enhancement have led to a widespread assumption that improving perceptual audio quality should directly benefit recognition accuracy. In this work, we rigorously examine whether this assumption holds for modern zero-shot ASR systems. We present a systematic empirical study on the impact of Segment Anything Model Audio by Meta AI, a recent foundation-scale speech enhancement model proposed by Meta, when used as a preprocessing step for zero-shot transcription with Whisper. Experiments are conducted across multiple Whisper model variants and two linguistically distinct noisy speech datasets: a real-world Bengali YouTube corpus and a publicly available English noisy dataset. Contrary to common intuition, our results show that SAM-Audio preprocessing consistently degrades ASR performance, increasing both Word Error Rate (WER) and Character Error Rate (CER) compared to raw noisy speech, despite substantial improvements in signal-level quality. Objective Peak Signal-to-Noise Ratio analysis on the English dataset confirms that SAM-Audio produces acoustically cleaner signals, yet this improvement fails to translate into recognition gains. Therefore, we conducted a detailed utterance-level analysis to understand this counterintuitive result. We found that the recognition degradation is a systematic issue affecting the majority of the audio, not just isolated outliers, and that the errors worsen as the Whisper model size increases. These findings expose a fundamental mismatch: audio that is perceptually cleaner to human listeners is not necessarily robust for machine recognition. This highlights the risk of blindly applying state-of-the-art denoising as a preprocessing step in zero-shot ASR pipelines.


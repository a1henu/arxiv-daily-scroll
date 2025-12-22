---
layout: default
title: When De-noising Hurts: A Systematic Study of Speech Enhancement Effects on Modern Medical ASR Systems
---

# When De-noising Hurts: A Systematic Study of Speech Enhancement Effects on Modern Medical ASR Systems
**arXiv**：[2512.17562v1](https://arxiv.org/abs/2512.17562) · [PDF](https://arxiv.org/pdf/2512.17562.pdf)  
**作者**：Sujal Chondhekar, Vasanth Murukuri, Rushabh Vasani, Sanika Goyal, Rajshree Badami, Anushree Rana, Sanjana SN, Karthik Pandia, Sulabh Katiyar, Neha Jagadeesh, Sankalp Gulati  

**一句话要点**：揭示语音增强预处理在现代医疗ASR系统中普遍损害性能，建议避免使用

**关键词**：语音增强, 医疗ASR, 噪声鲁棒性, 语义WER, 系统评估, 预处理影响

## 3 点简述
- 核心问题：语音增强方法在现代大规模ASR模型中的有效性未知，尤其在医疗场景下。
- 方法要点：系统评估MetricGAN-plus-voicebank去噪对四种先进ASR模型的影响，使用500条医疗语音和九种噪声条件。
- 实验或效果：增强音频在所有40个配置中均导致语义WER增加，降级范围1.1%至46.6%，表明传统增强可能移除关键声学特征。

## 摘要（原文）

> Speech enhancement methods are commonly believed to improve the performance of automatic speech recognition (ASR) in noisy environments. However, the effectiveness of these techniques cannot be taken for granted in the case of modern large-scale ASR models trained on diverse, noisy data. We present a systematic evaluation of MetricGAN-plus-voicebank denoising on four state-of-the-art ASR systems: OpenAI Whisper, NVIDIA Parakeet, Google Gemini Flash 2.0, Parrotlet-a using 500 medical speech recordings under nine noise conditions. ASR performance is measured using semantic WER (semWER), a normalized word error rate (WER) metric accounting for domain-specific normalizations. Our results reveal a counterintuitive finding: speech enhancement preprocessing degrades ASR performance across all noise conditions and models. Original noisy audio achieves lower semWER than enhanced audio in all 40 tested configurations (4 models x 10 conditions), with degradations ranging from 1.1% to 46.6% absolute semWER increase. These findings suggest that modern ASR models possess sufficient internal noise robustness and that traditional speech enhancement may remove acoustic features critical for ASR. For practitioners deploying medical scribe systems in noisy clinical environments, our results indicate that preprocessing audio with noise reduction techniques might not just be computationally wasteful but also be potentially harmful to the transcription accuracy.


---
layout: default
title: ARCHI-TTS: A flow-matching-based Text-to-Speech Model with Self-supervised Semantic Aligner and Accelerated Inference
---

# ARCHI-TTS: A flow-matching-based Text-to-Speech Model with Self-supervised Semantic Aligner and Accelerated Inference
**arXiv**：[2602.05207v1](https://arxiv.org/abs/2602.05207) · [PDF](https://arxiv.org/pdf/2602.05207.pdf)  
**作者**：Chunyat Wu, Jiajun Deng, Zhengxi Liu, Zheqi Dai, Haolin He, Qiuqiang Kong  

**一句话要点**：提出ARCHI-TTS，通过自监督语义对齐器和加速推理策略，解决文本-语音对齐建模难和计算开销高的问题。

**关键词**：文本到语音合成, 流匹配模型, 语义对齐, 加速推理, 非自回归生成

## 3 点简述
- 核心问题：基于扩散的非自回归TTS系统面临文本-语音对齐建模困难和迭代去噪计算开销高的挑战。
- 方法要点：采用自监督语义对齐器确保文本与音频的时序和语义一致性，并重用编码器特征加速推理。
- 实验或效果：在LibriSpeech-PC和SeedTTS数据集上实现低WER和高推理效率，优于现有先进系统。

## 摘要（原文）

> Although diffusion-based, non-autoregressive text-to-speech (TTS) systems have demonstrated impressive zero-shot synthesis capabilities, their efficacy is still hindered by two key challenges: the difficulty of text-speech alignment modeling and the high computational overhead of the iterative denoising process. To address these limitations, we propose ARCHI-TTS that features a dedicated semantic aligner to ensure robust temporal and semantic consistency between text and audio. To overcome high computational inference costs, ARCHI-TTS employs an efficient inference strategy that reuses encoder features across denoising steps, drastically accelerating synthesis without performance degradation. An auxiliary CTC loss applied to the condition encoder further enhances the semantic understanding. Experimental results demonstrate that ARCHI-TTS achieves a WER of 1.98% on LibriSpeech-PC test-clean, and 1.47%/1.42% on SeedTTS test-en/test-zh with a high inference efficiency, consistently outperforming recent state-of-the-art TTS systems.


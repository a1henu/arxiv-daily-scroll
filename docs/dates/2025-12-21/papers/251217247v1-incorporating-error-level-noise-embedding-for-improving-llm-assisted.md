---
layout: default
title: Incorporating Error Level Noise Embedding for Improving LLM-Assisted Robustness in Persian Speech Recognition
---

# Incorporating Error Level Noise Embedding for Improving LLM-Assisted Robustness in Persian Speech Recognition
**arXiv**：[2512.17247v1](https://arxiv.org/abs/2512.17247) · [PDF](https://arxiv.org/pdf/2512.17247.pdf)  
**作者**：Zahra Rahmani, Hossein Sameti  

**一句话要点**：提出结合误差级别噪声嵌入的LLM辅助框架，以提升波斯语语音识别在噪声环境下的鲁棒性。

**关键词**：波斯语语音识别, 噪声鲁棒性, 误差级别噪声嵌入, LLM辅助纠错, 多假设融合

## 3 点简述
- 核心问题：波斯语等低资源语言ASR在噪声环境中性能显著下降，现有模型如Whisper难以保持准确性。
- 方法要点：引入误差级别噪声（ELN）嵌入，量化噪声引起的语义和词级不一致，结合多假设和噪声感知建模进行LLM辅助纠错。
- 实验或效果：在混合噪声测试集上，ELN条件模型将词错误率从31.10%降至24.84%，显著优于无ELN的文本基线。

## 摘要（原文）

> Automatic Speech Recognition (ASR) systems suffer significant performance degradation in noisy environments, a challenge that is especially severe for low-resource languages such as Persian. Even state-of-the-art models such as Whisper struggle to maintain accuracy under varying signal-to-noise ratios (SNRs). This study presents a robust noise-sensitive ASR error correction framework that combines multiple hypotheses and noise-aware modeling. Using noisy Persian speech, we generate 5-best hypotheses from a modified Whisper-large decoder. Error Level Noise (ELN) is introduced as a representation that captures semantic- and token-level disagreement across hypotheses, quantifying the linguistic distortions caused by noise. ELN thus provides a direct measure of noise-induced uncertainty, enabling the LLM to reason about the reliability of each hypothesis during correction. Three models are evaluated: (1) a base LLaMA-2-7B model without fine-tuning, (2) a fine-tuned variant trained on text-only hypotheses, and (3) a noise-conditioned model integrating ELN embeddings at both sentence and word levels. Experimental results demonstrate that the ELN-conditioned model achieves substantial reductions in Word Error Rate (WER). Specifically, on the challenging Mixed Noise test set, the proposed Fine-tuned + ELN (Ours) model reduces the WER from a baseline of 31.10\% (Raw Whisper) to 24.84\%, significantly surpassing the Fine-tuned (No ELN) text-only baseline of 30.79\%, whereas the original LLaMA-2-7B model increased the WER to 64.58\%, demonstrating that it is unable to correct Persian errors on its own. This confirms the effectiveness of combining multiple hypotheses with noise-aware embeddings for robust Persian ASR in noisy real-world scenarios.


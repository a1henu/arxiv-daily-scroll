---
layout: default
title: Universal Robust Speech Adaptation for Cross-Domain Speech Recognition and Enhancement
---

# Universal Robust Speech Adaptation for Cross-Domain Speech Recognition and Enhancement
**arXiv**：[2602.04307v1](https://arxiv.org/abs/2602.04307) · [PDF](https://arxiv.org/pdf/2602.04307.pdf)  
**作者**：Chien-Chun Wang, Hung-Shin Lee, Hsin-Min Wang, Berlin Chen  

**一句话要点**：提出URSA-GAN统一生成框架，以缓解跨域语音识别和增强中的噪声与信道失配问题。

**关键词**：语音识别, 语音增强, 生成对抗网络, 域适应, 噪声鲁棒性, 信道失真

## 3 点简述
- 预训练ASR和SE模型在域偏移下性能下降，尤其在未见噪声和信道失真时。
- URSA-GAN采用双嵌入架构和GAN生成器，合成目标域对齐语音并保留音素内容。
- 实验显示URSA-GAN在ASR和SE任务中显著提升性能，验证其跨域泛化能力。

## 摘要（原文）

> Pre-trained models for automatic speech recognition (ASR) and speech enhancement (SE) have exhibited remarkable capabilities under matched noise and channel conditions. However, these models often suffer from severe performance degradation when confronted with domain shifts, particularly in the presence of unseen noise and channel distortions. In view of this, we in this paper present URSA-GAN, a unified and domain-aware generative framework specifically designed to mitigate mismatches in both noise and channel conditions. URSA-GAN leverages a dual-embedding architecture that consists of a noise encoder and a channel encoder, each pre-trained with limited in-domain data to capture domain-relevant representations. These embeddings condition a GAN-based speech generator, facilitating the synthesis of speech that is acoustically aligned with the target domain while preserving phonetic content. To enhance generalization further, we propose dynamic stochastic perturbation, a novel regularization technique that introduces controlled variability into the embeddings during generation, promoting robustness to unseen domains. Empirical results demonstrate that URSA-GAN effectively reduces character error rates in ASR and improves perceptual metrics in SE across diverse noisy and mismatched channel scenarios. Notably, evaluations on compound test conditions with both channel and noise degradations confirm the generalization ability of URSA-GAN, yielding relative improvements of 16.16% in ASR performance and 15.58% in SE metrics.


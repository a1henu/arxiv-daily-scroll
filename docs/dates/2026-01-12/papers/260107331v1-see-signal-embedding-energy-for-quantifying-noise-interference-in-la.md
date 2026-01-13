---
layout: default
title: SEE: Signal Embedding Energy for Quantifying Noise Interference in Large Audio Language Models
---

# SEE: Signal Embedding Energy for Quantifying Noise Interference in Large Audio Language Models
**arXiv**：[2601.07331v1](https://arxiv.org/abs/2601.07331) · [PDF](https://arxiv.org/pdf/2601.07331.pdf)  
**作者**：Yuanhe Zhang, Jiayu Tian, Yibo Zhang, Shilinlu Yan, Liang Lin, Zhenhong Zhou, Li Sun, Sen Su  

**一句话要点**：提出信号嵌入能量（SEE）以量化大型音频语言模型中的噪声干扰

**关键词**：大型音频语言模型, 噪声量化, 信号嵌入能量, 模型鲁棒性, 去噪策略

## 3 点简述
- 核心问题：现有研究缺乏对噪声影响的定量分析，依赖直觉和经验观察。
- 方法要点：基于模型内部表示的结构化激活子空间，引入SEE量化噪声强度影响。
- 实验或效果：SEE与模型性能强相关（0.98），传统去噪方法效果有限甚至有害。

## 摘要（原文）

> Large Audio Language Models (LALMs) have been widely applied in real-time scenarios, such as in-car assistants and online meeting comprehension. In practice, audio inputs are often corrupted by device and environmental noise, leading to performance degradation. However, existing LALM studies on noise lack quantitative analysis and rely mainly on intuition and empirical observation, thus failing to understand practical robustness. To address this issue, we introduce Signal Embedding Energy (SEE), a method for quantifying the impact of noise intensity on LALM inputs, enabling the differentiation of LALM robustness in real-world deployments. SEE introduces a perspective based on structured activation subspaces derived from the model's internal representations, which more accurately captures its perception of noise than raw audio features. Across experiments, SEE exhibits a strong correlation with LALM performance, achieving a correlation of 0.98. Surprisingly, traditional audio denoising methods are only marginally effective for LALMs, and, in some cases, even increase SEE and impair performance. This suggests a mismatch between speech-centric denoising objectives and the noise sensitivity of modern LALMs. Therefore, we propose a mitigation strategy derived from SEE to denoise LALM inputs, outperforming existing denoising methods. This paper introduces a novel metric for noise quantification in LALMs, providing guidance for robustness improvements in real-world deployments.


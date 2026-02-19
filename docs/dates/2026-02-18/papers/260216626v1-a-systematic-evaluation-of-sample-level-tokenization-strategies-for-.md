---
layout: default
title: A Systematic Evaluation of Sample-Level Tokenization Strategies for MEG Foundation Models
---

# A Systematic Evaluation of Sample-Level Tokenization Strategies for MEG Foundation Models
**arXiv**：[2602.16626v1](https://arxiv.org/abs/2602.16626) · [PDF](https://arxiv.org/pdf/2602.16626.pdf)  
**作者**：SungJun Cho, Chetan Gohil, Rukuang Huang, Oiwi Parker Jones, Mark W. Woolrich  

**一句话要点**：系统评估MEG基础模型的样本级标记化策略，比较可学习与不可学习方法。

**关键词**：神经影像基础模型, 标记化策略, MEG数据处理, 自编码器, 变压器模型, 下游任务评估

## 3 点简述
- 核心问题：神经影像数据标记化策略对基础模型性能的影响尚不明确。
- 方法要点：引入基于自编码器的可学习标记器，并与不可学习方法对比。
- 实验或效果：在多个MEG数据集上评估重建精度、模型性能与下游任务表现。

## 摘要（原文）

> Recent success in natural language processing has motivated growing interest in large-scale foundation models for neuroimaging data. Such models often require discretization of continuous neural time series data, a process referred to as 'tokenization'. However, the impact of different tokenization strategies for neural data is currently poorly understood. In this work, we present a systematic evaluation of sample-level tokenization strategies for transformer-based large neuroimaging models (LNMs) applied to magnetoencephalography (MEG) data. We compare learnable and non-learnable tokenizers by examining their signal reconstruction fidelity and their impact on subsequent foundation modeling performance (token prediction, biological plausibility of generated data, preservation of subject-specific information, and performance on downstream tasks). For the learnable tokenizer, we introduce a novel approach based on an autoencoder. Experiments were conducted on three publicly available MEG datasets spanning different acquisition sites, scanners, and experimental paradigms. Our results show that both learnable and non-learnable discretization schemes achieve high reconstruction accuracy and broadly comparable performance across most evaluation criteria, suggesting that simple fixed sample-level tokenization strategies can be used in the development of neural foundation models. The code is available at https://github.com/OHBA-analysis/Cho2026_Tokenizer.


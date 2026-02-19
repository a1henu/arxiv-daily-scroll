---
layout: default
title: ASPEN: Spectral-Temporal Fusion for Cross-Subject Brain Decoding
---

# ASPEN: Spectral-Temporal Fusion for Cross-Subject Brain Decoding
**arXiv**：[2602.16147v1](https://arxiv.org/abs/2602.16147) · [PDF](https://arxiv.org/pdf/2602.16147.pdf)  
**作者**：Megan Lee, Seung Ha Hwang, Inhyeok Choi, Shreyas Darade, Mengchun Zhang, Kateryna Shapovalenko  

**一句话要点**：提出ASPEN架构，通过谱-时特征融合解决跨被试脑电解码中的个体差异问题。

**关键词**：脑电解码, 跨被试泛化, 谱-时融合, 乘法融合, 脑机接口

## 3 点简述
- 核心问题：脑电信号个体差异大，跨被试泛化困难。
- 方法要点：基于谱特征更稳定，设计谱-时流乘法融合，要求跨模态一致。
- 实验或效果：在六个基准数据集上，ASPEN动态优化谱-时平衡，取得最佳或竞争性跨被试准确率。

## 摘要（原文）

> Cross-subject generalization in EEG-based brain-computer interfaces (BCIs) remains challenging due to individual variability in neural signals. We investigate whether spectral representations offer more stable features for cross-subject transfer than temporal waveforms. Through correlation analyses across three EEG paradigms (SSVEP, P300, and Motor Imagery), we find that spectral features exhibit consistently higher cross-subject similarity than temporal signals. Motivated by this observation, we introduce ASPEN, a hybrid architecture that combines spectral and temporal feature streams via multiplicative fusion, requiring cross-modal agreement for features to propagate. Experiments across six benchmark datasets reveal that ASPEN is able to dynamically achieve the optimal spectral-temporal balance depending on the paradigm. ASPEN achieves the best unseen-subject accuracy on three of six datasets and competitive performance on others, demonstrating that multiplicative multimodal fusion enables effective cross-subject generalization.


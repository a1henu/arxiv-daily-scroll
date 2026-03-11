---
layout: default
title: BrainSTR: Spatio-Temporal Contrastive Learning for Interpretable Dynamic Brain Network Modeling
---

# BrainSTR: Spatio-Temporal Contrastive Learning for Interpretable Dynamic Brain Network Modeling
**arXiv**：[2603.09825v1](https://arxiv.org/abs/2603.09825) · [PDF](https://arxiv.org/pdf/2603.09825.pdf)  
**作者**：Guiliang Guo, Guangqi Wen, Lingwen Liu, Ruoxian Song, Peng Cao, Jinzhu Yang, Fei Wang, Xiaoli Liu, Osmar R. Zaiane  

**一句话要点**：提出BrainSTR框架，通过时空对比学习解决动态脑网络建模中诊断信号稀疏和噪声干扰的挑战。

**关键词**：动态脑网络建模, 时空对比学习, 自适应相位划分, 增量图结构生成, 神经精神疾病诊断, 可解释性分析

## 3 点简述
- 核心问题：动态功能连接中诊断信号稀疏且受噪声干扰，影响时空可解释性。
- 方法要点：自适应相位划分、注意力机制和增量图结构生成器，结合时空监督对比学习。
- 实验或效果：在ASD、BD和MDD数据集上验证有效性，发现的关键相位和子网络与神经影像发现一致。

## 摘要（原文）

> Dynamic functional connectivity captures time-varying brain states for better neuropsychiatric diagnosis and spatio-temporal interpretability, i.e., identifying when discriminative disease signatures emerge and where they reside in the connectivity topology. Reliable interpretability faces major challenges: diagnostic signals are often subtle and sparsely distributed across both time and topology, while nuisance fluctuations and non-diagnostic connectivities are pervasive. To address these issues, we propose BrainSTR, a spatio-temporal contrastive learning framework for interpretable dynamic brain network modeling. BrainSTR learns state-consistent phase boundaries via a data-driven Adaptive Phase Partition module, identifies diagnostically critical phases with attention, and extracts disease-related connectivity within each phase using an Incremental Graph Structure Generator regularized by binarization, temporal smoothness, and sparsity. Then, we introduce a spatio-temporal supervised contrastive learning approach that leverages diagnosis-relevant spatio-temporal patterns to refine the similarity metric between samples and capture more discriminative spatio-temporal features, thereby constructing a well-structured semantic space for coherent and interpretable representations. Experiments on ASD, BD, and MDD validate the effectiveness of BrainSTR, and the discovered critical phases and subnetworks provide interpretable evidence consistent with prior neuroimaging findings. Our code: https://anonymous.4open.science/r/BrainSTR1.


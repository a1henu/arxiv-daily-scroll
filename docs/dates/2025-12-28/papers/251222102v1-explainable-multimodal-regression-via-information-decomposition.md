---
layout: default
title: Explainable Multimodal Regression via Information Decomposition
---

# Explainable Multimodal Regression via Information Decomposition
**arXiv**：[2512.22102v1](https://arxiv.org/abs/2512.22102) · [PDF](https://arxiv.org/pdf/2512.22102.pdf)  
**作者**：Zhaozhao Ma, Shujian Yu  

**一句话要点**：提出基于部分信息分解的多模态回归框架，以提升预测准确性和可解释性。

**关键词**：多模态回归, 部分信息分解, 可解释性, 模态融合, 脑年龄预测

## 3 点简述
- 现有方法缺乏量化模态贡献的工具，限制多模态融合的可解释性。
- 利用部分信息分解将模态表示分解为独特、冗余和协同成分，并引入高斯性假设实现解析计算。
- 在六个真实数据集上验证，包括脑年龄预测案例，显示在准确性和可解释性上优于现有方法。

## 摘要（原文）

> Multimodal regression aims to predict a continuous target from heterogeneous input sources and typically relies on fusion strategies such as early or late fusion. However, existing methods lack principled tools to disentangle and quantify the individual contributions of each modality and their interactions, limiting the interpretability of multimodal fusion. We propose a novel multimodal regression framework grounded in Partial Information Decomposition (PID), which decomposes modality-specific representations into unique, redundant, and synergistic components. The basic PID framework is inherently underdetermined. To resolve this, we introduce inductive bias by enforcing Gaussianity in the joint distribution of latent representations and the transformed response variable (after inverse normal transformation), thereby enabling analytical computation of the PID terms. Additionally, we derive a closed-form conditional independence regularizer to promote the isolation of unique information within each modality. Experiments on six real-world datasets, including a case study on large-scale brain age prediction from multimodal neuroimaging data, demonstrate that our framework outperforms state-of-the-art methods in both predictive accuracy and interpretability, while also enabling informed modality selection for efficient inference. Implementation is available at https://github.com/zhaozhaoma/PIDReg.


---
layout: default
title: Sparse Bayesian Deep Functional Learning with Structured Region Selection
---

# Sparse Bayesian Deep Functional Learning with Structured Region Selection
**arXiv**：[2602.20651v1](https://arxiv.org/abs/2602.20651) · [PDF](https://arxiv.org/pdf/2602.20651.pdf)  
**作者**：Xiaoxian Zhu, Yingmeng Li, Shuangge Ma, Mengyun Wu  

**一句话要点**：提出稀疏贝叶斯功能深度神经网络以解决功能数据分析中非线性建模与可解释区域选择的权衡问题。

**关键词**：功能数据分析, 稀疏贝叶斯学习, 深度神经网络, 区域选择, 可解释性, 非线性建模

## 3 点简述
- 核心问题：现有功能模型线性受限，深度学习方法缺乏可解释的稀疏效应区域选择。
- 方法要点：结合深度贝叶斯架构学习自适应功能嵌入，利用结构化先验实现可解释的区域选择。
- 实验或效果：理论保证近似误差界和后验一致性，实证显示在预测准确性和区域识别上优于现有方法。

## 摘要（原文）

> In modern applications such as ECG monitoring, neuroimaging, wearable sensing, and industrial equipment diagnostics, complex and continuously structured data are ubiquitous, presenting both challenges and opportunities for functional data analysis. However, existing methods face a critical trade-off: conventional functional models are limited by linearity, whereas deep learning approaches lack interpretable region selection for sparse effects. To bridge these gaps, we propose a sparse Bayesian functional deep neural network (sBayFDNN). It learns adaptive functional embeddings through a deep Bayesian architecture to capture complex nonlinear relationships, while a structured prior enables interpretable, region-wise selection of influential domains with quantified uncertainty. Theoretically, we establish rigorous approximation error bounds, posterior consistency, and region selection consistency. These results provide the first theoretical guarantees for a Bayesian deep functional model, ensuring its reliability and statistical rigor. Empirically, comprehensive simulations and real-world studies confirm the effectiveness and superiority of sBayFDNN. Crucially, sBayFDNN excels in recognizing intricate dependencies for accurate predictions and more precisely identifies functionally meaningful regions, capabilities fundamentally beyond existing approaches.


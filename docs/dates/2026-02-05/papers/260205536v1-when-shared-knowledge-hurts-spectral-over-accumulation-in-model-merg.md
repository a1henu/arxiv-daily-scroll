---
layout: default
title: When Shared Knowledge Hurts: Spectral Over-Accumulation in Model Merging
---

# When Shared Knowledge Hurts: Spectral Over-Accumulation in Model Merging
**arXiv**：[2602.05536v1](https://arxiv.org/abs/2602.05536) · [PDF](https://arxiv.org/pdf/2602.05536.pdf)  
**作者**：Yayuan Li, Ze Peng, Jian Zhang, Jintao Guo, Yue Duan, Yinghuan Shi  

**一句话要点**：提出奇异值校准以解决模型合并中的谱过累积问题

**关键词**：模型合并, 谱分析, 奇异值校准, 任务算术, 后处理优化, 共享知识

## 3 点简述
- 核心问题：任务共享谱方向时，线性合并导致奇异值膨胀和偏向共享子空间。
- 方法要点：提出无训练、无数据的后处理方法，量化子空间重叠并重标定奇异值。
- 实验或效果：在视觉和语言基准上提升基线，Task Arithmetic性能提升13.0%。

## 摘要（原文）

> Model merging combines multiple fine-tuned models into a single model by adding their weight updates, providing a lightweight alternative to retraining. Existing methods primarily target resolving conflicts between task updates, leaving the failure mode of over-counting shared knowledge unaddressed. We show that when tasks share aligned spectral directions (i.e., overlapping singular vectors), a simple linear combination repeatedly accumulates these directions, inflating the singular values and biasing the merged model toward shared subspaces. To mitigate this issue, we propose Singular Value Calibration (SVC), a training-free and data-free post-processing method that quantifies subspace overlap and rescales inflated singular values to restore a balanced spectrum. Across vision and language benchmarks, SVC consistently improves strong merging baselines and achieves state-of-the-art performance. Furthermore, by modifying only the singular values, SVC improves the performance of Task Arithmetic by 13.0%. Code is available at: https://github.com/lyymuwu/SVC.


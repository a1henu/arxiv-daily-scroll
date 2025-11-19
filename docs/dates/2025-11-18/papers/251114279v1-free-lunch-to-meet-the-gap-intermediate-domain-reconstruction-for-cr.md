---
layout: default
title: Free Lunch to Meet the Gap: Intermediate Domain Reconstruction for Cross-Domain Few-Shot Learning
---

# Free Lunch to Meet the Gap: Intermediate Domain Reconstruction for Cross-Domain Few-Shot Learning
**arXiv**：[2511.14279v1](https://arxiv.org/abs/2511.14279) · [PDF](https://arxiv.org/pdf/2511.14279.pdf)  
**作者**：Tong Zhang, Yifan Zhao, Liangyu Wang, Jia Li  

**一句话要点**：提出中间域代理重建方法以解决跨域少样本学习中的域差异问题

**关键词**：跨域少样本学习, 中间域重建, 特征变换, 域对齐, 少样本分类

## 3 点简述
- 核心问题：跨域少样本学习面临语义不匹配、大域差异和数据稀缺挑战
- 方法要点：利用源域特征嵌入构建中间域代理，重建目标域特征
- 实验或效果：在8个基准测试中超越现有最优模型，实现快速域对齐

## 摘要（原文）

> Cross-Domain Few-Shot Learning (CDFSL) endeavors to transfer generalized knowledge from the source domain to target domains using only a minimal amount of training data, which faces a triplet of learning challenges in the meantime, i.e., semantic disjoint, large domain discrepancy, and data scarcity. Different from predominant CDFSL works focused on generalized representations, we make novel attempts to construct Intermediate Domain Proxies (IDP) with source feature embeddings as the codebook and reconstruct the target domain feature with this learned codebook. We then conduct an empirical study to explore the intrinsic attributes from perspectives of visual styles and semantic contents in intermediate domain proxies. Reaping benefits from these attributes of intermediate domains, we develop a fast domain alignment method to use these proxies as learning guidance for target domain feature transformation. With the collaborative learning of intermediate domain reconstruction and target feature transformation, our proposed model is able to surpass the state-of-the-art models by a margin on 8 cross-domain few-shot learning benchmarks.


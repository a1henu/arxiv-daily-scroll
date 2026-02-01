---
layout: default
title: Representation Unlearning: Forgetting through Information Compression
---

# Representation Unlearning: Forgetting through Information Compression
**arXiv**：[2601.21564v1](https://arxiv.org/abs/2601.21564) · [PDF](https://arxiv.org/pdf/2601.21564.pdf)  
**作者**：Antonio Almudévar, Alfonso Ortega  

**一句话要点**：提出表示遗忘框架，通过信息压缩在表示空间直接移除特定数据影响

**关键词**：机器遗忘, 表示学习, 信息瓶颈, 变分方法, 零样本遗忘

## 3 点简述
- 核心问题：现有机器遗忘方法修改参数不稳定、计算成本高且受局部近似限制
- 方法要点：在表示空间学习变换，通过信息瓶颈最大化保留数据互信息并抑制遗忘数据信息
- 实验或效果：在多个基准测试中实现更可靠遗忘、更好效用保持和更高计算效率

## 摘要（原文）

> Machine unlearning seeks to remove the influence of specific training data from a model, a need driven by privacy regulations and robustness concerns. Existing approaches typically modify model parameters, but such updates can be unstable, computationally costly, and limited by local approximations. We introduce Representation Unlearning, a framework that performs unlearning directly in the model's representation space. Instead of modifying model parameters, we learn a transformation over representations that imposes an information bottleneck: maximizing mutual information with retained data while suppressing information about data to be forgotten. We derive variational surrogates that make this objective tractable and show how they can be instantiated in two practical regimes: when both retain and forget data are available, and in a zero-shot setting where only forget data can be accessed. Experiments across several benchmarks demonstrate that Representation Unlearning achieves more reliable forgetting, better utility retention, and greater computational efficiency than parameter-centric baselines.


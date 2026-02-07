---
layout: default
title: Transport and Merge: Cross-Architecture Merging for Large Language Models
---

# Transport and Merge: Cross-Architecture Merging for Large Language Models
**arXiv**：[2602.05495v1](https://arxiv.org/abs/2602.05495) · [PDF](https://arxiv.org/pdf/2602.05495.pdf)  
**作者**：Chenhang Cui, Binyun Yang, Fei Shen, Yuxin Chen, Jingnan Zheng, Xiang Wang, An Zhang, Tat-Seng Chua  

**一句话要点**：提出基于最优传输的跨架构合并框架，以解决大语言模型向异构小模型的知识迁移问题。

**关键词**：模型合并, 最优传输, 知识迁移, 异构架构, 低资源语言

## 3 点简述
- 核心问题：现有模型合并方法假设架构兼容，无法直接处理异构模型间的知识迁移。
- 方法要点：利用最优传输对齐激活，推断跨神经元对应关系，指导权重空间融合。
- 实验或效果：在低资源语言和专门领域实验中，目标模型性能得到一致提升。

## 摘要（原文）

> Large language models (LLMs) achieve strong capabilities by scaling model capacity and training data, yet many real-world deployments rely on smaller models trained or adapted from low-resource data. This gap motivates the need for mechanisms to transfer knowledge from large, high-resource models to smaller, low-resource targets. While model merging provides an effective transfer mechanism, most existing approaches assume architecture-compatible models and therefore cannot directly transfer knowledge from large high-resource LLMs to heterogeneous low-resource targets. In this work, we propose a cross-architecture merging framework based on optimal transport (OT) that aligns activations to infer cross-neuron correspondences between heterogeneous models. The resulting transport plans are then used to guide direct weight-space fusion, enabling effective high-resource to low-resource transfer using only a small set of inputs. Extensive experiments across low-resource languages and specialized domains demonstrate consistent improvements over target models.


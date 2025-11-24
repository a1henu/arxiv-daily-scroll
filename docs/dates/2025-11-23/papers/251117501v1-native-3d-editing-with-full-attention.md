---
layout: default
title: Native 3D Editing with Full Attention
---

# Native 3D Editing with Full Attention
**arXiv**：[2511.17501v1](https://arxiv.org/abs/2511.17501) · [PDF](https://arxiv.org/pdf/2511.17501.pdf)  
**作者**：Weiwei Cai, Shuangkang Fang, Weicai Ye, Xin Dong, Yunhan Yang, Xuanyang Zhang, Wei Cheng, Yanpei Cao, Gang Yu, Tao Chen  

**一句话要点**：提出原生3D编辑框架以解决现有方法速度慢和几何不一致问题

**关键词**：3D编辑, 指令引导, 多模态数据集, 令牌拼接, 几何一致性

## 3 点简述
- 现有3D编辑方法优化慢或2D提升导致几何不一致和质量下降
- 构建大规模多模态数据集，探索交叉注意力和3D令牌拼接策略
- 实验显示令牌拼接更高效，在质量、一致性和指令忠实度上领先

## 摘要（原文）

> Instruction-guided 3D editing is a rapidly emerging field with the potential to broaden access to 3D content creation. However, existing methods face critical limitations: optimization-based approaches are prohibitively slow, while feed-forward approaches relying on multi-view 2D editing often suffer from inconsistent geometry and degraded visual quality. To address these issues, we propose a novel native 3D editing framework that directly manipulates 3D representations in a single, efficient feed-forward pass. Specifically, we create a large-scale, multi-modal dataset for instruction-guided 3D editing, covering diverse addition, deletion, and modification tasks. This dataset is meticulously curated to ensure that edited objects faithfully adhere to the instructional changes while preserving the consistency of unedited regions with the source object. Building upon this dataset, we explore two distinct conditioning strategies for our model: a conventional cross-attention mechanism and a novel 3D token concatenation approach. Our results demonstrate that token concatenation is more parameter-efficient and achieves superior performance. Extensive evaluations show that our method outperforms existing 2D-lifting approaches, setting a new benchmark in generation quality, 3D consistency, and instruction fidelity.


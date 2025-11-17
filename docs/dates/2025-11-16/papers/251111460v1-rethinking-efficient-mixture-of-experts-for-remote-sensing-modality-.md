---
layout: default
title: Rethinking Efficient Mixture-of-Experts for Remote Sensing Modality-Missing Classification
---

# Rethinking Efficient Mixture-of-Experts for Remote Sensing Modality-Missing Classification
**arXiv**：[2511.11460v1](https://arxiv.org/abs/2511.11460) · [PDF](https://arxiv.org/pdf/2511.11460.pdf)  
**作者**：Qinghao Gao, Jianhai Qu, Yunsong Li, Weiqiang Dong  

**一句话要点**：提出缺失感知混合LoRA框架以解决遥感多模态分类中的模态缺失问题

**关键词**：遥感多模态分类, 模态缺失处理, 混合专家模型, 参数高效适应, 双路由机制

## 3 点简述
- 核心问题：遥感多模态分类因环境干扰或传感器故障导致模态缺失，性能下降。
- 方法要点：引入双路由机制，动态激活专家处理缺失模式，静态共享跨模态知识。
- 实验或效果：在多个基准测试中展现强鲁棒性和泛化性，计算开销低。

## 摘要（原文）

> Multimodal classification in remote sensing often suffers from missing modalities caused by environmental interference, sensor failures, or atmospheric effects, which severely degrade classification performance. Existing two-stage adaptation methods are computationally expensive and assume complete multimodal data during training, limiting their generalization to real-world incompleteness. To overcome these issues, we propose a Missing-aware Mixture-of-Loras (MaMOL) framework that reformulates modality missing as a multi-task learning problem. MaMOL introduces a dual-routing mechanism: a task-oriented dynamic router that adaptively activates experts for different missing patterns, and a modality-specific-shared static router that maintains stable cross-modal knowledge sharing. Unlike prior methods that train separate networks for each missing configuration, MaMOL achieves parameter-efficient adaptation via lightweight expert updates and shared expert reuse. Experiments on multiple remote sensing benchmarks demonstrate superior robustness and generalization under varying missing rates, with minimal computational overhead. Moreover, transfer experiments on natural image datasets validate its scalability and cross-domain applicability, highlighting MaMOL as a general and efficient solution for incomplete multimodal learning.


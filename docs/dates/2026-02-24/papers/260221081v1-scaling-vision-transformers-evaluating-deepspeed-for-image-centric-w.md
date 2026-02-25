---
layout: default
title: Scaling Vision Transformers: Evaluating DeepSpeed for Image-Centric Workloads
---

# Scaling Vision Transformers: Evaluating DeepSpeed for Image-Centric Workloads
**arXiv**：[2602.21081v1](https://arxiv.org/abs/2602.21081) · [PDF](https://arxiv.org/pdf/2602.21081.pdf)  
**作者**：Huy Trinh, Rebecca Ma, Zeqi Yu, Tahsin Reza  

**一句话要点**：评估DeepSpeed以提升Vision Transformers在图像任务中的可扩展性

**关键词**：Vision Transformers, 分布式训练, DeepSpeed, 可扩展性, 图像处理

## 3 点简述
- 核心问题：Vision Transformers因计算和内存需求高，可扩展性受限。
- 方法要点：利用DeepSpeed分布式训练框架，评估数据并行对训练效率和通信开销的影响。
- 实验或效果：在CIFAR数据集上测试不同GPU配置，分析批大小等参数对性能的影响。

## 摘要（原文）

> Vision Transformers (ViTs) have demonstrated remarkable potential in image processing tasks by utilizing self-attention mechanisms to capture global relationships within data. However, their scalability is hindered by significant computational and memory demands, especially for large-scale models with many parameters. This study aims to leverage DeepSpeed, a highly efficient distributed training framework that is commonly used for language models, to enhance the scalability and performance of ViTs. We evaluate intra- and inter-node training efficiency across multiple GPU configurations on various datasets like CIFAR-10 and CIFAR-100, exploring the impact of distributed data parallelism on training speed, communication overhead, and overall scalability (strong and weak scaling). By systematically varying software parameters, such as batch size and gradient accumulation, we identify key factors influencing performance of distributed training. The experiments in this study provide a foundational basis for applying DeepSpeed to image-related tasks. Future work will extend these investigations to deepen our understanding of DeepSpeed's limitations and explore strategies for optimizing distributed training pipelines for Vision Transformers.


---
layout: default
title: FlashMem: Supporting Modern DNN Workloads on Mobile with GPU Memory Hierarchy Optimizations
---

# FlashMem: Supporting Modern DNN Workloads on Mobile with GPU Memory Hierarchy Optimizations
**arXiv**：[2602.15379v1](https://arxiv.org/abs/2602.15379) · [PDF](https://arxiv.org/pdf/2602.15379.pdf)  
**作者**：Zhihao Shu, Md Musfiqur Rahman Sanim, Hangyu Zheng, Kunxiong Zhu, Miao Yin, Gagan Agrawal, Wei Niu  

**一句话要点**：提出FlashMem框架，通过内存流式调度优化移动GPU内存层次，支持大规模DNN和多DNN工作负载。

**关键词**：移动GPU优化, 内存流式调度, DNN推理加速, 多DNN工作负载, 2.5D纹理内存

## 3 点简述
- 核心问题：移动GPU内存有限，传统权重预加载策略不适用于大规模或连续多模型DNN推理。
- 方法要点：静态确定模型加载计划，动态按需流式传输权重，利用2.5D纹理内存减少数据转换。
- 实验或效果：在11个模型上实现2.0x至8.4x内存减少和1.7x至75.0x加速，提升资源受限移动GPU效率。

## 摘要（原文）

> The increasing size and complexity of modern deep neural networks (DNNs) pose significant challenges for on-device inference on mobile GPUs, with limited memory and computational resources. Existing DNN acceleration frameworks primarily deploy a weight preloading strategy, where all model parameters are loaded into memory before execution on mobile GPUs. We posit that this approach is not adequate for modern DNN workloads that comprise very large model(s) and possibly execution of several distinct models in succession. In this work, we introduce FlashMem, a memory streaming framework designed to efficiently execute large-scale modern DNNs and multi-DNN workloads while minimizing memory consumption and reducing inference latency. Instead of fully preloading weights, FlashMem statically determines model loading schedules and dynamically streams them on demand, leveraging 2.5D texture memory to minimize data transformations and improve execution efficiency. Experimental results on 11 models demonstrate that FlashMem achieves 2.0x to 8.4x memory reduction and 1.7x to 75.0x speedup compared to existing frameworks, enabling efficient execution of large-scale models and multi-DNN support on resource-constrained mobile GPUs.


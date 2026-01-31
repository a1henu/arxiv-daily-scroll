---
layout: default
title: Where Do the Joules Go? Diagnosing Inference Energy Consumption
---

# Where Do the Joules Go? Diagnosing Inference Energy Consumption
**arXiv**：[2601.22076v1](https://arxiv.org/abs/2601.22076) · [PDF](https://arxiv.org/pdf/2601.22076.pdf)  
**作者**：Jae-Won Chung, Ruofan Wu, Jeff J. Ma, Mosharaf Chowdhury  

**一句话要点**：提出诊断框架以分析生成式AI推理能耗，基于大规模测量研究揭示关键因素。

**关键词**：能耗诊断, 生成式AI, 推理优化, GPU能耗, 大规模测量, 能源效率

## 3 点简述
- 核心问题：生成式AI推理能耗差异巨大，需诊断原因以优化能源效率。
- 方法要点：通过大规模测量（46模型、7任务、1858配置）分析时间与能耗，构建基于内存和利用率的推理框架。
- 实验或效果：发现任务类型、GPU利用等导致能耗数量级差异，框架可扩展至吞吐每瓦指标。

## 摘要（原文）

> Energy is now a critical ML computing resource. While measuring energy consumption and observing trends is a valuable first step, accurately understanding and diagnosing why those differences occur is crucial for optimization. To that end, we begin by presenting a large-scale measurement study of inference time and energy across the generative AI landscape with 46 models, 7 tasks, and 1,858 different configurations on NVIDIA H100 and B200 GPUs. Our empirical findings span order-of-magnitude variations: LLM task type can lead to 25$\times$ energy differences, video generation sometimes consumes more than 100$\times$ the energy of images, and GPU utilization differences can result in 3--5$\times$ energy differences. Based on our observations, we present a framework for reasoning about the underlying mechanisms that govern time and energy consumption. The essence is that time and energy are determined by latent metrics like memory and utilization, which are in turn affected by various factors across the algorithm, software, and hardware layers. Our framework also extends directly to throughput per watt, a critical metric for power-constrained datacenters.


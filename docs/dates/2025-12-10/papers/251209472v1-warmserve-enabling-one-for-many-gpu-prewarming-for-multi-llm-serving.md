---
layout: default
title: WarmServe: Enabling One-for-Many GPU Prewarming for Multi-LLM Serving
---

# WarmServe: Enabling One-for-Many GPU Prewarming for Multi-LLM Serving
**arXiv**：[2512.09472v1](https://arxiv.org/abs/2512.09472) · [PDF](https://arxiv.org/pdf/2512.09472.pdf)  
**作者**：Chiheng Lou, Sheng Qi, Rui Kang, Yong Zhang, Chen Sun, Pengcheng Wang, Bingyang Liu, Xuanzhe Liu, Xin Jin  

**一句话要点**：提出WarmServe系统，通过通用GPU工作器实现一对多预热，以优化多LLM服务中的推理性能。

**关键词**：多LLM服务, GPU预热, 负载预测, 模型放置, 内存管理, 推理性能优化

## 3 点简述
- 核心问题：现有系统因忽视未来负载特性，导致GPU利用率优化与推理性能（如首词延迟）之间的权衡。
- 方法要点：设计通用GPU工作器，基于负载预测进行主动预热，采用驱逐感知模型放置和零开销内存切换机制。
- 实验或效果：在真实数据集上，相比现有系统，首词延迟提升最高达50.8倍，请求服务能力提升至2.5倍。

## 摘要（原文）

> Deploying multiple models within shared GPU clusters is promising for improving resource efficiency in large language model (LLM) serving. Existing multi-LLM serving systems optimize GPU utilization at the cost of worse inference performance, especially time-to-first-token (TTFT). We identify the root cause of such compromise as their unawareness of future workload characteristics. In contrast, recent analysis on real-world traces has shown the high periodicity and long-term predictability of LLM serving workloads.
>   We propose universal GPU workers to enable one-for-many GPU prewarming that loads models with knowledge of future workloads. Based on universal GPU workers, we design and build WarmServe, a multi-LLM serving system that (1) mitigates cluster-wide prewarming interference by adopting an evict-aware model placement strategy, (2) prepares universal GPU workers in advance by proactive prewarming, and (3) manages GPU memory with a zero-overhead memory switching mechanism. Evaluation under real-world datasets shows that WarmServe improves TTFT by up to 50.8$\times$ compared to the state-of-the-art autoscaling-based system, while being capable of serving up to 2.5$\times$ more requests compared to the GPU-sharing system.


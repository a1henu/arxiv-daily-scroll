---
layout: default
title: NanoVLA: Routing Decoupled Vision-Language Understanding for Nano-sized Generalist Robotic Policies
---

# NanoVLA: Routing Decoupled Vision-Language Understanding for Nano-sized Generalist Robotic Policies
**arXiv**：[2510.25122v1](https://arxiv.org/abs/2510.25122) · [PDF](https://arxiv.org/pdf/2510.25122.pdf)  
**作者**：Jiahong Chen, Jing Wang, Long Chen, Chuwei Cai, Jinghui Lu  

**一句话要点**：提出NanoVLA轻量架构以解决资源受限边缘设备上的视觉-语言-动作模型部署挑战

**关键词**：视觉-语言-动作模型, 轻量架构, 边缘计算, 推理优化, 机器人操作, 动态路由

## 3 点简述
- 核心问题：视觉-语言-动作模型在边缘设备上部署困难，计算需求高，影响实时性和资源效率。
- 方法要点：采用视觉-语言解耦、长短期动作分块和动态路由，优化推理效率和性能。
- 实验或效果：在边缘设备上实现高达52倍加速，参数减少98%，保持或超越任务精度和泛化能力。

## 摘要（原文）

> Vision-language-action (VLA) models have significantly advanced robotic
> manipulation by integrating vision-language models (VLMs), and action decoders
> into a unified architecture. However, their deployment on resource-constrained
> edge devices, such as mobile robots or embedded systems (e.g., Jetson Orin
> Nano), remains challenging due to high computational demands, especially in
> real-world scenarios where power, latency, and computational resources are
> critical. To close this gap, we introduce Nano-scale Vision-Language Action
> (NanoVLA), a family of lightweight VLA architectures that achieve high
> performance with minimal resources. Our core innovations include: (1)
> vision-language decoupling that moves conventional early vision and language
> inputs fusion in VLM to late stage, achieving better performance while enabling
> caching and reduce inference overhead and latency; (2) long-short action
> chunking to ensure smooth, coherent multi-step planning without sacrificing
> real-time responsiveness; (3) dynamic routing that adaptively assigns
> lightweight or heavy backbones based on task complexity, further optimizing
> inference efficiency. Experimental results on several benchmarks, as well as
> real-world deployments, demonstrate that NanoVLA achieves up to 52x faster
> inference on edge devices compared to previous state-of-the-art VLA models,
> with 98% less parameters while maintaining or surpassing their task accuracy
> and generalization. Ablation studies confirm that our decoupling strategy
> preserves cross-task transferability, and the routing module enhances
> cost-performance trade-offs, enabling practical, high-precision robotic
> manipulation on resource-constrained hardware.


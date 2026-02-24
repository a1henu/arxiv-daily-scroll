---
layout: default
title: A Replicate-and-Quantize Strategy for Plug-and-Play Load Balancing of Sparse Mixture-of-Experts LLMs
---

# A Replicate-and-Quantize Strategy for Plug-and-Play Load Balancing of Sparse Mixture-of-Experts LLMs
**arXiv**：[2602.19938v1](https://arxiv.org/abs/2602.19938) · [PDF](https://arxiv.org/pdf/2602.19938.pdf)  
**作者**：Zijie Liu, Jie Peng, Jinhao Duan, Zirui Liu, Kaixiong Zhou, Mingfu Liang, Luke Simon, Xi Liu, Zhaozhuo Xu, Tianlong Chen  

**一句话要点**：提出复制与量化策略以解决稀疏专家混合大模型推理时的负载不均衡问题

**关键词**：稀疏专家混合模型, 负载均衡, 推理优化, 模型量化, 动态路由

## 3 点简述
- 核心问题：稀疏专家混合模型在推理时存在严重负载不均衡，影响部署效率
- 方法要点：通过复制高负载专家和量化低负载专家，动态重平衡工作负载，无需重新训练
- 实验或效果：在代表性模型和基准测试中，负载不均衡减少达1.4倍，准确率变化在±0.6%内

## 摘要（原文）

> Sparse Mixture-of-Experts (SMoE) architectures are increasingly used to scale large language models efficiently, delivering strong accuracy under fixed compute budgets. However, SMoE models often suffer from severe load imbalance across experts, where a small subset of experts receives most tokens while others are underutilized. Prior work has focused mainly on training-time solutions such as routing regularization or auxiliary losses, leaving inference-time behavior, which is critical for deployment, less explored.
>   We present a systematic analysis of expert routing during inference and identify three findings: (i) load imbalance persists and worsens with larger batch sizes, (ii) selection frequency does not reliably reflect expert importance, and (iii) overall expert workload and importance can be estimated using a small calibration set. These insights motivate inference-time mechanisms that rebalance workloads without retraining or router modification.
>   We propose Replicate-and-Quantize (R&Q), a training-free and near-lossless framework for dynamic workload rebalancing. In each layer, heavy-hitter experts are replicated to increase parallel capacity, while less critical experts and replicas are quantized to remain within the original memory budget. We also introduce a Load-Imbalance Score (LIS) to measure routing skew by comparing heavy-hitter load to an equal allocation baseline. Experiments across representative SMoE models and benchmarks show up to 1.4x reduction in imbalance with accuracy maintained within +/-0.6%, enabling more predictable and efficient inference.


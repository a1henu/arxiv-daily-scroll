---
layout: default
title: OmniMoE: An Efficient MoE by Orchestrating Atomic Experts at Scale
---

# OmniMoE: An Efficient MoE by Orchestrating Atomic Experts at Scale
**arXiv**：[2602.05711v1](https://arxiv.org/abs/2602.05711) · [PDF](https://arxiv.org/pdf/2602.05711.pdf)  
**作者**：Jingze Shi, Zhangyang Peng, Yizhang Zhu, Yifan Wu, Guang Liu, Yuyu Luo  

**一句话要点**：提出OmniMoE框架，通过系统算法协同设计解决细粒度MoE中路由复杂性与内存访问效率的权衡问题。

**关键词**：混合专家模型, 系统算法协同设计, 细粒度路由, 原子专家, 推理加速, 参数效率

## 3 点简述
- 核心问题：现有MoE架构在专家专业化粒度与硬件执行效率间存在固有权衡，细粒度设计导致路由复杂性和内存访问挑战。
- 方法要点：引入向量级原子专家，采用笛卡尔积路由器降低路由复杂度，并通过专家中心调度优化内存访问为密集矩阵操作。
- 实验或效果：在七个基准测试中，OmniMoE以1.7B活跃参数实现50.9%零样本准确率，推理延迟相比PEER降低10.9倍至6.7毫秒。

## 摘要（原文）

> Mixture-of-Experts (MoE) architectures are evolving towards finer granularity to improve parameter efficiency. However, existing MoE designs face an inherent trade-off between the granularity of expert specialization and hardware execution efficiency. We propose OmniMoE, a system-algorithm co-designed framework that pushes expert granularity to its logical extreme. OmniMoE introduces vector-level Atomic Experts, enabling scalable routing and execution within a single MoE layer, while retaining a shared dense MLP branch for general-purpose processing. Although this atomic design maximizes capacity, it poses severe challenges for routing complexity and memory access. To address these, OmniMoE adopts a system-algorithm co-design: (i) a Cartesian Product Router that decomposes the massive index space to reduce routing complexity from O(N) to O(sqrt(N)); and (ii) Expert-Centric Scheduling that inverts the execution order to turn scattered, memory-bound lookups into efficient dense matrix operations. Validated on seven benchmarks, OmniMoE (with 1.7B active parameters) achieves 50.9% zero-shot accuracy across seven benchmarks, outperforming coarse-grained (e.g., DeepSeekMoE) and fine-grained (e.g., PEER) baselines. Crucially, OmniMoE reduces inference latency from 73ms to 6.7ms (a 10.9-fold speedup) compared to PEER, demonstrating that massive-scale fine-grained MoE can be fast and accurate. Our code is open-sourced at https://github.com/flash-algo/omni-moe.


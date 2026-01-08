---
layout: default
title: A Scheduling Framework for Efficient MoE Inference on Edge GPU-NDP Systems
---

# A Scheduling Framework for Efficient MoE Inference on Edge GPU-NDP Systems
**arXiv**：[2601.03992v1](https://arxiv.org/abs/2601.03992) · [PDF](https://arxiv.org/pdf/2601.03992.pdf)  
**作者**：Qi Wu, Chao Fang, Jiayuan Chen, Ye Lin, Yueqi Zhang, Yichuan Bai, Yuan Du, Li Du  

**一句话要点**：提出高效调度框架以解决边缘GPU-NDP系统中MoE推理的负载不均与资源利用问题

**关键词**：MoE推理, 边缘计算, GPU-NDP系统, 负载均衡, 张量并行, 预取策略

## 3 点简述
- 核心问题：MoE模型在边缘GPU-NDP系统中面临负载不均、GPU利用率低和数据预取依赖预分析等挑战
- 方法要点：利用张量并行性、负载均衡调度算法和无数据集预取策略优化推理效率
- 实验或效果：相比先进方法，平均加速2.41倍，最高达2.56倍，提升资源受限环境下的推理性能

## 摘要（原文）

> Mixture-of-Experts (MoE) models facilitate edge deployment by decoupling model capacity from active computation, yet their large memory footprint drives the need for GPU systems with near-data processing (NDP) capabilities that offload experts to dedicated processing units. However, deploying MoE models on such edge-based GPU-NDP systems faces three critical challenges: 1) severe load imbalance across NDP units due to non-uniform expert selection and expert parallelism, 2) insufficient GPU utilization during expert computation within NDP units, and 3) extensive data pre-profiling necessitated by unpredictable expert activation patterns for pre-fetching. To address these challenges, this paper proposes an efficient inference framework featuring three key optimizations. First, the underexplored tensor parallelism in MoE inference is exploited to partition and compute large expert parameters across multiple NDP units simultaneously towards edge low-batch scenarios. Second, a load-balancing-aware scheduling algorithm distributes expert computations across NDP units and GPU to maximize resource utilization. Third, a dataset-free pre-fetching strategy proactively loads frequently accessed experts to minimize activation delays. Experimental results show that our framework enables GPU-NDP systems to achieve 2.41x on average and up to 2.56x speedup in end-to-end latency compared to state-of-the-art approaches, significantly enhancing MoE inference efficiency in resource-constrained environments.


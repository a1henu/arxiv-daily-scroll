---
layout: default
title: HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference
---

# HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference
**arXiv**：[2601.13684v1](https://arxiv.org/abs/2601.13684) · [PDF](https://arxiv.org/pdf/2601.13684.pdf)  
**作者**：Zhiyuan Shi, Qibo Qiu, Feng Xue, Zhonglin Jiang, Li Yu, Jian Jiang, Xiaofei He, Wenxiao Wang  

**一句话要点**：提出HeteroCache动态检索方法以解决长上下文LLM推理中KV缓存的内存增长问题。

**关键词**：KV缓存压缩, 长上下文推理, 动态检索, 注意力机制, LLM推理优化

## 3 点简述
- 核心问题：KV缓存线性内存增长和静态压缩方法忽略注意力漂移，导致全局信息丢失。
- 方法要点：基于注意力头的时空异质性，采用细粒度权重分配和分层存储机制进行动态压缩。
- 实验或效果：在多个长上下文基准测试中达到最优性能，在224K上下文下解码加速达3倍。

## 摘要（原文）

> The linear memory growth of the KV cache poses a significant bottleneck for LLM inference in long-context tasks. Existing static compression methods often fail to preserve globally important information, principally because they overlook the attention drift phenomenon where token significance evolves dynamically. Although recent dynamic retrieval approaches attempt to address this issue, they typically suffer from coarse-grained caching strategies and incur high I/O overhead due to frequent data transfers. To overcome these limitations, we propose HeteroCache, a training-free dynamic compression framework. Our method is built on two key insights: attention heads exhibit diverse temporal heterogeneity, and there is significant spatial redundancy among heads within the same layer. Guided by these insights, HeteroCache categorizes heads based on stability and redundancy. Consequently, we apply a fine-grained weighting strategy that allocates larger cache budgets to heads with rapidly shifting attention to capture context changes, thereby addressing the inefficiency of coarse-grained strategies. Furthermore, we employ a hierarchical storage mechanism in which a subset of representative heads monitors attention shift, and trigger an asynchronous, on-demand retrieval of contexts from the CPU, effectively hiding I/O latency. Finally, experiments demonstrate that HeteroCache achieves state-of-the-art performance on multiple long-context benchmarks and accelerates decoding by up to $3\times$ compared to the original model in the 224K context. Our code will be open-source.


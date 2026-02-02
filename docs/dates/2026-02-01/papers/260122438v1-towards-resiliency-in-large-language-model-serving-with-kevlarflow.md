---
layout: default
title: Towards Resiliency in Large Language Model Serving with KevlarFlow
---

# Towards Resiliency in Large Language Model Serving with KevlarFlow
**arXiv**：[2601.22438v1](https://arxiv.org/abs/2601.22438) · [PDF](https://arxiv.org/pdf/2601.22438.pdf)  
**作者**：Shangshu Qian, Kipling Liu, P. C. Sruthi, Lin Tan, Yongle Zhang  

**一句话要点**：提出KevlarFlow以解决大规模语言模型服务中硬件故障导致的恢复缓慢问题

**关键词**：大规模语言模型服务, 容错架构, 模型并行, KV缓存, 恢复时间优化

## 3 点简述
- 核心问题：超大规模集群硬件故障频繁，导致LLM服务中断，现有恢复机制耗时长达10分钟。
- 方法要点：采用解耦模型并行初始化、动态流量重路由和后台KV缓存复制，提升故障容忍性。
- 实验或效果：评估显示MTTR降低20倍，故障下延迟和TTFT显著改善，运行时开销可忽略。

## 摘要（原文）

> Large Language Model (LLM) serving systems remain fundamentally fragile, where frequent hardware faults in hyperscale clusters trigger disproportionate service outages in the software stack. Current recovery mechanisms are prohibitively slow, often requiring up to 10 minutes to reinitialize resources and reload massive model weights. We introduce KevlarFlow, a fault tolerant serving architecture designed to bridge the gap between hardware unreliability and service availability. KevlarFlow leverages 1) decoupled model parallelism initialization, 2) dynamic traffic rerouting, and 3) background KV cache replication to maintain high throughput during partial failures. Our evaluation demonstrates that KevlarFlow reduces mean-time-to-recovery (MTTR) by 20x and, under failure conditions, improves average latency by 3.1x, 99th percentile (p99) latency by 2.8x, average time-to-first-token (TTFT) by 378.9x, and p99 TTFT by 574.6x with negligible runtime overhead in comparison to state-of-the-art LLM serving systems.


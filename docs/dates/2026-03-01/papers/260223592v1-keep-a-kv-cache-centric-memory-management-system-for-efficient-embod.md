---
layout: default
title: KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning
---

# KEEP: A KV-Cache-Centric Memory Management System for Efficient Embodied Planning
**arXiv**：[2602.23592v1](https://arxiv.org/abs/2602.23592) · [PDF](https://arxiv.org/pdf/2602.23592.pdf)  
**作者**：Zebin Yang, Tong Xie, Baotong Lu, Shaoshan Liu, Bo Yu, Meng Li  

**一句话要点**：提出KEEP系统以解决具身规划中KV缓存更新频繁导致的效率低下问题

**关键词**：具身规划, KV缓存管理, 内存系统, 大语言模型, 效率优化

## 3 点简述
- 核心问题：现有基于文本的记忆方法导致提示过长和预填充延迟高，而KV缓存重用因频繁更新效率受限
- 方法要点：采用静态-动态内存构建、多跳内存重计算和层平衡内存加载算法优化KV缓存管理
- 实验或效果：在ALFRED数据集上比文本方法提速2.68倍，比CacheBlend方法提升4.13%成功率并减少1.90倍首令牌时间

## 摘要（原文）

> Memory-augmented Large Language Models (LLMs) have demonstrated remarkable capability for complex and long-horizon embodied planning. By keeping track of past experiences and environmental states, memory enables LLMs to maintain a global view, thereby avoiding repetitive exploration. However, existing approaches often store the memory as raw text, leading to excessively long prompts and high prefill latency. While it is possible to store and reuse the KV caches, the efficiency benefits are greatly undermined due to frequent KV cache updates. In this paper, we propose KEEP, a KV-cache-centric memory management system for efficient embodied planning. KEEP features 3 key innovations: (1) a Static-Dynamic Memory Construction algorithm that reduces KV cache recomputation by mixed-granularity memory group; (2) a Multi-hop Memory Re-computation algorithm that dynamically identifies important cross-attention among different memory groups and reconstructs memory interactions iteratively; (3) a Layer-balanced Memory Loading that eliminates unbalanced KV cache loading and cross-attention computation across different layers. Extensive experimental results have demonstrated that KEEP achieves 2.68x speedup with negligible accuracy loss compared with text-based memory methods on ALFRED dataset. Compared with the KV re-computation method CacheBlend (EuroSys'25), KEEP shows 4.13% success rate improvement and 1.90x time-to-first-token (TTFT) reduction. Our code is available on https://github.com/PKU-SEC-Lab/KEEP_Embodied_Memory.


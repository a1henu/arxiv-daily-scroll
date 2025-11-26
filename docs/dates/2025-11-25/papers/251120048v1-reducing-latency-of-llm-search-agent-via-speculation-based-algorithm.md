---
layout: default
title: Reducing Latency of LLM Search Agent via Speculation-based Algorithm-System Co-Design
---

# Reducing Latency of LLM Search Agent via Speculation-based Algorithm-System Co-Design
**arXiv**：[2511.20048v1](https://arxiv.org/abs/2511.20048) · [PDF](https://arxiv.org/pdf/2511.20048.pdf)  
**作者**：Zixiao Huang, Wen Zeng, Tianyu Fu, Tengxuan Liu, Yizhou Sun, Ke Hong, Xinhao Yang, Chengchun Liu, Yan Li, Quanlu Zhang, Guohao Dai, Zhenhua Zhu, Yu Wang  

**一句话要点**：提出SPAgent框架以降低LLM搜索代理的延迟

**关键词**：LLM搜索代理, 推测算法, 系统协同设计, 延迟优化, 自适应调度

## 3 点简述
- LLM搜索代理存在高延迟问题，源于串行推理与工具执行
- 采用自适应推测机制，在安全时省略验证以减少推理开销
- 实验显示端到端加速达1.65倍，同时保持或提升准确性

## 摘要（原文）

> LLM-based search agents achieve strong performance but suffer from severe latency, as each step requires serialized LLM reasoning followed by action of tool execution. We revisit this bottleneck through the lens of speculation. While traditional predict-verify speculation paradigm can break serial execution, its benefit remains limited, as it retains the full original workload and adds extra inference overhead. We observe that early agent steps often involve simple evidence-gathering, where correct actions can often be predicted without full reasoning. Building on these observations, we present SPAgent, an algorithm-system co-design framework that expands the role of speculation in search agents to reduce latency. Algorithmically, SPAgent introduces a two-phase adaptive speculation mechanism that selectively omits verification when safe. System-wise, a two-level scheduler regulates speculative requests based on engine load to ensure speculation remains beneficial. We implement SPAgent in real-world systems. Across extensive experimental settings, SPAgent achieves up to $1.65\times$ end-to-end speedup while maintaining same or even achieving higher accuracy, enabling practical deployment of multi-step search agents.


---
layout: default
title: Theoretically Optimal Attention/FFN Ratios in Disaggregated LLM Serving
---

# Theoretically Optimal Attention/FFN Ratios in Disaggregated LLM Serving
**arXiv**：[2601.21351v1](https://arxiv.org/abs/2601.21351) · [PDF](https://arxiv.org/pdf/2601.21351.pdf)  
**作者**：Chendong Song, Meixuan Wang, Hang Zhou, Hong Liang, Yuan Lyu, Zixi Chen, Yuwei Fan, Zijie Zhou  

**一句话要点**：提出理论最优注意力/前馈网络比例以优化解耦大语言模型服务性能

**关键词**：大语言模型服务, 注意力-前馈网络解耦, 资源优化, 吞吐量分析, 概率模型

## 3 点简述
- 核心问题：解耦架构中注意力与前馈网络资源比例不当导致步级阻塞和设备空闲。
- 方法要点：基于概率工作负载模型推导闭式规则，确定最大化系统平均吞吐量的最优比例。
- 实验或效果：仿真验证理论最优比例与模拟最优匹配度在10%内，显著减少空闲时间。

## 摘要（原文）

> Attention-FFN disaggregation (AFD) is an emerging architecture for LLM decoding that separates state-heavy, KV-cache-dominated Attention computation from stateless, compute-intensive FFN computation, connected by per-step communication. While AFD enables independent scaling of memory and compute resources, its performance is highly sensitive to the Attention/FFN provisioning ratio: mis-sizing induces step-level blocking and costly device idle time. We develop a tractable analytical framework for sizing AFD bundles in an $r$A-$1$F topology, where the key difficulty is that Attention-side work is nonstationary-token context grows and requests are continuously replenished with random lengths-while FFN work is stable given the aggregated batch. Using a probabilistic workload model, we derive closed-form rules for the optimal A/F ratio that maximize average throughput per instance across the system. A trace-calibrated AFD simulator validates the theory: across workloads, the theoretical optimal A/F ratio matches the simulation-optimal within 10%, and consistently reduces idle time.


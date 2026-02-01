---
layout: default
title: The Path of Least Resistance: Guiding LLM Reasining Trajectories with Prefix Consensus
---

# The Path of Least Resistance: Guiding LLM Reasining Trajectories with Prefix Consensus
**arXiv**：[2601.21494v1](https://arxiv.org/abs/2601.21494) · [PDF](https://arxiv.org/pdf/2601.21494.pdf)  
**作者**：Ishan Jindal, Sai Prashanth Akuthota, Jayant Taneja, Sachin Dev Sharma  

**一句话要点**：提出PoLR方法，利用前缀一致性降低大语言模型推理的计算开销。

**关键词**：大语言模型推理, 前缀一致性, 计算效率优化, 自适应推理, 推理轨迹聚类, 令牌减少

## 3 点简述
- 核心问题：Self-Consistency等推理策略计算成本高，需完全扩展所有推理路径。
- 方法要点：通过聚类推理轨迹的短前缀，识别主导簇并仅扩展该簇路径，减少令牌使用和延迟。
- 实验或效果：在多个数据集上匹配或超越Self-Consistency，令牌使用减少达60%，延迟降低达50%。

## 摘要（原文）

> Large language models achieve strong reasoning performance, but inference strategies such as Self-Consistency (SC) are computationally expensive, as they fully expand all reasoning traces. We introduce PoLR (Path of Least Resistance), the first inference-time method to leverage prefix consistency for compute-efficient reasoning. PoLR clusters short prefixes of reasoning traces, identifies the dominant cluster, and expands all paths in that cluster, preserving the accuracy benefits of SC while substantially reducing token usage and latency. Our theoretical analysis, framed via mutual information and entropy, explains why early reasoning steps encode strong signals predictive of final correctness. Empirically, PoLR consistently matches or exceeds SC across GSM8K, MATH500, AIME24/25, and GPQA-DIAMOND, reducing token usage by up to 60% and wall-clock latency by up to 50%. Moreover, PoLR is fully complementary to adaptive inference methods (e.g., Adaptive Consistency, Early-Stopping SC) and can serve as a drop-in pre-filter, making SC substantially more efficient and scalable without requiring model fine-tuning.


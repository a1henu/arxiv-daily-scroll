---
layout: default
title: Search-P1: Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training
---

# Search-P1: Path-Centric Reward Shaping for Stable and Efficient Agentic RAG Training
**arXiv**：[2602.22576v1](https://arxiv.org/abs/2602.22576) · [PDF](https://arxiv.org/pdf/2602.22576.pdf)  
**作者**：Tianle Xia, Ming Xu, Lingxiang Hu, Yiding Sun, Wenwei Li, Linfang Shang, Liqun Liu, Peng Shu, Huan Yu, Jie Jiang  

**一句话要点**：提出Search-P1框架，通过路径中心奖励塑形解决智能检索增强生成训练中的稀疏奖励和低样本效率问题。

**关键词**：检索增强生成, 智能体训练, 奖励塑形, 路径中心评估, 强化学习, 问答系统

## 3 点简述
- 核心问题：基于强化学习的智能检索增强生成训练存在稀疏结果奖励和低样本效率，丢弃中间信号且失败样本无贡献。
- 方法要点：引入路径中心奖励，通过顺序无关步骤覆盖和软评分评估推理轨迹结构质量，并采用双轨路径评分结合自一致性和参考对齐视角。
- 实验或效果：在多个问答基准测试中，Search-P1相比Search-R1等基线平均准确率提升7.7点，表现显著改进。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by incorporating external knowledge, yet traditional single-round retrieval struggles with complex multi-step reasoning. Agentic RAG addresses this by enabling LLMs to dynamically decide when and what to retrieve, but current RL-based training methods suffer from sparse outcome rewards that discard intermediate signals and low sample efficiency where failed samples contribute nothing. We propose Search-P1, a framework that introduces path-centric reward shaping for agentic RAG training, comprising two key components: (1) Path-Centric Reward, which evaluates the structural quality of reasoning trajectories through order-agnostic step coverage and soft scoring that extracts learning signals even from failed samples, and (2) Dual-Track Path Scoring with offline-generated reference planners that assesses paths from both self-consistency and reference-alignment perspectives. Experiments on multiple QA benchmarks demonstrate that Search-P1 achieves significant improvements over Search-R1 and other strong baselines, with an average accuracy gain of 7.7 points.


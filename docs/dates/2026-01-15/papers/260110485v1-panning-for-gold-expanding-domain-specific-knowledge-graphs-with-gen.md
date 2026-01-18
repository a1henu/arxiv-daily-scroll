---
layout: default
title: Panning for Gold: Expanding Domain-Specific Knowledge Graphs with General Knowledge
---

# Panning for Gold: Expanding Domain-Specific Knowledge Graphs with General Knowledge
**arXiv**：[2601.10485v1](https://arxiv.org/abs/2601.10485) · [PDF](https://arxiv.org/pdf/2601.10485.pdf)  
**作者**：Runhao Zhao, Weixin Zeng, Wentao Zhang, Chong Chen, Zhengpin Li, Xiang Zhao, Lei Chen  

**一句话要点**：提出ExeFuse方法以解决领域知识图谱融合中的相关性和粒度对齐问题

**关键词**：知识图谱融合, 领域知识图谱, 通用知识图谱, 语义程序, 粒度对齐, 基准数据集

## 3 点简述
- 核心问题：领域知识图谱覆盖不足，融合通用知识时面临高歧义性和粒度不匹配挑战。
- 方法要点：采用Fact-as-Program范式，将通用事实视为语义程序，通过程序可执行性验证领域相关性。
- 实验或效果：构建两个基准数据集，包含21种评估配置，实验验证了任务重要性和模型有效性。

## 摘要（原文）

> Domain-specific knowledge graphs (DKGs) often lack coverage compared to general knowledge graphs (GKGs). To address this, we introduce Domain-specific Knowledge Graph Fusion (DKGF), a novel task that enriches DKGs by integrating relevant facts from GKGs. DKGF faces two key challenges: high ambiguity in domain relevance and misalignment in knowledge granularity across graphs. We propose ExeFuse, a simple yet effective Fact-as-Program paradigm. It treats each GKG fact as a latent semantic program, maps abstract relations to granularity-aware operators, and verifies domain relevance via program executability on the target DKG. This unified probabilistic framework jointly resolves relevance and granularity issues. We construct two benchmarks, DKGF(W-I) and DKGF(Y-I), with 21 evaluation configurations. Extensive experiments validate the task's importance and our model's effectiveness, providing the first standardized testbed for DKGF.


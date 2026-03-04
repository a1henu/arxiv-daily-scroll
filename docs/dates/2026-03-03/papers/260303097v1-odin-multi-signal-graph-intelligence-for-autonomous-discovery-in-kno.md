---
layout: default
title: Odin: Multi-Signal Graph Intelligence for Autonomous Discovery in Knowledge Graphs
---

# Odin: Multi-Signal Graph Intelligence for Autonomous Discovery in Knowledge Graphs
**arXiv**：[2603.03097v1](https://arxiv.org/abs/2603.03097) · [PDF](https://arxiv.org/pdf/2603.03097.pdf)  
**作者**：Muyukani Kizito, Elizabeth Nyambere  

**一句话要点**：提出Odin多信号图智能引擎，通过COMPASS评分实现知识图谱自主发现，解决回声室问题。

**关键词**：知识图谱, 自主发现, 多信号集成, 图神经网络, 评分机制, 生产部署

## 3 点简述
- 核心问题：知识图谱自主发现中回声室问题，即探索易陷于密集局部社区。
- 方法要点：结合结构重要性、语义合理性、时间相关性和社区感知的多信号评分机制。
- 实验或效果：在医疗和保险等受监管生产环境中部署，提升模式发现质量和分析效率。

## 摘要（原文）

> We present Odin, the first production-deployed graph intelligence engine for autonomous discovery of meaningful patterns in knowledge graphs without prior specification. Unlike retrieval-based systems that answer predefined queries, Odin guides exploration through the COMPASS (Composite Oriented Multi-signal Path Assessment) score, a novel metric that combines (1) structural importance via Personalized PageRank, (2) semantic plausibility through Neural Probabilistic Logic Learning (NPLL) used as a discriminative filter rather than generative model, (3) temporal relevance with configurable decay, and (4) community-aware guidance through GNN-identified bridge entities and inter-community affinity scores. This multi-signal integration, particularly the bridge scoring mechanism, addresses the "echo chamber" problem where graph exploration becomes trapped in dense local communities. We formalize the autonomous discovery problem, prove theoretical properties of our scoring function, and demonstrate that beam search with multi-signal guidance achieves $O(b \cdot h)$ complexity while maintaining high recall compared to exhaustive exploration. To our knowledge, Odin represents the first autonomous discovery system deployed in regulated production environments (healthcare and insurance), demonstrating significant improvements in pattern discovery quality and analyst efficiency. Our approach maintains complete provenance traceability -- a critical requirement for regulated industries where hallucination is unacceptable.


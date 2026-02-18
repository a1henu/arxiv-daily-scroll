---
layout: default
title: FAST-EQA: Efficient Embodied Question Answering with Global and Local Region Relevancy
---

# FAST-EQA: Efficient Embodied Question Answering with Global and Local Region Relevancy
**arXiv**：[2602.15813v1](https://arxiv.org/abs/2602.15813) · [PDF](https://arxiv.org/pdf/2602.15813.pdf)  
**作者**：Haochen Zhang, Nirav Savaliya, Faizan Siddiqui, Enna Sachdeva  

**一句话要点**：提出FAST-EQA框架，通过全局与局部区域相关性高效解决具身问答中的搜索与推理问题

**关键词**：具身问答, 视觉目标识别, 链式思维推理, 全局区域导航, 有界场景记忆, 高效探索策略

## 3 点简述
- 核心问题：具身问答需在部分可观测下结合视觉理解、探索与时空推理，面临搜索空间大和推理速度慢的挑战
- 方法要点：采用问题条件化框架，包括目标识别、全局区域评分导航和基于视觉记忆的链式思维推理
- 实验或效果：在HMEQA和EXPRESS-Bench上达到最优性能，在OpenEQA和MT-HM3D上表现竞争性，且推理速度显著提升

## 摘要（原文）

> Embodied Question Answering (EQA) combines visual scene understanding, goal-directed exploration, spatial and temporal reasoning under partial observability. A central challenge is to confine physical search to question-relevant subspaces while maintaining a compact, actionable memory of observations. Furthermore, for real-world deployment, fast inference time during exploration is crucial. We introduce FAST-EQA, a question-conditioned framework that (i) identifies likely visual targets, (ii) scores global regions of interest to guide navigation, and (iii) employs Chain-of-Thought (CoT) reasoning over visual memory to answer confidently. FAST-EQA maintains a bounded scene memory that stores a fixed-capacity set of region-target hypotheses and updates them online, enabling robust handling of both single and multi-target questions without unbounded growth. To expand coverage efficiently, a global exploration policy treats narrow openings and doors as high-value frontiers, complementing local target seeking with minimal computation. Together, these components focus the agent's attention, improve scene coverage, and improve answer reliability while running substantially faster than prior approaches. On HMEQA and EXPRESS-Bench, FAST-EQA achieves state-of-the-art performance, while performing competitively on OpenEQA and MT-HM3D.


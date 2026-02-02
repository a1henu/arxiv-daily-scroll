---
layout: default
title: ScholarPeer: A Context-Aware Multi-Agent Framework for Automated Peer Review
---

# ScholarPeer: A Context-Aware Multi-Agent Framework for Automated Peer Review
**arXiv**：[2601.22638v1](https://arxiv.org/abs/2601.22638) · [PDF](https://arxiv.org/pdf/2601.22638.pdf)  
**作者**：Palash Goyal, Mihir Parmar, Yiwen Song, Hamid Palangi, Tomas Pfister, Jinsung Yoon  

**一句话要点**：提出ScholarPeer框架，通过多智能体与上下文检索解决自动同行评审中深度评估不足的问题。

**关键词**：自动同行评审, 多智能体框架, 上下文检索, 文献验证, 深度评估

## 3 点简述
- 核心问题：现有自动同行评审系统缺乏外部上下文，难以评估论文新颖性和方法缺陷。
- 方法要点：采用多智能体框架，包括历史学家、基线侦察和问答引擎，动态获取并验证文献上下文。
- 实验或效果：在DeepReview-13K数据集上评估，相比现有方法显著提升胜率，接近人类评审多样性。

## 摘要（原文）

> Automated peer review has evolved from simple text classification to structured feedback generation. However, current state-of-the-art systems still struggle with "surface-level" critiques: they excel at summarizing content but often fail to accurately assess novelty and significance or identify deep methodological flaws because they evaluate papers in a vacuum, lacking the external context a human expert possesses. In this paper, we introduce ScholarPeer, a search-enabled multi-agent framework designed to emulate the cognitive processes of a senior researcher. ScholarPeer employs a dual-stream process of context acquisition and active verification. It dynamically constructs a domain narrative using a historian agent, identifies missing comparisons via a baseline scout, and verifies claims through a multi-aspect Q&A engine, grounding the critique in live web-scale literature. We evaluate ScholarPeer on DeepReview-13K and the results demonstrate that ScholarPeer achieves significant win-rates against state-of-the-art approaches in side-by-side evaluations and reduces the gap to human-level diversity.


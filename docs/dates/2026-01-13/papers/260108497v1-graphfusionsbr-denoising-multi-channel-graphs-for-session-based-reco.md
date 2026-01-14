---
layout: default
title: GraphFusionSBR: Denoising Multi-Channel Graphs for Session-Based Recommendation
---

# GraphFusionSBR: Denoising Multi-Channel Graphs for Session-Based Recommendation
**arXiv**：[2601.08497v1](https://arxiv.org/abs/2601.08497) · [PDF](https://arxiv.org/pdf/2601.08497.pdf)  
**作者**：Jia-Xin He, Hung-Hsuan Chen  

**一句话要点**：提出GraphFusionSBR模型，通过多通道图去噪解决会话推荐中的噪声和物品主导问题。

**关键词**：会话推荐, 多通道图, 图去噪, 知识图谱, 超图, 互信息最大化

## 3 点简述
- 核心问题：会话推荐存在物品交互主导和噪声会话，影响用户意图捕捉。
- 方法要点：构建知识图谱、会话超图和会话线图三通道，自适应去噪并最大化互信息辅助学习。
- 实验或效果：实验显示模型提升电商和多媒体推荐准确性，代码已开源。

## 摘要（原文）

> Session-based recommendation systems must capture implicit user intents from sessions. However, existing models suffer from issues such as item interaction dominance and noisy sessions. We propose a multi-channel recommendation model, including a knowledge graph channel, a session hypergraph channel, and a session line graph channel, to capture information from multiple sources. Our model adaptively removes redundant edges in the knowledge graph channel to reduce noise. Knowledge graph representations cooperate with hypergraph representations for prediction to alleviate item dominance. We also generate in-session attention for denoising. Finally, we maximize mutual information between the hypergraph and line graph channels as an auxiliary task. Experiments demonstrate that our method enhances the accuracy of various recommendations, including e-commerce and multimedia recommendations. We release the code on GitHub for reproducibility.\footnote{https://github.com/hohehohe0509/DSR-HK}


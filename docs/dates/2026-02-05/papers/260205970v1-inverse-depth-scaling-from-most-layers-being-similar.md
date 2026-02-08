---
layout: default
title: Inverse Depth Scaling From Most Layers Being Similar
---

# Inverse Depth Scaling From Most Layers Being Similar
**arXiv**：[2602.05970v1](https://arxiv.org/abs/2602.05970) · [PDF](https://arxiv.org/pdf/2602.05970.pdf)  
**作者**：Yizhou Liu, Sara Kangaslahti, Ziming Liu, Jeff Gore  

**一句话要点**：揭示大语言模型中深度与损失的逆比例缩放关系，源于层间功能相似性

**关键词**：大语言模型, 深度缩放, 残差网络, 损失函数, 模型效率, 架构偏差

## 3 点简述
- 核心问题：深度和宽度对大型语言模型性能的贡献差异，需详细研究深度如何影响损失。
- 方法要点：通过分析大语言模型和玩具残差网络，量化深度对损失的影响，发现损失与深度成反比。
- 实验或效果：发现功能相似层通过集成平均减少误差，而非组合学习或离散化平滑动态，导致效率低下但鲁棒性强。

## 摘要（原文）

> Neural scaling laws relate loss to model size in large language models (LLMs), yet depth and width may contribute to performance differently, requiring more detailed studies. Here, we quantify how depth affects loss via analysis of LLMs and toy residual networks. We find loss scales inversely proportional to depth in LLMs, probably due to functionally similar layers reducing error through ensemble averaging rather than compositional learning or discretizing smooth dynamics. This regime is inefficient yet robust and may arise from the architectural bias of residual networks and target functions incompatible with smooth dynamics. The findings suggest that improving LLM efficiency may require architectural innovations to encourage compositional use of depth.


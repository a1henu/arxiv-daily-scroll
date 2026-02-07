---
layout: default
title: Inverse Depth Scaling From Most Layers Being Similar
---

# Inverse Depth Scaling From Most Layers Being Similar
**arXiv**：[2602.05970v1](https://arxiv.org/abs/2602.05970) · [PDF](https://arxiv.org/pdf/2602.05970.pdf)  
**作者**：Yizhou Liu, Sara Kangaslahti, Ziming Liu, Jeff Gore  

**一句话要点**：揭示大语言模型中深度与损失的逆比例缩放关系，源于层间功能相似性

**关键词**：大语言模型, 缩放定律, 深度缩放, 残差网络, 集成平均, 架构创新

## 3 点简述
- 核心问题：深度和宽度对LLM性能的贡献差异，需量化深度如何影响损失
- 方法要点：分析LLMs和玩具残差网络，发现损失与深度成反比，归因于功能相似层的集成平均
- 实验或效果：此机制效率低但鲁棒性强，可能源于残差网络架构偏置和目标函数不兼容平滑动态

## 摘要（原文）

> Neural scaling laws relate loss to model size in large language models (LLMs), yet depth and width may contribute to performance differently, requiring more detailed studies. Here, we quantify how depth affects loss via analysis of LLMs and toy residual networks. We find loss scales inversely proportional to depth in LLMs, probably due to functionally similar layers reducing error through ensemble averaging rather than compositional learning or discretizing smooth dynamics. This regime is inefficient yet robust and may arise from the architectural bias of residual networks and target functions incompatible with smooth dynamics. The findings suggest that improving LLM efficiency may require architectural innovations to encourage compositional use of depth.


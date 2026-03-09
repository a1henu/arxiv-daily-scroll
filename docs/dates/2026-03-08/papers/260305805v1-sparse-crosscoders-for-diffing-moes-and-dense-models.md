---
layout: default
title: Sparse Crosscoders for diffing MoEs and Dense models
---

# Sparse Crosscoders for diffing MoEs and Dense models
**arXiv**：[2603.05805v1](https://arxiv.org/abs/2603.05805) · [PDF](https://arxiv.org/pdf/2603.05805.pdf)  
**作者**：Marmik Chaudhari, Nishkal Hundia, Idhant Gulati  

**一句话要点**：提出稀疏交叉编码器以比较MoE与密集模型内部表示差异

**关键词**：稀疏交叉编码器, MoE模型, 密集模型, 内部表示分析, 特征组织, 参数效率

## 3 点简述
- 核心问题：MoE模型内部表示机制不明确，与密集模型对比不足
- 方法要点：使用稀疏交叉编码器联合建模多激活空间，分析特征组织
- 实验或效果：在1B令牌数据上训练，解释约87%方差，揭示MoE特征更少、更专注

## 摘要（原文）

> Mixture of Experts (MoE) achieve parameter-efficient scaling through sparse expert routing, yet their internal representations remain poorly understood compared to dense models. We present a systematic comparison of MoE and dense model internals using crosscoders, a variant of sparse autoencoders, that jointly models multiple activation spaces. We train 5-layer dense and MoEs (equal active parameters) on 1B tokens across code, scientific text, and english stories. Using BatchTopK crosscoders with explicitly designated shared features, we achieve $\sim 87\%$ fractional variance explained and uncover concrete differences in feature organization. The MoE learns significantly fewer unique features compared to the dense model. MoE-specific features also exhibit higher activation density than shared features, whereas dense-specific features show lower density. Our analysis reveals that MoEs develop more specialized, focused representations while dense models distribute information across broader, more general-purpose features.


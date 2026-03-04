---
layout: default
title: Conditioned Activation Transport for T2I Safety Steering
---

# Conditioned Activation Transport for T2I Safety Steering
**arXiv**：[2603.03163v1](https://arxiv.org/abs/2603.03163) · [PDF](https://arxiv.org/pdf/2603.03163.pdf)  
**作者**：Maciej Chrabąszcz, Aleksander Szymczyk, Jan Dubiński, Tomasz Trzciński, Franziska Boenisch, Adam Dziedzic  

**一句话要点**：提出条件激活传输以解决文本到图像模型安全引导中的质量下降问题

**关键词**：文本到图像模型, 安全引导, 激活传输, 非线性映射, 推理时干预, 对比数据集

## 3 点简述
- 核心问题：线性激活引导在安全提示下常导致图像质量下降
- 方法要点：基于几何条件机制和非线性传输图，仅在危险激活区域应用引导
- 实验或效果：在Z-Image和Infinity架构上验证，显著降低攻击成功率并保持图像保真度

## 摘要（原文）

> Despite their impressive capabilities, current Text-to-Image (T2I) models remain prone to generating unsafe and toxic content. While activation steering offers a promising inference-time intervention, we observe that linear activation steering frequently degrades image quality when applied to benign prompts. To address this trade-off, we first construct SafeSteerDataset, a contrastive dataset containing 2300 safe and unsafe prompt pairs with high cosine similarity. Leveraging this data, we propose Conditioned Activation Transport (CAT), a framework that employs a geometry-based conditioning mechanism and nonlinear transport maps. By conditioning transport maps to activate only within unsafe activation regions, we minimize interference with benign queries. We validate our approach on two state-of-the-art architectures: Z-Image and Infinity. Experiments demonstrate that CAT generalizes effectively across these backbones, significantly reducing Attack Success Rate while maintaining image fidelity compared to unsteered generations. Warning: This paper contains potentially offensive text and images.


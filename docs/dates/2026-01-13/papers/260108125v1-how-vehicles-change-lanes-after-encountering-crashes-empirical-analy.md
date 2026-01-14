---
layout: default
title: How vehicles change lanes after encountering crashes: Empirical analysis and modeling
---

# How vehicles change lanes after encountering crashes: Empirical analysis and modeling
**arXiv**：[2601.08125v1](https://arxiv.org/abs/2601.08125) · [PDF](https://arxiv.org/pdf/2601.08125.pdf)  
**作者**：Kequan Chen, Yuxuan Wang, Pan Liu, Victor L. Knoop, David Z. W. Wang, Yu Han  

**一句话要点**：提出基于图注意力模块的轨迹预测框架，以建模事故后换道中的让行行为。

**关键词**：事故后换道, 轨迹预测, 图注意力模块, 让行行为建模, 条件变分自编码器, Transformer解码器

## 3 点简述
- 核心问题：事故后换道行为特征未知，涉及高比例非让行行为，增加碰撞风险。
- 方法要点：构建事故后换道数据集，开发图注意力模块显式建模让行行为，结合条件变分自编码器和Transformer解码器预测轨迹。
- 实验或效果：模型在轨迹预测误差上优于基线10%以上，提升碰撞风险分析可靠性，验证了跨场景可迁移性。

## 摘要（原文）

> When a traffic crash occurs, following vehicles need to change lanes to bypass the obstruction. We define these maneuvers as post crash lane changes. In such scenarios, vehicles in the target lane may refuse to yield even after the lane change has already begun, increasing the complexity and crash risk of post crash LCs. However, the behavioral characteristics and motion patterns of post crash LCs remain unknown. To address this gap, we construct a post crash LC dataset by extracting vehicle trajectories from drone videos captured after crashes. Our empirical analysis reveals that, compared to mandatory LCs (MLCs) and discretionary LCs (DLCs), post crash LCs exhibit longer durations, lower insertion speeds, and higher crash risks. Notably, 79.4% of post crash LCs involve at least one instance of non yielding behavior from the new follower, compared to 21.7% for DLCs and 28.6% for MLCs. Building on these findings, we develop a novel trajectory prediction framework for post crash LCs. At its core is a graph based attention module that explicitly models yielding behavior as an auxiliary interaction aware task. This module is designed to guide both a conditional variational autoencoder and a Transformer based decoder to predict the lane changer's trajectory. By incorporating the interaction aware module, our model outperforms existing baselines in trajectory prediction performance by more than 10% in both average displacement error and final displacement error across different prediction horizons. Moreover, our model provides more reliable crash risk analysis by reducing false crash rates and improving conflict prediction accuracy. Finally, we validate the model's transferability using additional post crash LC datasets collected from different sites.


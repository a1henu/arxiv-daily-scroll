---
layout: default
title: AGMA: Adaptive Gaussian Mixture Anchors for Prior-Guided Multimodal Human Trajectory Forecasting
---

# AGMA: Adaptive Gaussian Mixture Anchors for Prior-Guided Multimodal Human Trajectory Forecasting
**arXiv**：[2602.04204v1](https://arxiv.org/abs/2602.04204) · [PDF](https://arxiv.org/pdf/2602.04204.pdf)  
**作者**：Chao Li, Rui Zhang, Siyuan Huang, Xian Zhong, Hongbo Jiang  

**一句话要点**：提出AGMA以解决行人轨迹预测中的先验错配问题，通过自适应高斯混合锚点构建高质量先验。

**关键词**：行人轨迹预测, 先验建模, 高斯混合模型, 自适应先验, 多模态预测

## 3 点简述
- 核心问题：现有方法因先验错配，难以捕捉行人行为的完整分布，限制预测准确性和多样性。
- 方法要点：AGMA分两阶段构建先验，从训练数据提取行为模式，并蒸馏为场景自适应全局先验。
- 实验或效果：在ETH-UCY、Stanford Drone和JRDB数据集上实现最优性能，验证高质量先验的关键作用。

## 摘要（原文）

> Human trajectory forecasting requires capturing the multimodal nature of pedestrian behavior. However, existing approaches suffer from prior misalignment. Their learned or fixed priors often fail to capture the full distribution of plausible futures, limiting both prediction accuracy and diversity. We theoretically establish that prediction error is lower-bounded by prior quality, making prior modeling a key performance bottleneck. Guided by this insight, we propose AGMA (Adaptive Gaussian Mixture Anchors), which constructs expressive priors through two stages: extracting diverse behavioral patterns from training data and distilling them into a scene-adaptive global prior for inference. Extensive experiments on ETH-UCY, Stanford Drone, and JRDB datasets demonstrate that AGMA achieves state-of-the-art performance, confirming the critical role of high-quality priors in trajectory forecasting.


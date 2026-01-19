---
layout: default
title: GMM-COMET: Continual Source-Free Universal Domain Adaptation via a Mean Teacher and Gaussian Mixture Model-Based Pseudo-Labeling
---

# GMM-COMET: Continual Source-Free Universal Domain Adaptation via a Mean Teacher and Gaussian Mixture Model-Based Pseudo-Labeling
**arXiv**：[2601.11161v1](https://arxiv.org/abs/2601.11161) · [PDF](https://arxiv.org/pdf/2601.11161.pdf)  
**作者**：Pascal Schlachter, Bin Yang  

**一句话要点**：提出GMM-COMET方法，通过均值教师与高斯混合模型伪标签解决持续源自由通用域自适应问题。

**关键词**：持续域自适应, 源自由学习, 均值教师, 高斯混合模型, 伪标签, 通用域自适应

## 3 点简述
- 核心问题：处理源数据不可用且目标域标签空间变化的持续多域自适应场景。
- 方法要点：结合均值教师框架与高斯混合模型伪标签，引入一致性损失提升稳定性。
- 实验或效果：在持续SF-UniDA中提供首个基线，在所有场景中优于仅源模型。

## 摘要（原文）

> Unsupervised domain adaptation tackles the problem that domain shifts between training and test data impair the performance of neural networks in many real-world applications. Thereby, in realistic scenarios, the source data may no longer be available during adaptation, and the label space of the target domain may differ from the source label space. This setting, known as source-free universal domain adaptation (SF-UniDA), has recently gained attention, but all existing approaches only assume a single domain shift from source to target. In this work, we present the first study on continual SF-UniDA, where the model must adapt sequentially to a stream of multiple different unlabeled target domains. Building upon our previous methods for online SF-UniDA, we combine their key ideas by integrating Gaussian mixture model-based pseudo-labeling within a mean teacher framework for improved stability over long adaptation sequences. Additionally, we introduce consistency losses for further robustness. The resulting method GMM-COMET provides a strong first baseline for continual SF-UniDA and is the only approach in our experiments to consistently improve upon the source-only model across all evaluated scenarios. Our code is available at https://github.com/pascalschlachter/GMM-COMET.


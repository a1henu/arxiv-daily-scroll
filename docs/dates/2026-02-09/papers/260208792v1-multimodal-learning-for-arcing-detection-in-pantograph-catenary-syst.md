---
layout: default
title: Multimodal Learning for Arcing Detection in Pantograph-Catenary Systems
---

# Multimodal Learning for Arcing Detection in Pantograph-Catenary Systems
**arXiv**：[2602.08792v1](https://arxiv.org/abs/2602.08792) · [PDF](https://arxiv.org/pdf/2602.08792.pdf)  
**作者**：Hao Dong, Eleni Chatzi, Olga Fink  

**一句话要点**：提出多模态框架MultiDeepSAD，结合视觉与力数据以提升受电弓-接触网系统电弧检测的准确性与鲁棒性。

**关键词**：多模态学习, 电弧检测, 受电弓-接触网系统, 异常检测, 数据增强, 深度学习

## 3 点简述
- 核心问题：受电弓-接触网界面电弧检测因瞬态性、噪声环境、数据稀缺及相似现象干扰而具挑战性。
- 方法要点：构建多模态数据集，扩展DeepSAD算法为MultiDeepSAD，并引入针对性的伪异常生成技术增强训练。
- 实验或效果：框架在实验中显著优于基线方法，对真实电弧事件敏感性高，能应对领域偏移和真实数据有限情况。

## 摘要（原文）

> The pantograph-catenary interface is essential for ensuring uninterrupted and reliable power delivery in electrified rail systems. However, electrical arcing at this interface poses serious risks, including accelerated wear of contact components, degraded system performance, and potential service disruptions. Detecting arcing events at the pantograph-catenary interface is challenging due to their transient nature, noisy operating environment, data scarcity, and the difficulty of distinguishing arcs from other similar transient phenomena. To address these challenges, we propose a novel multimodal framework that combines high-resolution image data with force measurements to more accurately and robustly detect arcing events. First, we construct two arcing detection datasets comprising synchronized visual and force measurements. One dataset is built from data provided by the Swiss Federal Railways (SBB), and the other is derived from publicly available videos of arcing events in different railway systems and synthetic force data that mimic the characteristics observed in the real dataset. Leveraging these datasets, we propose MultiDeepSAD, an extension of the DeepSAD algorithm for multiple modalities with a new loss formulation. Additionally, we introduce tailored pseudo-anomaly generation techniques specific to each data type, such as synthetic arc-like artifacts in images and simulated force irregularities, to augment training data and improve the discriminative ability of the model. Through extensive experiments and ablation studies, we demonstrate that our framework significantly outperforms baseline approaches, exhibiting enhanced sensitivity to real arcing events even under domain shifts and limited availability of real arcing observations.


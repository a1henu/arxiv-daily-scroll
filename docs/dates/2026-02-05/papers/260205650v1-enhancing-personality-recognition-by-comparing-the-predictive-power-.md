---
layout: default
title: Enhancing Personality Recognition by Comparing the Predictive Power of Traits, Facets, and Nuances
---

# Enhancing Personality Recognition by Comparing the Predictive Power of Traits, Facets, and Nuances
**arXiv**：[2602.05650v1](https://arxiv.org/abs/2602.05650) · [PDF](https://arxiv.org/pdf/2602.05650.pdf)  
**作者**：Amir Ansari, Jana Subirana, Bruna Silva, Sergio Escalera, David Gallardo-Pujol, Cristina Palmero  

**一句话要点**：提出基于细粒度人格层次（特质、方面、细微特征）的预测模型，以增强从视听交互数据中的人格识别性能。

**关键词**：人格识别, 大五人格模型, Transformer模型, 跨模态注意力, 视听交互数据, 细粒度预测

## 3 点简述
- 核心问题：依赖宽泛特质分数作为真实标签，结合有限训练数据，导致人格识别模型泛化能力受限。
- 方法要点：探索大五人格模型中更细粒度的层次（方面和细微特征），使用基于Transformer的模型，包含跨模态（视听）和跨主体（双人感知）注意力机制。
- 实验或效果：在UDIVA v0.5数据集上，细微特征级模型在交互场景中平均平方误差降低高达74%，优于方面和特质级模型。

## 摘要（原文）

> Personality is a complex, hierarchical construct typically assessed through item-level questionnaires aggregated into broad trait scores. Personality recognition models aim to infer personality traits from different sources of behavioral data. However, reliance on broad trait scores as ground truth, combined with limited training data, poses challenges for generalization, as similar trait scores can manifest through diverse, context dependent behaviors. In this work, we explore the predictive impact of the more granular hierarchical levels of the Big-Five Personality Model, facets and nuances, to enhance personality recognition from audiovisual interaction data. Using the UDIVA v0.5 dataset, we trained a transformer-based model including cross-modal (audiovisual) and cross-subject (dyad-aware) attention mechanisms. Results show that nuance-level models consistently outperform facet and trait-level models, reducing mean squared error by up to 74% across interaction scenarios.


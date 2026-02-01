---
layout: default
title: Making Foundation Models Probabilistic via Singular Value Ensembles
---

# Making Foundation Models Probabilistic via Singular Value Ensembles
**arXiv**：[2601.22068v1](https://arxiv.org/abs/2601.22068) · [PDF](https://arxiv.org/pdf/2601.22068.pdf)  
**作者**：Mehmet Ozgur Turkoglu, Dominik J. Mühlematter, Alexander Becker, Konrad Schindler, Helge Aasen  

**一句话要点**：提出奇异值集成方法，以参数高效方式为基础模型提供概率不确定性估计。

**关键词**：基础模型, 不确定性估计, 奇异值分解, 参数高效, 模型集成, 校准性

## 3 点简述
- 基础模型常产生过度自信的预测，传统集成方法计算成本过高。
- SVE通过冻结权重矩阵的奇异向量，仅训练奇异值来调制知识方向贡献，实现隐式集成。
- 实验表明SVE在NLP和视觉任务中提升校准性，参数增加少于1%，保持预测准确性。

## 摘要（原文）

> Foundation models have become a dominant paradigm in machine learning, achieving remarkable performance across diverse tasks through large-scale pretraining. However, these models often yield overconfident, uncalibrated predictions. The standard approach to quantifying epistemic uncertainty, training an ensemble of independent models, incurs prohibitive computational costs that scale linearly with ensemble size, making it impractical for large foundation models. We propose Singular Value Ensemble (SVE), a parameter-efficient implicit ensemble method that builds on a simple, but powerful core assumption: namely, that the singular vectors of the weight matrices constitute meaningful subspaces of the model's knowledge. Pretrained foundation models encode rich, transferable information in their weight matrices. If the singular vectors are indeed meaningful (orthogonal) "knowledge directions". To obtain a model ensemble, we modulate only how strongly each direction contributes to the output. Rather than learning entirely new parameters, we freeze the singular vectors and only train per-member singular values that rescale the contribution of each direction in that shared knowledge basis. Ensemble diversity emerges naturally as stochastic initialization and random sampling of mini-batches during joint training cause different members to converge to different combinations of the same underlying knowledge. SVE achieves uncertainty quantification comparable to explicit deep ensembles while increasing the parameter count of the base model by less than 1%, making principled uncertainty estimation accessible in resource-constrained settings. We validate SVE on NLP and vision tasks with various different backbones and show that it improves calibration while maintaining predictive accuracy.


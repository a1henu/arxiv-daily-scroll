---
layout: default
title: An interpretable prototype parts-based neural network for medical tabular data
---

# An interpretable prototype parts-based neural network for medical tabular data
**arXiv**：[2603.05423v1](https://arxiv.org/abs/2603.05423) · [PDF](https://arxiv.org/pdf/2603.05423.pdf)  
**作者**：Jacek Karolczak, Jerzy Stefanowski  

**一句话要点**：提出基于原型部件的可解释神经网络，用于医疗表格数据分类与临床决策支持。

**关键词**：可解释机器学习, 原型部件网络, 医疗表格数据, 临床决策支持, 特征离散化

## 3 点简述
- 核心问题：医疗领域需模型预测准确且可解释，以增强临床信任与决策透明度。
- 方法要点：采用可训练特征分块学习原型部件，以二进制或离散化特征子集表示，实现人类可读解释。
- 实验或效果：在医疗基准数据集上分类性能与基线模型竞争，同时提供透明预测，弥合性能与可解释性差距。

## 摘要（原文）

> The ability to interpret machine learning model decisions is critical in such domains as healthcare, where trust in model predictions is as important as their accuracy. Inspired by the development of prototype parts-based deep neural networks in computer vision, we propose a new model for tabular data, specifically tailored to medical records, that requires discretization of diagnostic result norms. Unlike the original vision models that rely on the spatial structure, our method employs trainable patching over features describing a patient, to learn meaningful prototypical parts from structured data. These parts are represented as binary or discretized feature subsets. This allows the model to express prototypes in human-readable terms, enabling alignment with clinical language and case-based reasoning. Our proposed neural network is inherently interpretable and offers interpretable concept-based predictions by comparing the patient's description to learned prototypes in the latent space of the network. In experiments, we demonstrate that the model achieves classification performance competitive to widely used baseline models on medical benchmark datasets, while also offering transparency, bridging the gap between predictive performance and interpretability in clinical decision support.


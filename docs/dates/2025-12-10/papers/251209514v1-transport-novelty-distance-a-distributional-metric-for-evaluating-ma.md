---
layout: default
title: Transport Novelty Distance: A Distributional Metric for Evaluating Material Generative Models
---

# Transport Novelty Distance: A Distributional Metric for Evaluating Material Generative Models
**arXiv**：[2512.09514v1](https://arxiv.org/abs/2512.09514) · [PDF](https://arxiv.org/pdf/2512.09514.pdf)  
**作者**：Paul Hagemann, Simon Müller, Janine George, Philipp Benner  

**一句话要点**：提出Transport Novelty Distance以评估材料生成模型的质量与新颖性

**关键词**：材料生成模型评估, 最优传输理论, 图神经网络, 对比学习, 晶体结构预测

## 3 点简述
- 现有评估方法难以同时衡量生成材料的质量和新颖性
- 基于最优传输理论，通过阈值将训练与生成特征耦合分解为质量和记忆机制
- 在晶体结构预测相关实验和数据集上验证了该指标的有效性

## 摘要（原文）

> Recent advances in generative machine learning have opened new possibilities for the discovery and design of novel materials. However, as these models become more sophisticated, the need for rigorous and meaningful evaluation metrics has grown. Existing evaluation approaches often fail to capture both the quality and novelty of generated structures, limiting our ability to assess true generative performance. In this paper, we introduce the Transport Novelty Distance (TNovD) to judge generative models used for materials discovery jointly by the quality and novelty of the generated materials. Based on ideas from Optimal Transport theory, TNovD uses a coupling between the features of the training and generated sets, which is refined into a quality and memorization regime by a threshold. The features are generated from crystal structures using a graph neural network that is trained to distinguish between materials, their augmented counterparts, and differently sized supercells using contrastive learning. We evaluate our proposed metric on typical toy experiments relevant for crystal structure prediction, including memorization, noise injection and lattice deformations. Additionally, we validate the TNovD on the MP20 validation set and the WBM substitution dataset, demonstrating that it is capable of detecting both memorized and low-quality material data. We also benchmark the performance of several popular material generative models. While introduced for materials, our TNovD framework is domain-agnostic and can be adapted for other areas, such as images and molecules.


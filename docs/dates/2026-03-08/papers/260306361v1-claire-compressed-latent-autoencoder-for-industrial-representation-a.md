---
layout: default
title: CLAIRE: Compressed Latent Autoencoder for Industrial Representation and Evaluation -- A Deep Learning Framework for Smart Manufacturing
---

# CLAIRE: Compressed Latent Autoencoder for Industrial Representation and Evaluation -- A Deep Learning Framework for Smart Manufacturing
**arXiv**：[2603.06361v1](https://arxiv.org/abs/2603.06361) · [PDF](https://arxiv.org/pdf/2603.06361.pdf)  
**作者**：Mohammadhossein Ghahramani, Mengchu Zhou  

**一句话要点**：提出CLAIRE框架，通过压缩潜在自编码器与下游分类器集成，解决智能制造中高维传感器数据的故障检测问题。

**关键词**：智能制造, 故障检测, 深度自编码器, 潜在表示学习, 可解释AI, 高维数据

## 3 点简述
- 核心问题：高维工业环境中传感器数据复杂、噪声多、冗余高，导致故障检测准确性低。
- 方法要点：采用优化深度自编码器将原始输入压缩到潜在空间，捕获内在数据结构并抑制噪声，结合下游分类器进行故障预测。
- 实验或效果：在高维数据集上，CLAIRE显著优于直接在原始特征上训练的传统分类器，并利用基于博弈论的可解释性技术分析潜在空间。

## 摘要（原文）

> Accurate fault detection in high-dimensional industrial environments remains a major challenge due to the inherent complexity, noise, and redundancy in sensor data. This paper introduces CLAIRE, i.e., a hybrid end-to-end learning framework that integrates unsupervised deep representation learning with supervised classification for intelligent quality control in smart manufacturing systems. It employs an optimized deep autoencoder to transform raw input into a compact latent space, effectively capturing the intrinsic data structure while suppressing irrelevant or noisy features. The learned representations are then fed into a downstream classifier to perform binary fault prediction. Experimental results on a high-dimensional dataset demonstrate that CLAIRE significantly outperforms conventional classifiers trained directly on raw features. Moreover, the framework incorporates a post hoc phase, using a game-theory-based interpretability technique, to analyze the latent space and identify the most informative input features contributing to fault predictions. The proposed framework highlights the potential of integrating explainable AI with feature-aware regularization for robust fault detection. The modular and interpretable nature of the proposed framework makes it highly adaptable, offering promising applications in other domains characterized by complex, high-dimensional data, such as healthcare, finance, and environmental monitoring.


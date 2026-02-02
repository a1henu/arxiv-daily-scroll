---
layout: default
title: Leveraging Convolutional Sparse Autoencoders for Robust Movement Classification from Low-Density sEMG
---

# Leveraging Convolutional Sparse Autoencoders for Robust Movement Classification from Low-Density sEMG
**arXiv**：[2601.23011v1](https://arxiv.org/abs/2601.23011) · [PDF](https://arxiv.org/pdf/2601.23011.pdf)  
**作者**：Blagoj Hristov, Zoran Hadzi-Velkov, Katerina Hadzi-Velkova Saneva, Gorjan Nadzinski, Vesna Ojleska Latkoska  

**一句话要点**：提出卷积稀疏自编码器框架，用于低密度表面肌电信号的鲁棒手势分类

**关键词**：表面肌电信号分类, 卷积稀疏自编码器, 少样本迁移学习, 增量学习, 手势识别, 肌电假肢控制

## 3 点简述
- 核心问题：肌电假肢控制受高主体间变异性和高密度传感器临床不实用性的限制。
- 方法要点：使用卷积稀疏自编码器从原始信号提取时间特征，无需启发式特征工程。
- 实验或效果：在6类手势集上实现94.3% F1分数，通过少样本迁移学习将未见主体性能从35.1%提升至92.3%。

## 摘要（原文）

> Reliable control of myoelectric prostheses is often hindered by high inter-subject variability and the clinical impracticality of high-density sensor arrays. This study proposes a deep learning framework for accurate gesture recognition using only two surface electromyography (sEMG) channels. The method employs a Convolutional Sparse Autoencoder (CSAE) to extract temporal feature representations directly from raw signals, eliminating the need for heuristic feature engineering. On a 6-class gesture set, our model achieved a multi-subject F1-score of 94.3% $\pm$ 0.3%. To address subject-specific differences, we present a few-shot transfer learning protocol that improved performance on unseen subjects from a baseline of 35.1% $\pm$ 3.1% to 92.3% $\pm$ 0.9% with minimal calibration data. Furthermore, the system supports functional extensibility through an incremental learning strategy, allowing for expansion to a 10-class set with a 90.0% $\pm$ 0.2% F1-score without full model retraining. By combining high precision with minimal computational and sensor overhead, this framework provides a scalable and efficient approach for the next generation of affordable and adaptive prosthetic systems.


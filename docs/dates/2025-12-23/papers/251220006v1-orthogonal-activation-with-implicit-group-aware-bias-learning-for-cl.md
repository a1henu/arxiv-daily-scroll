---
layout: default
title: Orthogonal Activation with Implicit Group-Aware Bias Learning for Class Imbalance
---

# Orthogonal Activation with Implicit Group-Aware Bias Learning for Class Imbalance
**arXiv**：[2512.20006v1](https://arxiv.org/abs/2512.20006) · [PDF](https://arxiv.org/pdf/2512.20006.pdf)  
**作者**：Sukumar Kishanthan, Asela Hevapathige  

**一句话要点**：提出OGAB激活函数以解决深度学习中的类别不平衡问题

**关键词**：类别不平衡, 激活函数, 正交变换, 组感知偏置, 深度学习, 特征学习

## 3 点简述
- 类别不平衡导致分类器性能下降，是机器学习常见挑战。
- OGAB结合正交性和隐式组感知偏置学习，增强特征可区分性。
- 在真实和合成不平衡数据集上验证，性能优于传统和可学习激活函数。

## 摘要（原文）

> Class imbalance is a common challenge in machine learning and data mining, often leading to suboptimal performance in classifiers. While deep learning excels in feature extraction, its performance still deteriorates under imbalanced data. In this work, we propose a novel activation function, named OGAB, designed to alleviate class imbalance in deep learning classifiers. OGAB incorporates orthogonality and group-aware bias learning to enhance feature distinguishability in imbalanced scenarios without explicitly requiring label information. Our key insight is that activation functions can be used to introduce strong inductive biases that can address complex data challenges beyond traditional non-linearity. Our work demonstrates that orthogonal transformations can preserve information about minority classes by maintaining feature independence, thereby preventing the dominance of majority classes in the embedding space. Further, the proposed group-aware bias mechanism automatically identifies data clusters and adjusts embeddings to enhance class separability without the need for explicit supervision. Unlike existing approaches that address class imbalance through preprocessing data modifications or post-processing corrections, our proposed approach tackles class imbalance during the training phase at the embedding learning level, enabling direct integration with the learning process. We demonstrate the effectiveness of our solution on both real-world and synthetic imbalanced datasets, showing consistent performance improvements over both traditional and learnable activation functions.


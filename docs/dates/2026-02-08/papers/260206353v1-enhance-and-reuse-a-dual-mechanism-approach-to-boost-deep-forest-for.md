---
layout: default
title: Enhance and Reuse: A Dual-Mechanism Approach to Boost Deep Forest for Label Distribution Learning
---

# Enhance and Reuse: A Dual-Mechanism Approach to Boost Deep Forest for Label Distribution Learning
**arXiv**：[2602.06353v1](https://arxiv.org/abs/2602.06353) · [PDF](https://arxiv.org/pdf/2602.06353.pdf)  
**作者**：Jia-Le Xu, Shen-Huan Lyu, Yu-Nian Wang, Ning Chen, Zhihao Qu, Bin Tang, Baoliu Ye  

**一句话要点**：提出增强与重用特征深度森林方法，以提升标签分布学习性能。

**关键词**：标签分布学习, 深度森林, 特征增强, 特征重用, 树集成学习

## 3 点简述
- 核心问题：现有深度森林方法在标签分布学习中未有效利用标签相关性。
- 方法要点：通过标签相关性增强特征，并对验证集表现差的样本进行特征重用。
- 实验或效果：在六个评估指标上优于其他对比算法。

## 摘要（原文）

> Label distribution learning (LDL) requires the learner to predict the degree of correlation between each sample and each label. To achieve this, a crucial task during learning is to leverage the correlation among labels. Deep Forest (DF) is a deep learning framework based on tree ensembles, whose training phase does not rely on backpropagation. DF performs in-model feature transform using the prediction of each layer and achieves competitive performance on many tasks. However, its exploration in the field of LDL is still in its infancy. The few existing methods that apply DF to the field of LDL do not have effective ways to utilize the correlation among labels. Therefore, we propose a method named Enhanced and Reused Feature Deep Forest (ERDF). It mainly contains two mechanisms: feature enhancement exploiting label correlation and measure-aware feature reuse. The first one is to utilize the correlation among labels to enhance the original features, enabling the samples to acquire more comprehensive information for the task of LDL. The second one performs a reuse operation on the features of samples that perform worse than the previous layer on the validation set, in order to ensure the stability of the training process. This kind of Enhance-Reuse pattern not only enables samples to enrich their features but also validates the effectiveness of their new features and conducts a reuse process to prevent the noise from spreading further. Experiments show that our method outperforms other comparison algorithms on six evaluation metrics.


---
layout: default
title: Investigation into respiratory sound classification for an imbalanced data set using hybrid LSTM-KAN architectures
---

# Investigation into respiratory sound classification for an imbalanced data set using hybrid LSTM-KAN architectures
**arXiv**：[2601.03610v1](https://arxiv.org/abs/2601.03610) · [PDF](https://arxiv.org/pdf/2601.03610.pdf)  
**作者**：Nithinkumar K., Anand R  

**一句话要点**：提出混合LSTM-KAN架构以解决呼吸音分类中的类别不平衡问题

**关键词**：呼吸音分类, 类别不平衡, LSTM, KAN, 不平衡缓解策略, 深度学习

## 3 点简述
- 核心问题：呼吸音分类面临声学差异细微和临床数据集类别严重不平衡的挑战。
- 方法要点：结合LSTM进行序列特征编码和KAN进行分类，并集成特征提取与不平衡缓解策略。
- 实验或效果：在高度偏斜的六类数据集上，模型达到94.6%准确率和0.703宏平均F1分数，提升少数类检测性能。

## 摘要（原文）

> Respiratory sounds captured via auscultation contain critical clues for diagnosing pulmonary conditions. Automated classification of these sounds faces challenges due to subtle acoustic differences and severe class imbalance in clinical datasets. This study investigates respiratory sound classification with a focus on mitigating pronounced class imbalance. We propose a hybrid deep learning model that combines a Long Short-Term Memory (LSTM) network for sequential feature encoding with a Kolmogorov-Arnold Network (KAN) for classification. The model is integrated with a comprehensive feature extraction pipeline and targeted imbalance mitigation strategies. Experiments were conducted on a public respiratory sound database comprising six classes with a highly skewed distribution. Techniques such as focal loss, class-specific data augmentation, and Synthetic Minority Over-sampling Technique (SMOTE) were employed to enhance minority class recognition. The proposed Hybrid LSTM-KAN model achieves an overall accuracy of 94.6 percent and a macro-averaged F1 score of 0.703, despite the dominant COPD class accounting for over 86 percent of the data. Improved detection performance is observed for minority classes compared to baseline approaches, demonstrating the effectiveness of the proposed architecture for imbalanced respiratory sound classification.


---
layout: default
title: Class Confidence Aware Reweighting for Long Tailed Learning
---

# Class Confidence Aware Reweighting for Long Tailed Learning
**arXiv**：[2601.15924v1](https://arxiv.org/abs/2601.15924) · [PDF](https://arxiv.org/pdf/2601.15924.pdf)  
**作者**：Brainard Philemon Jagati, Jitendra Tembhurne, Harsh Goud, Rudra Pratap Singh, Chandrashekhar Meshram  

**一句话要点**：提出基于类别置信度的重加权方案以解决长尾学习中的类别不平衡问题

**关键词**：长尾学习, 类别不平衡, 置信度感知, 重加权方案, 损失调制

## 3 点简述
- 核心问题：长尾数据分布导致深度神经网络性能下降，尾部类别训练样本不足
- 方法要点：设计类别和置信度感知的重加权方案，通过Ω函数基于预测置信度和类别频率调制损失贡献
- 实验或效果：在CIFAR-100-LT、ImageNet-LT和iNaturalist2018数据集上验证，不同不平衡因子下效果显著

## 摘要（原文）

> Deep neural network models degrade significantly in the long-tailed data distribution, with the overall training data dominated by a small set of classes in the head, and the tail classes obtaining less training examples. Addressing the imbalance in the classes, attention in the related literature was given mainly to the adjustments carried out in the decision space in terms of either corrections performed at the logit level in order to compensate class-prior bias, with the least attention to the optimization process resulting from the adjustments introduced through the differences in the confidences among the samples. In the current study, we present the design of a class and confidence-aware re-weighting scheme for long-tailed learning. This scheme is purely based upon the loss level and has a complementary nature to the existing methods performing the adjustment of the logits. In the practical implementation stage of the proposed scheme, we use an Ω(p_t, f_c) function. This function enables the modulation of the contribution towards the training task based upon the confidence value of the prediction, as well as the relative frequency of the corresponding class. Our observations in the experiments are corroborated by significant experimental results performed on the CIFAR-100-LT, ImageNet-LT, and iNaturalist2018 datasets under various values of imbalance factors that clearly authenticate the theoretical discussions above.


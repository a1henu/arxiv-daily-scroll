---
layout: default
title: A Multi-View Consistency Framework with Semi-Supervised Domain Adaptation
---

# A Multi-View Consistency Framework with Semi-Supervised Domain Adaptation
**arXiv**：[2601.19266v1](https://arxiv.org/abs/2601.19266) · [PDF](https://arxiv.org/pdf/2601.19266.pdf)  
**作者**：Yuting Hong, Li Dong, Xiaojie Qiu, Hui Xiao, Baochen Yao, Siming Zheng, Chengbin Peng  

**一句话要点**：提出多视图一致性框架，通过去偏策略和伪负标签解决半监督域适应中的类别相似性偏差问题。

**关键词**：半监督域适应, 多视图一致性, 去偏策略, 伪负标签, 跨域特征对齐

## 3 点简述
- 核心问题：目标域标记样本有限导致特征空间类别相似性，引发预测偏差。
- 方法要点：结合去偏策略调整预测概率，利用伪负标签增强训练，并引入跨域亲和性学习对齐特征。
- 实验或效果：在DomainNet和Office-Home数据集上优于现有方法，提升模型适应性和性能。

## 摘要（原文）

> Semi-Supervised Domain Adaptation (SSDA) leverages knowledge from a fully labeled source domain to classify data in a partially labeled target domain. Due to the limited number of labeled samples in the target domain, there can be intrinsic similarity of classes in the feature space, which may result in biased predictions, even when the model is trained on a balanced dataset. To overcome this limitation, we introduce a multi-view consistency framework, which includes two views for training strongly augmented data. One is a debiasing strategy for correcting class-wise prediction probabilities according to the prediction performance of the model. The other involves leveraging pseudo-negative labels derived from the model predictions. Furthermore, we introduce a cross-domain affinity learning aimed at aligning features of the same class across different domains, thereby enhancing overall performance. Experimental results demonstrate that our method outperforms the competing methods on two standard domain adaptation datasets, DomainNet and Office-Home. Combining unsupervised domain adaptation and semi-supervised learning offers indispensable contributions to the industrial sector by enhancing model adaptability, reducing annotation costs, and improving performance.


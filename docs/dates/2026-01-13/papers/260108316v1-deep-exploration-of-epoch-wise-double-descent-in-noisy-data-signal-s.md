---
layout: default
title: Deep Exploration of Epoch-wise Double Descent in Noisy Data: Signal Separation, Large Activation, and Benign Overfitting
---

# Deep Exploration of Epoch-wise Double Descent in Noisy Data: Signal Separation, Large Activation, and Benign Overfitting
**arXiv**：[2601.08316v1](https://arxiv.org/abs/2601.08316) · [PDF](https://arxiv.org/pdf/2601.08316.pdf)  
**作者**：Tomoki Kubo, Ryuken Uda, Yusuke Iida  

**一句话要点**：通过信号分离分析揭示噪声数据中epoch-wise双下降的内部机制与良性过拟合

**关键词**：epoch-wise双下降, 良性过拟合, 大型激活, 信号分离, 噪声数据, 深度学习泛化

## 3 点简述
- 研究噪声数据下深度学习的epoch-wise双下降现象，关注内部结构演化
- 分解损失曲线为干净与噪声数据信号，分析激活分离与大型激活
- 实验在CIFAR-10数据集上进行，发现良性过拟合与大型激活相关

## 摘要（原文）

> Deep double descent is one of the key phenomena underlying the generalization capability of deep learning models. In this study, epoch-wise double descent, which is delayed generalization following overfitting, was empirically investigated by focusing on the evolution of internal structures. Fully connected neural networks of three different sizes were trained on the CIFAR-10 dataset with 30% label noise. By decomposing the loss curves into signal contributions from clean and noisy training data, the epoch-wise evolutions of internal signals were analyzed separately. Three main findings were obtained from this analysis. First, the model achieved strong re-generalization on test data even after perfectly fitting noisy training data during the double descent phase, corresponding to a "benign overfitting" state. Second, noisy data were learned after clean data, and as learning progressed, their corresponding internal activations became increasingly separated in outer layers; this enabled the model to overfit only noisy data. Third, a single, very large activation emerged in the shallow layer across all models; this phenomenon is referred as "outliers," "massive activa-tions," and "super activations" in recent large language models and evolves with re-generalization. The magnitude of large activation correlated with input patterns but not with output patterns. These empirical findings directly link the recent key phenomena of "deep double descent," "benign overfitting," and "large activation", and support the proposal of a novel scenario for understanding deep double descent.


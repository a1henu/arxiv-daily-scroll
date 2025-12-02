---
layout: default
title: The Active and Noise-Tolerant Strategic Perceptron
---

# The Active and Noise-Tolerant Strategic Perceptron
**arXiv**：[2512.01783v1](https://arxiv.org/abs/2512.01783) · [PDF](https://arxiv.org/pdf/2512.01783.pdf)  
**作者**：Maria-Florina Blacan, Hedyeh Beyhaghi  

**一句话要点**：提出主动且抗噪的战略感知机算法，以在战略环境中高效分类代理。

**关键词**：主动学习, 战略分类, 感知机算法, 标签复杂度, 噪声容忍

## 3 点简述
- 研究主动学习在战略分类中的应用，处理代理特征操纵带来的挑战。
- 算法基于主动感知机修改，在单位球均匀分布下实现指数级标签复杂度改进。
- 在非可实现情况下，使用约O(d ln 1/ε)标签查询，错误率相对最优分类器有限。

## 摘要（原文）

> We initiate the study of active learning algorithms for classifying strategic agents. Active learning is a well-established framework in machine learning in which the learner selectively queries labels, often achieving substantially higher accuracy and efficiency than classical supervised methods-especially in settings where labeling is costly or time-consuming, such as hiring, admissions, and loan decisions. Strategic classification, however, addresses scenarios where agents modify their features to obtain more favorable outcomes, resulting in observed data that is not truthful. Such manipulation introduces challenges beyond those in learning from clean data. Our goal is to design active and noise-tolerant algorithms that remain effective in strategic environments-algorithms that classify strategic agents accurately while issuing as few label requests as possible. The central difficulty is to simultaneously account for strategic manipulation and preserve the efficiency gains of active learning.
>   Our main result is an algorithm for actively learning linear separators in the strategic setting that preserves the exponential improvement in label complexity over passive learning previously obtained only in the non-strategic case. Specifically, for data drawn uniformly from the unit sphere, we show that a modified version of the Active Perceptron algorithm [DKM05,YZ17] achieves excess error $ε$ using only $\tilde{O}(d \ln \frac{1}ε)$ label queries and incurs at most $\tilde{O}(d \ln \frac{1}ε)$ additional mistakes relative to the optimal classifier, even in the nonrealizable case, when a $\tildeΩ(ε)$ fraction of inputs have inconsistent labels with the optimal classifier. The algorithm is computationally efficient and, under these distributional assumptions, requires substantially fewer label queries than prior work on strategic Perceptron [ABBN21].


---
layout: default
title: RankOOD - Class Ranking-based Out-of-Distribution Detection
---

# RankOOD - Class Ranking-based Out-of-Distribution Detection
**arXiv**：[2511.19996v1](https://arxiv.org/abs/2511.19996) · [PDF](https://arxiv.org/pdf/2511.19996.pdf)  
**作者**：Dishanika Denipitiyage, Naveen Karunanayake, Suranga Seneviratne, Sanjay Chawla  

**一句话要点**：提出RankOOD基于类排序的OOD检测方法，提升近OOD基准性能。

**关键词**：分布外检测, 类排序, Plackett-Luce损失, 深度学习模型, TinyImageNet基准

## 3 点简述
- 核心问题：解决深度学习模型在分布外检测中的误判问题。
- 方法要点：使用Plackett-Luce损失训练模型，基于类排序模式进行检测。
- 实验或效果：在TinyImageNet基准上FPR95降低4.3%，达到SOTA。

## 摘要（原文）

> We propose RankOOD, a rank-based Out-of-Distribution (OOD) detection approach based on training a model with the Placket-Luce loss, which is now extensively used for preference alignment tasks in foundational models. Our approach is based on the insight that with a deep learning model trained using the Cross Entropy Loss, in-distribution (ID) class prediction induces a ranking pattern for each ID class prediction. The RankOOD framework formalizes the insight by first extracting a rank list for each class using an initial classifier and then uses another round of training with the Plackett-Luce loss, where the class rank, a fixed permutation for each class, is the predicted variable. An OOD example may get assigned with high probability to an ID example, but the probability of it respecting the ranking classification is likely to be small. RankOOD, achieves SOTA performance on the near-ODD TinyImageNet evaluation benchmark, reducing FPR95 by 4.3%.


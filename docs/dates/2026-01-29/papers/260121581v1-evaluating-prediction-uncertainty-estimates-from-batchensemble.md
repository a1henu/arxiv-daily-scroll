---
layout: default
title: Evaluating Prediction Uncertainty Estimates from BatchEnsemble
---

# Evaluating Prediction Uncertainty Estimates from BatchEnsemble
**arXiv**：[2601.21581v1](https://arxiv.org/abs/2601.21581) · [PDF](https://arxiv.org/pdf/2601.21581.pdf)  
**作者**：Morten Blørstad, Herman Jangsett Mostein, Nello Blaser, Pekka Parviainen  

**一句话要点**：提出BatchEnsemble和GRUBE以高效估计深度学习模型的不确定性

**关键词**：不确定性估计, BatchEnsemble, GRUBE, 深度学习, 序列建模, 集成学习

## 3 点简述
- 深度学习模型在不确定性估计方面存在困难，现有方法计算成本高或低估不确定性。
- 研究BatchEnsemble作为通用可扩展方法，并引入GRUBE扩展至序列建模。
- 实验表明BatchEnsemble性能媲美深度集成，优于蒙特卡洛dropout，且参数更少、训练推理更快。

## 摘要（原文）

> Deep learning models struggle with uncertainty estimation. Many approaches are either computationally infeasible or underestimate uncertainty. We investigate \textit{BatchEnsemble} as a general and scalable method for uncertainty estimation across both tabular and time series tasks. To extend BatchEnsemble to sequential modeling, we introduce GRUBE, a novel BatchEnsemble GRU cell. We compare the BatchEnsemble to Monte Carlo dropout and deep ensemble models. Our results show that BatchEnsemble matches the uncertainty estimation performance of deep ensembles, and clearly outperforms Monte Carlo dropout. GRUBE achieves similar or better performance in both prediction and uncertainty estimation. These findings show that BatchEnsemble and GRUBE achieve similar performance with fewer parameters and reduced training and inference time compared to traditional ensembles.


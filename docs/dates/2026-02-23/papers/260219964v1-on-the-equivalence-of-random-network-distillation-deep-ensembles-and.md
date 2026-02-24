---
layout: default
title: On the Equivalence of Random Network Distillation, Deep Ensembles, and Bayesian Inference
---

# On the Equivalence of Random Network Distillation, Deep Ensembles, and Bayesian Inference
**arXiv**：[2602.19964v1](https://arxiv.org/abs/2602.19964) · [PDF](https://arxiv.org/pdf/2602.19964.pdf)  
**作者**：Moritz A. Zanger, Yijun Wu, Pascal R. Van der Vaart, Wendelin Böhmer, Matthijs T. J. Spaan  

**一句话要点**：建立随机网络蒸馏与深度集成、贝叶斯推断的理论等价性，为不确定性量化提供统一视角

**关键词**：不确定性量化, 随机网络蒸馏, 深度集成, 贝叶斯推断, 神经正切核, 理论等价性

## 3 点简述
- 核心问题：随机网络蒸馏（RND）缺乏理论解释，其不确定性估计与其他方法的关系未知
- 方法要点：在无限网络宽度极限下，使用神经正切核框架分析RND，证明其平方自预测误差等价于深度集成的预测方差
- 实验或效果：通过构建特定RND目标函数，使RND误差分布匹配贝叶斯推断的后验预测分布，并设计后验采样算法

## 摘要（原文）

> Uncertainty quantification is central to safe and efficient deployments of deep learning models, yet many computationally practical methods lack lacking rigorous theoretical motivation. Random network distillation (RND) is a lightweight technique that measures novelty via prediction errors against a fixed random target. While empirically effective, it has remained unclear what uncertainties RND measures and how its estimates relate to other approaches, e.g. Bayesian inference or deep ensembles. This paper establishes these missing theoretical connections by analyzing RND within the neural tangent kernel framework in the limit of infinite network width. Our analysis reveals two central findings in this limit: (1) The uncertainty signal from RND -- its squared self-predictive error -- is equivalent to the predictive variance of a deep ensemble. (2) By constructing a specific RND target function, we show that the RND error distribution can be made to mirror the centered posterior predictive distribution of Bayesian inference with wide neural networks. Based on this equivalence, we moreover devise a posterior sampling algorithm that generates i.i.d. samples from an exact Bayesian posterior predictive distribution using this modified \textit{Bayesian RND} model. Collectively, our findings provide a unified theoretical perspective that places RND within the principled frameworks of deep ensembles and Bayesian inference, and offer new avenues for efficient yet theoretically grounded uncertainty quantification methods.


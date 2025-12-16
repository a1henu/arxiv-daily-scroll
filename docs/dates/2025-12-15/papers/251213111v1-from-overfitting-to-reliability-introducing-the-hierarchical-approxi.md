---
layout: default
title: From Overfitting to Reliability: Introducing the Hierarchical Approximate Bayesian Neural Network
---

# From Overfitting to Reliability: Introducing the Hierarchical Approximate Bayesian Neural Network
**arXiv**：[2512.13111v1](https://arxiv.org/abs/2512.13111) · [PDF](https://arxiv.org/pdf/2512.13111.pdf)  
**作者**：Hayk Amirkhanian, Marco F. Huber  

**一句话要点**：提出分层近似贝叶斯神经网络以解决过拟合和不确定性估计问题，适用于安全关键环境。

**关键词**：贝叶斯神经网络, 过拟合缓解, 不确定性估计, 分层先验, 闭式计算, 安全关键应用

## 3 点简述
- 核心问题：神经网络存在超参数调优和过拟合挑战，影响模型可靠性。
- 方法要点：使用高斯-逆Wishart分布作为权重超先验，提供闭式预测分布和权重后验，计算复杂度线性。
- 实验或效果：模型在分布外任务中表现稳健，性能常优于先进模型，提供可靠不确定性估计。

## 摘要（原文）

> In recent years, neural networks have revolutionized various domains, yet challenges such as hyperparameter tuning and overfitting remain significant hurdles. Bayesian neural networks offer a framework to address these challenges by incorporating uncertainty directly into the model, yielding more reliable predictions, particularly for out-of-distribution data. This paper presents Hierarchical Approximate Bayesian Neural Network, a novel approach that uses a Gaussian-inverse-Wishart distribution as a hyperprior of the network's weights to increase both the robustness and performance of the model. We provide analytical representations for the predictive distribution and weight posterior, which amount to the calculation of the parameters of Student's t-distributions in closed form with linear complexity with respect to the number of weights. Our method demonstrates robust performance, effectively addressing issues of overfitting and providing reliable uncertainty estimates, particularly for out-of-distribution tasks. Experimental results indicate that HABNN not only matches but often outperforms state-of-the-art models, suggesting a promising direction for future applications in safety-critical environments.


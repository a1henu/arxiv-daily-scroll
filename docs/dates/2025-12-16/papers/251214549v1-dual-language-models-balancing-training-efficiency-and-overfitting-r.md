---
layout: default
title: Dual Language Models: Balancing Training Efficiency and Overfitting Resilience
---

# Dual Language Models: Balancing Training Efficiency and Overfitting Resilience
**arXiv**：[2512.14549v1](https://arxiv.org/abs/2512.14549) · [PDF](https://arxiv.org/pdf/2512.14549.pdf)  
**作者**：David Samuel, Lucas Georges Gabriel Charpentier  

**一句话要点**：提出双目标训练方法，结合自回归与掩码扩散目标以平衡训练效率与过拟合鲁棒性。

**关键词**：双目标训练, 自回归模型, 掩码扩散模型, 训练效率, 过拟合鲁棒性, 语言模型优化

## 3 点简述
- 核心问题：自回归模型训练效率高但易过拟合，掩码扩散模型鲁棒性强但训练效率低。
- 方法要点：无需架构修改，结合两种训练目标，通过调整目标比例优化模型性能。
- 实验或效果：在50个语言模型上评估，双目标训练在所有设置下均优于单目标模型，最优比例相似。

## 摘要（原文）

> This paper combines autoregressive and masked-diffusion training objectives without any architectural modifications, resulting in flexible language models that outperform single-objective models. Autoregressive modeling has been a popular approach, partly because of its training efficiency; however, that comes at the cost of sensitivity to overfitting. On the other hand, masked-diffusion models are less efficient to train while being more resilient to overfitting. In this work, we demonstrate that dual-objective training achieves the best of both worlds. To derive the optimal ratio between both objectives, we train and evaluate 50 language models under varying levels of data repetition. We show that it is optimal to combine both objectives under all evaluated settings and that the optimal ratio is similar whether targeting autoregressive or masked-diffusion downstream performance.


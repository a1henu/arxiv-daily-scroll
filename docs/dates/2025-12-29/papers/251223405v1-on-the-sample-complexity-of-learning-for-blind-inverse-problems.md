---
layout: default
title: On the Sample Complexity of Learning for Blind Inverse Problems
---

# On the Sample Complexity of Learning for Blind Inverse Problems
**arXiv**：[2512.23405v1](https://arxiv.org/abs/2512.23405) · [PDF](https://arxiv.org/pdf/2512.23405.pdf)  
**作者**：Nathan Buskulic, Luca Calatroni, Lorenzo Rosasco, Silvia Villa  

**一句话要点**：在线性最小均方误差估计框架下，为盲逆问题学习提供理论保证与样本复杂度分析

**关键词**：盲逆问题, 线性最小均方误差估计, 样本复杂度, Tikhonov正则化, 理论保证, 数值实验

## 3 点简述
- 研究盲逆问题中前向算子未知时的学习理论，聚焦线性最小均方误差估计器
- 推导最优估计器闭式解，建立与Tikhonov正则化的等价性，并证明收敛性
- 通过数值实验验证理论结果，展示样本复杂度与噪声、算子随机性的关系

## 摘要（原文）

> Blind inverse problems arise in many experimental settings where the forward operator is partially or entirely unknown. In this context, methods developed for the non-blind case cannot be adapted in a straightforward manner. Recently, data-driven approaches have been proposed to address blind inverse problems, demonstrating strong empirical performance and adaptability. However, these methods often lack interpretability and are not supported by rigorous theoretical guarantees, limiting their reliability in applied domains such as imaging inverse problems. In this work, we shed light on learning in blind inverse problems within the simplified yet insightful framework of Linear Minimum Mean Square Estimators (LMMSEs). We provide an in-depth theoretical analysis, deriving closed-form expressions for optimal estimators and extending classical results. In particular, we establish equivalences with suitably chosen Tikhonov-regularized formulations, where the regularization depends explicitly on the distributions of the unknown signal, the noise, and the random forward operators. We also prove convergence results under appropriate source condition assumptions. Furthermore, we derive rigorous finite-sample error bounds that characterize the performance of learned estimators as a function of the noise level, problem conditioning, and number of available samples. These bounds explicitly quantify the impact of operator randomness and reveal the associated convergence rates as this randomness vanishes. Finally, we validate our theoretical findings through illustrative numerical experiments that confirm the predicted convergence behavior.


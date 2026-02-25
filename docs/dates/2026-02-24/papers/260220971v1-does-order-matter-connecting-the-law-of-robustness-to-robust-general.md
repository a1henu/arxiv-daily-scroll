---
layout: default
title: Does Order Matter : Connecting The Law of Robustness to Robust Generalization
---

# Does Order Matter : Connecting The Law of Robustness to Robust Generalization
**arXiv**：[2602.20971v1](https://arxiv.org/abs/2602.20971) · [PDF](https://arxiv.org/pdf/2602.20971.pdf)  
**作者**：Himadri Mandal, Vishnu Varadarajan, Jaee Ponde, Aritra Das, Mihir More, Debayan Gupta  

**一句话要点**：连接鲁棒性定律与鲁棒泛化，证明鲁棒泛化不改变平滑插值所需的Lipschitz常数阶数。

**关键词**：鲁棒性定律, 鲁棒泛化, Lipschitz常数, Rademacher复杂度, 过参数化, 平滑插值

## 3 点简述
- 核心问题：连接鲁棒性定律与鲁棒泛化，解决Bubeck和Sellke提出的开放问题。
- 方法要点：引入鲁棒泛化误差概念，转化为诱导鲁棒损失类的Rademacher复杂度下界。
- 实验或效果：在MNIST上验证Lipschitz常数缩放符合Wu等人的预测，并分析扰动半径与Lipschitz尺度的关系。

## 摘要（原文）

> Bubeck and Sellke (2021) pose as an open problem the connection between the law of robustness and robust generalization. The law of robustness states that overparameterization is necessary for models to interpolate robustly; in particular, robust interpolation requires the learned function to be Lipschitz. Robust generalization asks whether small robust training loss implies small robust test loss. We resolve this problem by explicitly connecting the two for arbitrary data distributions. Specifically, we introduce a nontrivial notion of robust generalization error and convert it into a lower bound on the expected Rademacher complexity of the induced robust loss class. Our bounds recover the $Ω(n^{1/d})$ regime of Wu et al.\ (2023) and show that, up to constants, robust generalization does not change the order of the Lipschitz constant required for smooth interpolation. We conduct experiments to probe the predicted scaling with dataset size and model capacity, testing whether empirical behavior aligns more closely with the predictions of Bubeck and Sellke (2021) or Wu et al.\ (2023). For MNIST, we find that the lower-bound Lipschitz constant scales on the order predicted by Wu et al.\ (2023). Informally, to obtain low robust generalization error, the Lipschitz constant must lie in a range that we bound, and the allowable perturbation radius is linked to the Lipschitz scale.


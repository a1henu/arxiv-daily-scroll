---
layout: default
title: Agnostic learning in (almost) optimal time via Gaussian surface area
---

# Agnostic learning in (almost) optimal time via Gaussian surface area
**arXiv**：[2603.06027v1](https://arxiv.org/abs/2603.06027) · [PDF](https://arxiv.org/pdf/2603.06027.pdf)  
**作者**：Lucas Pesenti, Lucas Slot, Manuel Wiedmer  

**一句话要点**：改进高斯表面面积与低阶多项式逼近分析，提升不可知学习复杂度界至近最优

**关键词**：不可知学习, 高斯表面面积, 低阶多项式逼近, 统计查询模型, 复杂度分析

## 3 点简述
- 核心问题：高斯分布下概念类的不可知学习复杂度与低阶多项式L1逼近性相关
- 方法要点：通过直接类比布尔超立方构造，将所需多项式阶数从O(Γ²/ε⁴)降至Õ(Γ²/ε²)
- 实验或效果：结合下界结果，在统计查询模型中为多项式阈值函数学习提供近最优复杂度界

## 摘要（原文）

> The complexity of learning a concept class under Gaussian marginals in the difficult agnostic model is closely related to its $L_1$-approximability by low-degree polynomials. For any concept class with Gaussian surface area at most $Γ$, Klivans et al. (2008) show that degree $d = O(Γ^2 / \varepsilon^4)$ suffices to achieve an $\varepsilon$-approximation. This leads to the best-known bounds on the complexity of learning a variety of concept classes. In this note, we improve their analysis by showing that degree $d = \tilde O (Γ^2 / \varepsilon^2)$ is enough. In light of lower bounds due to Diakonikolas et al. (2021), this yields (near) optimal bounds on the complexity of agnostically learning polynomial threshold functions in the statistical query model. Our proof relies on a direct analogue of a construction of Feldman et al. (2020), who considered $L_1$-approximation on the Boolean hypercube.


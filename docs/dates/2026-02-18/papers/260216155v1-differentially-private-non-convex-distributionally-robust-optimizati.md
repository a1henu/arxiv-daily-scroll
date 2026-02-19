---
layout: default
title: Differentially Private Non-convex Distributionally Robust Optimization
---

# Differentially Private Non-convex Distributionally Robust Optimization
**arXiv**：[2602.16155v1](https://arxiv.org/abs/2602.16155) · [PDF](https://arxiv.org/pdf/2602.16155.pdf)  
**作者**：Difei Xu, Meng Ding, Zebin Ma, Huanyi Xie, Youming Tao, Aicha Slaitane, Di Wang  

**一句话要点**：提出差分隐私双蜘蛛与递归蜘蛛方法，以解决非凸分布鲁棒优化中的隐私保护问题。

**关键词**：差分隐私, 分布鲁棒优化, 非凸优化, ψ-散度, KL-散度, 隐私保护机器学习

## 3 点简述
- 核心问题：传统经验风险最小化在分布偏移下性能下降，且差分隐私分布鲁棒优化研究不足。
- 方法要点：针对ψ-散度重构为最小化问题，开发差分隐私双蜘蛛方法；针对KL-散度转化为组合有限和优化，开发递归蜘蛛方法。
- 实验或效果：方法在梯度范数上达到理论效用界，实验表现优于现有差分隐私极小极大优化方法。

## 摘要（原文）

> Real-world deployments routinely face distribution shifts, group imbalances, and adversarial perturbations, under which the traditional Empirical Risk Minimization (ERM) framework can degrade severely.
>   Distributionally Robust Optimization (DRO) addresses this issue by optimizing the worst-case expected loss over an uncertainty set of distributions, offering a principled approach to robustness.
>   Meanwhile, as training data in DRO always involves sensitive information, safeguarding it against leakage under Differential Privacy (DP) is essential.
>   In contrast to classical DP-ERM, DP-DRO has received much less attention due to its minimax optimization structure with uncertainty constraint.
>   To bridge the gap, we provide a comprehensive study of DP-(finite-sum)-DRO with $ψ$-divergence and non-convex loss.
>   First, we study DRO with general $ψ$-divergence by reformulating it as a minimization problem, and develop a novel $(\varepsilon, δ)$-DP optimization method, called DP Double-Spider, tailored to this structure.
>   Under mild assumptions, we show that it achieves a utility bound of $\mathcal{O}(\frac{1}{\sqrt{n}}+ (\frac{\sqrt{d \log (1/δ)}}{n \varepsilon})^{2/3})$ in terms of the gradient norm, where $n$ denotes the data size and $d$ denotes the model dimension.
>   We further improve the utility rate for specific divergences.
>   In particular, for DP-DRO with KL-divergence, by transforming the problem into a compositional finite-sum optimization problem, we develop a DP Recursive-Spider method and show that it achieves a utility bound of $\mathcal{O}((\frac{\sqrt{d \log(1/δ)}}{n\varepsilon})^{2/3} )$, matching the best-known result for non-convex DP-ERM.
>   Experimentally, we demonstrate that our proposed methods outperform existing approaches for DP minimax optimization.


---
layout: default
title: On the Tension Between Optimality and Adversarial Robustness in Policy Optimization
---

# On the Tension Between Optimality and Adversarial Robustness in Policy Optimization
**arXiv**：[2512.01228v1](https://arxiv.org/abs/2512.01228) · [PDF](https://arxiv.org/pdf/2512.01228.pdf)  
**作者**：Haoran Li, Jiayu Lv, Congying Han, Zicheng Zhang, Anqi Li, Yan Liu, Tiande Guo, Nan Jiang  

**一句话要点**：提出BARPO双层框架以调和深度强化学习中策略优化的最优性与对抗鲁棒性

**关键词**：深度强化学习, 对抗鲁棒性, 策略优化, 双层优化, 全局景观分析, 理论实践差距

## 3 点简述
- 核心问题：标准策略优化与对抗鲁棒策略优化在理论一致但实践中存在最优性与鲁棒性冲突
- 方法要点：通过调制对抗者强度统一两种优化，缓解全局景观复杂性，提升导航性
- 实验或效果：BARPO在广泛实验中优于基线ARPO，实现理论与实证性能的调和

## 摘要（原文）

> Achieving optimality and adversarial robustness in deep reinforcement learning has long been regarded as conflicting goals. Nonetheless, recent theoretical insights presented in CAR suggest a potential alignment, raising the important question of how to realize this in practice. This paper first identifies a key gap between theory and practice by comparing standard policy optimization (SPO) and adversarially robust policy optimization (ARPO). Although they share theoretical consistency, a fundamental tension between robustness and optimality arises in practical policy gradient methods. SPO tends toward convergence to vulnerable first-order stationary policies (FOSPs) with strong natural performance, whereas ARPO typically favors more robust FOSPs at the expense of reduced returns. Furthermore, we attribute this tradeoff to the reshaping effect of the strongest adversary in ARPO, which significantly complicates the global landscape by inducing deceptive sticky FOSPs. This improves robustness but makes navigation more challenging. To alleviate this, we develop the BARPO, a bilevel framework unifying SPO and ARPO by modulating adversary strength, thereby facilitating navigability while preserving global optima. Extensive empirical results demonstrate that BARPO consistently outperforms vanilla ARPO, providing a practical approach to reconcile theoretical and empirical performance.


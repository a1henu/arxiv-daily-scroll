---
layout: default
title: Variance-Reduced $(\varepsilon,δ)-$Unlearning using Forget Set Gradients
---

# Variance-Reduced $(\varepsilon,δ)-$Unlearning using Forget Set Gradients
**arXiv**：[2602.14938v1](https://arxiv.org/abs/2602.14938) · [PDF](https://arxiv.org/pdf/2602.14938.pdf)  
**作者**：Martin Van Waerebeke, Marco Lorenzi, Kevin Scaman, El Mahdi El Mhamdi, Giovanni Neglia  

**一句话要点**：提出方差缩减遗忘算法，在强凸目标下结合遗忘集梯度实现高效且可证明的(ε,δ)-遗忘。

**关键词**：机器学习遗忘, (ε,δ)-遗忘, 方差缩减, 梯度优化, 强凸目标, 理论保证

## 3 点简述
- 核心问题：现有(ε,δ)-遗忘方法未直接利用遗忘集梯度，而启发式方法缺乏理论保证。
- 方法要点：VRU算法在更新规则中直接包含遗忘集梯度，并证明满足(ε,δ)-遗忘，收敛速率更优。
- 实验或效果：实验验证VRU优于现有认证遗忘方法和利用遗忘集的基线，在低误差区域表现更佳。

## 摘要（原文）

> In machine unlearning, $(\varepsilon,δ)-$unlearning is a popular framework that provides formal guarantees on the effectiveness of the removal of a subset of training data, the forget set, from a trained model. For strongly convex objectives, existing first-order methods achieve $(\varepsilon,δ)-$unlearning, but they only use the forget set to calibrate injected noise, never as a direct optimization signal. In contrast, efficient empirical heuristics often exploit the forget samples (e.g., via gradient ascent) but come with no formal unlearning guarantees. We bridge this gap by presenting the Variance-Reduced Unlearning (VRU) algorithm. To the best of our knowledge, VRU is the first first-order algorithm that directly includes forget set gradients in its update rule, while provably satisfying ($(\varepsilon,δ)-$unlearning. We establish the convergence of VRU and show that incorporating the forget set yields strictly improved rates, i.e. a better dependence on the achieved error compared to existing first-order $(\varepsilon,δ)-$unlearning methods. Moreover, we prove that, in a low-error regime, VRU asymptotically outperforms any first-order method that ignores the forget set.Experiments corroborate our theory, showing consistent gains over both state-of-the-art certified unlearning methods and over empirical baselines that explicitly leverage the forget set.


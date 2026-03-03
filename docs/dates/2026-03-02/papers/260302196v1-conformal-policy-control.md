---
layout: default
title: Conformal Policy Control
---

# Conformal Policy Control
**arXiv**：[2603.02196v1](https://arxiv.org/abs/2603.02196) · [PDF](https://arxiv.org/pdf/2603.02196.pdf)  
**作者**：Drew Prinster, Clara Fannjiang, Ji Won Park, Kyunghyun Cho, Anqi Liu, Suchi Saria, Samuel Stanton  

**一句话要点**：提出基于保形校准的策略控制方法，以在高风险环境中实现安全探索与性能提升。

**关键词**：安全强化学习, 保形校准, 策略控制, 高风险环境, 有限样本保证

## 3 点简述
- 核心问题：高风险环境中，智能体探索新行为时可能违反安全约束，导致危害并中断交互，而过度保守会抑制探索。
- 方法要点：利用安全参考策略作为概率调节器，通过保形校准确定新策略的激进程度，可证明地强制执行用户声明的风险容忍度。
- 实验或效果：在自然语言问答和生物分子工程等应用中，该方法从部署之初即实现安全探索，并能提升性能。

## 摘要（原文）

> An agent must try new behaviors to explore and improve. In high-stakes environments, an agent that violates safety constraints may cause harm and must be taken offline, curtailing any future interaction. Imitating old behavior is safe, but excessive conservatism discourages exploration. How much behavior change is too much? We show how to use any safe reference policy as a probabilistic regulator for any optimized but untested policy. Conformal calibration on data from the safe policy determines how aggressively the new policy can act, while provably enforcing the user's declared risk tolerance. Unlike conservative optimization methods, we do not assume the user has identified the correct model class nor tuned any hyperparameters. Unlike previous conformal methods, our theory provides finite-sample guarantees even for non-monotonic bounded constraint functions. Our experiments on applications ranging from natural language question answering to biomolecular engineering show that safe exploration is not only possible from the first moment of deployment, but can also improve performance.


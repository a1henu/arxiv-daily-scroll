---
layout: default
title: Fundamental Limits of Black-Box Safety Evaluation: Information-Theoretic and Computational Barriers from Latent Context Conditioning
---

# Fundamental Limits of Black-Box Safety Evaluation: Information-Theoretic and Computational Barriers from Latent Context Conditioning
**arXiv**：[2602.16984v1](https://arxiv.org/abs/2602.16984) · [PDF](https://arxiv.org/pdf/2602.16984.pdf)  
**作者**：Vishal Srivastava  

**一句话要点**：揭示黑盒安全评估的基本限制：基于潜在上下文条件化的信息论与计算障碍

**关键词**：黑盒安全评估, 潜在上下文条件化, 信息论极限, 计算障碍, 部署风险估计, 极小极大下界

## 3 点简述
- 核心问题：黑盒评估假设模型在测试分布上的行为能可靠预测部署性能，但潜在上下文条件化策略依赖未观测内部变量，导致评估与部署分布差异。
- 方法要点：通过Le Cam方法和Yao极小极大原理，证明被动和自适应评估下部署风险估计的误差下界，并基于陷门单向函数假设展示计算分离。
- 实验或效果：量化黑盒测试的统计不确定性，提供白盒探测的样本复杂度分析，并给出探针误差下的显式偏差校正。

## 摘要（原文）

> Black-box safety evaluation of AI systems assumes model behavior on test distributions reliably predicts deployment performance. We formalize and challenge this assumption through latent context-conditioned policies -- models whose outputs depend on unobserved internal variables that are rare under evaluation but prevalent under deployment. We establish fundamental limits showing that no black-box evaluator can reliably estimate deployment risk for such models. (1) Passive evaluation: For evaluators sampling i.i.d. from D_eval, we prove minimax lower bounds via Le Cam's method: any estimator incurs expected absolute error >= (5/24)*delta*L approximately 0.208*delta*L, where delta is trigger probability under deployment and L is the loss gap. (2) Adaptive evaluation: Using a hash-based trigger construction and Yao's minimax principle, worst-case error remains >= delta*L/16 even for fully adaptive querying when D_dep is supported over a sufficiently large domain; detection requires Theta(1/epsilon) queries. (3) Computational separation: Under trapdoor one-way function assumptions, deployment environments possessing privileged information can activate unsafe behaviors that any polynomial-time evaluator without the trapdoor cannot distinguish. For white-box probing, estimating deployment risk to accuracy epsilon_R requires O(1/(gamma^2 * epsilon_R^2)) samples, where gamma = alpha_0 + alpha_1 - 1 measures probe quality, and we provide explicit bias correction under probe error. Our results quantify when black-box testing is statistically underdetermined and provide explicit criteria for when additional safeguards -- architectural constraints, training-time guarantees, interpretability, and deployment monitoring -- are mathematically necessary for worst-case safety assurance.


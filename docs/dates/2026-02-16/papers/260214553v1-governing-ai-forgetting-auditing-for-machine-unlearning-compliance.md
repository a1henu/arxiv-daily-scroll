---
layout: default
title: Governing AI Forgetting: Auditing for Machine Unlearning Compliance
---

# Governing AI Forgetting: Auditing for Machine Unlearning Compliance
**arXiv**：[2602.14553v1](https://arxiv.org/abs/2602.14553) · [PDF](https://arxiv.org/pdf/2602.14553.pdf)  
**作者**：Qinqi Lin, Ningning Ding, Lingjie Duan, Jianwei Huang  

**一句话要点**：提出经济框架以审计机器遗忘合规性，解决技术可行性与监管实施间的差距

**关键词**：机器遗忘, 合规审计, 博弈论, 认证遗忘, 监管框架, 数据删除

## 3 点简述
- 核心问题：AI操作者常不遵守数据删除请求，机器遗忘技术可行性与监管实施存在根本差距
- 方法要点：结合认证遗忘理论与监管执法，建立博弈论模型分析审计者与操作者策略互动
- 实验或效果：通过变换非线性定点问题，证明均衡存在性，揭示审计强度随删除请求增加而降低的悖论

## 摘要（原文）

> Despite legal mandates for the right to be forgotten, AI operators routinely fail to comply with data deletion requests. While machine unlearning (MU) provides a technical solution to remove personal data's influence from trained models, ensuring compliance remains challenging due to the fundamental gap between MU's technical feasibility and regulatory implementation. In this paper, we introduce the first economic framework for auditing MU compliance, by integrating certified unlearning theory with regulatory enforcement. We first characterize MU's inherent verification uncertainty using a hypothesis-testing interpretation of certified unlearning to derive the auditor's detection capability, and then propose a game-theoretic model to capture the strategic interactions between the auditor and the operator. A key technical challenge arises from MU-specific nonlinearities inherent in the model utility and the detection probability, which create complex strategic couplings that traditional auditing frameworks do not address and that also preclude closed-form solutions. We address this by transforming the complex bivariate nonlinear fixed-point problem into a tractable univariate auxiliary problem, enabling us to decouple the system and establish the equilibrium existence, uniqueness, and structural properties without relying on explicit solutions. Counterintuitively, our analysis reveals that the auditor can optimally reduce the inspection intensity as deletion requests increase, since the operator's weakened unlearning makes non-compliance easier to detect. This is consistent with recent auditing reductions in China despite growing deletion requests. Moreover, we prove that although undisclosed auditing offers informational advantages for the auditor, it paradoxically reduces the regulatory cost-effectiveness relative to disclosed auditing.


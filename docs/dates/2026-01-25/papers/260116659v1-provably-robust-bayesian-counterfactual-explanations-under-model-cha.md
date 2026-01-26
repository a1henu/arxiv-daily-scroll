---
layout: default
title: Provably Robust Bayesian Counterfactual Explanations under Model Changes
---

# Provably Robust Bayesian Counterfactual Explanations under Model Changes
**arXiv**：[2601.16659v1](https://arxiv.org/abs/2601.16659) · [PDF](https://arxiv.org/pdf/2601.16659.pdf)  
**作者**：Jamie Duell, Xiuyi Fan  

**一句话要点**：提出概率安全反事实解释方法，确保模型更新下的鲁棒性与可靠性

**关键词**：反事实解释, 贝叶斯方法, 模型鲁棒性, 概率保证, 不确定性约束, 优化框架

## 3 点简述
- 核心问题：模型频繁更新导致现有反事实解释失效或不可靠
- 方法要点：基于贝叶斯原理，生成δ-安全和ε-鲁棒的反事实解释，提供形式化概率保证
- 实验或效果：在多样数据集上验证，相比先进方法，生成更合理、可区分且可证明鲁棒的解释

## 摘要（原文）

> Counterfactual explanations (CEs) offer interpretable insights into machine learning predictions by answering ``what if?" questions. However, in real-world settings where models are frequently updated, existing counterfactual explanations can quickly become invalid or unreliable. In this paper, we introduce Probabilistically Safe CEs (PSCE), a method for generating counterfactual explanations that are $δ$-safe, to ensure high predictive confidence, and $ε$-robust to ensure low predictive variance. Based on Bayesian principles, PSCE provides formal probabilistic guarantees for CEs under model changes which are adhered to in what we refer to as the $\langle δ, ε\rangle$-set. Uncertainty-aware constraints are integrated into our optimization framework and we validate our method empirically across diverse datasets. We compare our approach against state-of-the-art Bayesian CE methods, where PSCE produces counterfactual explanations that are not only more plausible and discriminative, but also provably robust under model change.


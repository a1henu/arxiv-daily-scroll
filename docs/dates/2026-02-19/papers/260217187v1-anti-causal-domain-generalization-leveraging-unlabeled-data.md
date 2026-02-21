---
layout: default
title: Anti-causal domain generalization: Leveraging unlabeled data
---

# Anti-causal domain generalization: Leveraging unlabeled data
**arXiv**：[2602.17187v1](https://arxiv.org/abs/2602.17187) · [PDF](https://arxiv.org/pdf/2602.17187.pdf)  
**作者**：Sorawit Saengkyongam, Juan L. Gamella, Andrew C. Miller, Jonas Peters, Nicolai Meinshausen, Christina Heinze-Deml  

**一句话要点**：提出反因果域泛化方法，利用无标签数据提升模型对分布偏移的鲁棒性。

**关键词**：域泛化, 反因果学习, 无监督学习, 分布偏移, 正则化方法, 鲁棒性优化

## 3 点简述
- 研究域泛化问题，聚焦反因果场景，其中结果导致协变量变化。
- 提出两种正则化方法，惩罚模型对协变量均值和协方差环境变化的敏感性。
- 在物理系统和生理信号数据集上验证方法有效性，证明其最优性保证。

## 摘要（原文）

> The problem of domain generalization concerns learning predictive models that are robust to distribution shifts when deployed in new, previously unseen environments. Existing methods typically require labeled data from multiple training environments, limiting their applicability when labeled data are scarce. In this work, we study domain generalization in an anti-causal setting, where the outcome causes the observed covariates. Under this structure, environment perturbations that affect the covariates do not propagate to the outcome, which motivates regularizing the model's sensitivity to these perturbations. Crucially, estimating these perturbation directions does not require labels, enabling us to leverage unlabeled data from multiple environments. We propose two methods that penalize the model's sensitivity to variations in the mean and covariance of the covariates across environments, respectively, and prove that these methods have worst-case optimality guarantees under certain classes of environments. Finally, we demonstrate the empirical performance of our approach on a controlled physical system and a physiological signal dataset.


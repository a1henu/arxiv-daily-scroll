---
layout: default
title: An Accounting Identity for Algorithmic Fairness
---

# An Accounting Identity for Algorithmic Fairness
**arXiv**：[2601.20217v1](https://arxiv.org/abs/2601.20217) · [PDF](https://arxiv.org/pdf/2601.20217.pdf)  
**作者**：Hadi Elzayn, Jacob Goldin  

**一句话要点**：提出预测模型的会计恒等式，链接准确性与公平性，揭示二元预测中的互补关系。

**关键词**：算法公平性, 预测模型, 会计恒等式, 二元预测, 校准误差, 公平性权衡

## 3 点简述
- 核心问题：预测模型中准确性与公平性准则之间的内在联系与权衡。
- 方法要点：推导会计恒等式，将组内校准误差和组间误差不平衡与总不公平预算关联。
- 实验或效果：基准数据验证理论，显示公平干预常替代公平违规，降低准确性可能扩大不公平预算。

## 摘要（原文）

> We derive an accounting identity for predictive models that links accuracy with common fairness criteria. The identity shows that for globally calibrated models, the weighted sums of miscalibration within groups and error imbalance across groups is equal to a "total unfairness budget." For binary outcomes, this budget is the model's mean-squared error times the difference in group prevalence across outcome classes. The identity nests standard impossibility results as special cases, while also describing inherent tradeoffs when one or more fairness measures are not perfectly satisfied. The results suggest that accuracy and fairness are best viewed as complements in binary prediction tasks: increasing accuracy necessarily shrinks the total unfairness budget and vice-versa. Experiments on benchmark data confirm the theory and show that many fairness interventions largely substitute between fairness violations, and when they reduce accuracy they tend to expand the total unfairness budget. The results extend naturally to prediction tasks with non-binary outcomes, illustrating how additional outcome information can relax fairness incompatibilities and identifying conditions under which the binary-style impossibility does and does not extend to regression tasks.


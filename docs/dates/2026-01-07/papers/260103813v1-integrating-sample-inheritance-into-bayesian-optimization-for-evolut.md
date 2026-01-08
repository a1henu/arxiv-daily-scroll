---
layout: default
title: Integrating Sample Inheritance into Bayesian Optimization for Evolutionary Robotics
---

# Integrating Sample Inheritance into Bayesian Optimization for Evolutionary Robotics
**arXiv**：[2601.03813v1](https://arxiv.org/abs/2601.03813) · [PDF](https://arxiv.org/pdf/2601.03813.pdf)  
**作者**：K. Ege de Bruin, Kyrre Glette, Kai Olav Ellefsen  

**一句话要点**：提出样本继承结合贝叶斯优化以解决进化机器人中控制器学习预算不足问题

**关键词**：进化机器人, 贝叶斯优化, 样本继承, 控制器优化, 形态-控制器协同设计

## 3 点简述
- 进化机器人中，形态与控制器协同优化面临高学习成本挑战
- 采用贝叶斯优化与样本继承（先验传递与重评估）提升样本效率
- 实验显示重评估继承效果最佳，环境挑战性增强稳定步态

## 摘要（原文）

> In evolutionary robotics, robot morphologies are designed automatically using evolutionary algorithms. This creates a body-brain optimization problem, where both morphology and control must be optimized together. A common approach is to include controller optimization for each morphology, but starting from scratch for every new body may require a high controller learning budget. We address this by using Bayesian optimization for controller optimization, exploiting its sample efficiency and strong exploration capabilities, and using sample inheritance as a form of Lamarckian inheritance. Under a deliberately low controller learning budget for each morphology, we investigate two types of sample inheritance: (1) transferring all the parent's samples to the offspring to be used as prior without evaluating them, and (2) reevaluating the parent's best samples on the offspring. Both are compared to a baseline without inheritance. Our results show that reevaluation performs best, with prior-based inheritance also outperforming no inheritance. Analysis reveals that while the learning budget is too low for a single morphology, generational inheritance compensates for this by accumulating learned adaptations across generations. Furthermore, inheritance mainly benefits offspring morphologies that are similar to their parents. Finally, we demonstrate the critical role of the environment, with more challenging environments resulting in more stable walking gaits. Our findings highlight that inheritance mechanisms can boost performance in evolutionary robotics without needing large learning budgets, offering an efficient path toward more capable robot design.


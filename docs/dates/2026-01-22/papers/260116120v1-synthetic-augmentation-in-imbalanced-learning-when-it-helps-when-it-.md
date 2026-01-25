---
layout: default
title: Synthetic Augmentation in Imbalanced Learning: When It Helps, When It Hurts, and How Much to Add
---

# Synthetic Augmentation in Imbalanced Learning: When It Helps, When It Hurts, and How Much to Add
**arXiv**：[2601.16120v1](https://arxiv.org/abs/2601.16120) · [PDF](https://arxiv.org/pdf/2601.16120.pdf)  
**作者**：Zhengchi Ma, Anru R. Zhang  

**一句话要点**：提出统计框架分析不平衡学习中合成增强的效用与优化策略

**关键词**：不平衡学习, 合成数据增强, 统计框架, 验证调优, 分类性能

## 3 点简述
- 研究不平衡分类中合成增强的效用，揭示其并非总是有益，取决于局部对称性
- 理论推导最优合成样本数量，取决于生成器准确性与方向对齐性
- 提出验证调优合成大小方法，通过模拟和真实数据验证理论

## 摘要（原文）

> Imbalanced classification, where one class is observed far less frequently than the other, often causes standard training procedures to prioritize the majority class and perform poorly on rare but important cases. A classic and widely used remedy is to augment the minority class with synthetic examples, but two basic questions remain under-resolved: when does synthetic augmentation actually help, and how many synthetic samples should be generated?
>   We develop a unified statistical framework for synthetic augmentation in imbalanced learning, studying models trained on imbalanced data augmented with synthetic minority samples and evaluated under the balanced population risk. Our theory shows that synthetic data is not always beneficial. In a ``local symmetry" regime, imbalance is not the dominant source of error near the balanced optimum, so adding synthetic samples cannot improve learning rates and can even degrade performance by amplifying generator mismatch. When augmentation can help (a ``local asymmetry" regime), the optimal synthetic size depends on generator accuracy and on whether the generator's residual mismatch is directionally aligned with the intrinsic majority-minority shift. This structure can make the best synthetic size deviate from naive full balancing, sometimes by a small refinement and sometimes substantially when generator bias is systematic. Practically, we recommend Validation-Tuned Synthetic Size (VTSS): select the synthetic size by minimizing balanced validation loss over a range centered near the fully balanced baseline, while allowing meaningful departures when the data indicate them. Simulations and a real sepsis prediction study support the theory and illustrate when synthetic augmentation helps, when it cannot, and how to tune its quantity effectively.


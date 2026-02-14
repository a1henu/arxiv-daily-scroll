---
layout: default
title: Aggregate Models, Not Explanations: Improving Feature Importance Estimation
---

# Aggregate Models, Not Explanations: Improving Feature Importance Estimation
**arXiv**：[2602.11760v1](https://arxiv.org/abs/2602.11760) · [PDF](https://arxiv.org/pdf/2602.11760.pdf)  
**作者**：Joseph Paillard, Angel Reyero Lobo, Denis A. Engemann, Bertrand Thirion  

**一句话要点**：提出聚合模型而非解释的方法，以提高表达性模型的特征重要性估计准确性

**关键词**：特征重要性估计, 模型集成, 超额风险, 表达性模型, 生物医学应用

## 3 点简述
- 核心问题：表达性模型因数据采样和算法随机性导致特征重要性估计不稳定，影响生物医学应用
- 方法要点：理论分析表明，模型级集成优于解释级集成，能减少超额风险误差
- 实验或效果：在经典基准和UK Biobank蛋白质组学研究中验证了模型级集成的优势

## 摘要（原文）

> Feature-importance methods show promise in transforming machine learning models from predictive engines into tools for scientific discovery. However, due to data sampling and algorithmic stochasticity, expressive models can be unstable, leading to inaccurate variable importance estimates and undermining their utility in critical biomedical applications. Although ensembling offers a solution, deciding whether to explain a single ensemble model or aggregate individual model explanations is difficult due to the nonlinearity of importance measures and remains largely understudied. Our theoretical analysis, developed under assumptions accommodating complex state-of-the-art ML models, reveals that this choice is primarily driven by the model's excess risk. In contrast to prior literature, we show that ensembling at the model level provides more accurate variable-importance estimates, particularly for expressive models, by reducing this leading error term. We validate these findings on classical benchmarks and a large-scale proteomic study from the UK Biobank.


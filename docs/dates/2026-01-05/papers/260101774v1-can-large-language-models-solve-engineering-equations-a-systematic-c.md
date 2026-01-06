---
layout: default
title: Can Large Language Models Solve Engineering Equations? A Systematic Comparison of Direct Prediction and Solver-Assisted Approaches
---

# Can Large Language Models Solve Engineering Equations? A Systematic Comparison of Direct Prediction and Solver-Assisted Approaches
**arXiv**：[2601.01774v1](https://arxiv.org/abs/2601.01774) · [PDF](https://arxiv.org/pdf/2601.01774.pdf)  
**作者**：Sai Varun Kodathala, Rakesh Vunnam  

**一句话要点**：比较大语言模型直接预测与求解器辅助方法在工程方程求解中的性能，提出混合架构作为优化方案。

**关键词**：大语言模型, 工程方程求解, 混合架构, 数值方法, 符号操作, 迭代求解器

## 3 点简述
- 核心问题：评估大语言模型能否有效求解工程中的超越方程，对比直接数值预测与混合方法的优劣。
- 方法要点：结合大语言模型符号操作与牛顿-拉弗森迭代求解器，测试六种先进模型在七个工程领域的100个问题。
- 实验或效果：求解器辅助方法将平均相对误差降低67.9%至81.8%，尤其在电子学领域改进显著，达93.1%。

## 摘要（原文）

> Transcendental equations requiring iterative numerical solution pervade engineering practice, from fluid mechanics friction factor calculations to orbital position determination. We systematically evaluate whether Large Language Models can solve these equations through direct numerical prediction or whether a hybrid architecture combining LLM symbolic manipulation with classical iterative solvers proves more effective. Testing six state-of-the-art models (GPT-5.1, GPT-5.2, Gemini-3-Flash, Gemini-2.5-Lite, Claude-Sonnet-4.5, Claude-Opus-4.5) on 100 problems spanning seven engineering domains, we compare direct prediction against solver-assisted computation where LLMs formulate governing equations and provide initial conditions while Newton-Raphson iteration performs numerical solution. Direct prediction yields mean relative errors of 0.765 to 1.262 across models, while solver-assisted computation achieves 0.225 to 0.301, representing error reductions of 67.9% to 81.8%. Domain-specific analysis reveals dramatic improvements in Electronics (93.1%) due to exponential equation sensitivity, contrasted with modest gains in Fluid Mechanics (7.2%) where LLMs exhibit effective pattern recognition. These findings establish that contemporary LLMs excel at symbolic manipulation and domain knowledge retrieval but struggle with precision-critical iterative arithmetic, suggesting their optimal deployment as intelligent interfaces to classical numerical solvers rather than standalone computational engines.


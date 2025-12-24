---
layout: default
title: Optimality-Informed Neural Networks for Solving Parametric Optimization Problems
---

# Optimality-Informed Neural Networks for Solving Parametric Optimization Problems
**arXiv**：[2512.20270v1](https://arxiv.org/abs/2512.20270) · [PDF](https://arxiv.org/pdf/2512.20270.pdf)  
**作者**：Matthias K. Hoffmann, Amine Othmane, Kathrin Flaßkamp  

**一句话要点**：提出OptINNs以解决参数化优化问题，通过嵌入最优性条件提升学习代理的准确性与可行性。

**关键词**：参数化优化, 神经网络代理, KKT条件, 对偶变量预测, 约束处理, 数据效率

## 3 点简述
- 核心问题：参数化非线性约束优化问题在实时控制等场景中计算成本高，需高效求解。
- 方法要点：结合KKT残差损失和问题特定输出激活，减少数据需求并预测对偶变量。
- 实验或效果：在低维和高维问题上，相比二次惩罚基线，OptINNs降低约束违反和原始误差。

## 摘要（原文）

> Many engineering tasks require solving families of nonlinear constrained optimization problems, parametrized in setting-specific variables. This is computationally demanding, particularly, if solutions have to be computed across strongly varying parameter values, e.g., in real-time control or for model-based design. Thus, we propose to learn the mapping from parameters to the primal optimal solutions and to their corresponding duals using neural networks, giving a dense estimation in contrast to gridded approaches. Our approach, Optimality-informed Neural Networks (OptINNs), combines (i) a KKT-residual loss that penalizes violations of the first-order optimality conditions under standard constraint qualifications assumptions, and (ii) problem-specific output activations that enforce simple inequality constraints (e.g., box-type/positivity) by construction. This design reduces data requirements, allows the prediction of dual variables, and improves feasibility and closeness to optimality compared to penalty-only training. Taking quadratic penalties as a baseline, since this approach has been previously proposed for the considered problem class in literature, our method simplifies hyperparameter tuning and attains tighter adherence to optimality conditions. We evaluate OptINNs on different nonlinear optimization problems ranging from low to high dimensions. On small problems, OptINNs match a quadratic-penalty baseline in primal accuracy while additionally predicting dual variables with low error. On larger problems, OptINNs achieve lower constraint violations and lower primal error compared to neural networks based on the quadratic-penalty method. These results suggest that embedding feasibility and optimality into the network architecture and loss can make learning-based surrogates more accurate, feasible, and data-efficient for parametric optimization.


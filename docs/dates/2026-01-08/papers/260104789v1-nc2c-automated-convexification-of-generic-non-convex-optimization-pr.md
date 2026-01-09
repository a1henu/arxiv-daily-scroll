---
layout: default
title: NC2C: Automated Convexification of Generic Non-Convex Optimization Problems
---

# NC2C: Automated Convexification of Generic Non-Convex Optimization Problems
**arXiv**：[2601.04789v1](https://arxiv.org/abs/2601.04789) · [PDF](https://arxiv.org/pdf/2601.04789.pdf)  
**作者**：Xinyue Peng, Yanming Liu, Yihan Cang, Yuwei Zhang, Xinyi Wang, Songhang Deng, Jiannan Cao  

**一句话要点**：提出NC2C框架，利用大语言模型自动化将通用非凸优化问题转化为可解凸形式。

**关键词**：非凸优化, 自动化凸化, 大语言模型, 符号推理, 迭代验证

## 3 点简述
- 核心问题：非凸优化问题因复杂目标函数和约束导致传统求解器效率低下，依赖专家知识。
- 方法要点：基于LLM的端到端框架，自动检测非凸成分、选择凸化策略并生成严格凸等价问题。
- 实验效果：在100个通用非凸问题上，执行率89.3%，成功率76%，优于基线方法。

## 摘要（原文）

> Non-convex optimization problems are pervasive across mathematical programming, engineering design, and scientific computing, often posing intractable challenges for traditional solvers due to their complex objective functions and constrained landscapes. To address the inefficiency of manual convexification and the over-reliance on expert knowledge, we propose NC2C, an LLM-based end-to-end automated framework designed to transform generic non-convex optimization problems into solvable convex forms using large language models. NC2C leverages LLMs' mathematical reasoning capabilities to autonomously detect non-convex components, select optimal convexification strategies, and generate rigorous convex equivalents. The framework integrates symbolic reasoning, adaptive transformation techniques, and iterative validation, equipped with error correction loops and feasibility domain correction mechanisms to ensure the robustness and validity of transformed problems. Experimental results on a diverse dataset of 100 generic non-convex problems demonstrate that NC2C achieves an 89.3\% execution rate and a 76\% success rate in producing feasible, high-quality convex transformations. This outperforms baseline methods by a significant margin, highlighting NC2C's ability to leverage LLMs for automated non-convex to convex transformation, reduce expert dependency, and enable efficient deployment of convex solvers for previously intractable optimization tasks.


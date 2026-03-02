---
layout: default
title: ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference
---

# ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference
**arXiv**：[2602.23681v1](https://arxiv.org/abs/2602.23681) · [PDF](https://arxiv.org/pdf/2602.23681.pdf)  
**作者**：Siyuan Ma, Bo Gao, Xiaojun Jia, Simeng Qin, Tianlin Li, Ke Ma, Xiaoshuang Jia, Wenqi Ren, Yang Liu  

**一句话要点**：提出ODAR-Expert自适应路由框架，通过主动推理优化大语言模型推理的准确性与效率权衡。

**关键词**：大语言模型推理, 自适应路由, 主动推理, 自由能原理, 计算效率优化, 风险敏感决策

## 3 点简述
- 核心问题：现有大语言模型推理方法依赖均匀暴力采样，导致计算成本高、难以归因且可能引发过度思考。
- 方法要点：基于摊销主动推理的难度估计器动态路由查询，结合自由能原理的风险敏感融合机制选择答案。
- 实验或效果：在23个基准测试中表现优异，如MATH准确率达98.2%，并在开源栈上减少82%计算成本。

## 摘要（原文）

> The paradigm of large language model (LLM) reasoning is shifting from parameter scaling to test-time compute scaling, yet many existing approaches still rely on uniform brute-force sampling (for example, fixed best-of-N or self-consistency) that is costly, hard to attribute, and can trigger overthinking with diminishing returns. We propose ODAR-Expert, an adaptive routing framework that optimizes the accuracy-efficiency trade-off via principled resource allocation. ODAR uses a difficulty estimator grounded in amortized active inference to dynamically route queries between a heuristic Fast Agent and a deliberative Slow Agent. We further introduce a free-energy-principled, risk-sensitive fusion mechanism that selects answers by minimizing a variational free energy objective, balancing log-likelihood with epistemic uncertainty (varentropy) as a principled alternative to ad hoc voting over heterogeneous candidates. Extensive evaluation across 23 benchmarks shows strong and consistent gains, including 98.2% accuracy on MATH and 54.8% on Humanity's Last Exam (HLE), while improving the compute-accuracy frontier under compute-matched settings. We also validate reproducibility on a fully open-source stack (Llama 4 + DeepSeek), where ODAR surpasses homogeneous sampling strategies while reducing computational costs by 82%. Overall, our results suggest that thinking-optimal scaling requires adaptive resource allocation with free-energy-based decision-making rather than simply increasing test-time compute.


---
layout: default
title: BoRP: Bootstrapped Regression Probing for Scalable and Human-Aligned LLM Evaluation
---

# BoRP: Bootstrapped Regression Probing for Scalable and Human-Aligned LLM Evaluation
**arXiv**：[2601.18253v1](https://arxiv.org/abs/2601.18253) · [PDF](https://arxiv.org/pdf/2601.18253.pdf)  
**作者**：Peng Sun, Xiangyu Zhang, Duan Wu  

**一句话要点**：提出BoRP框架以解决开放对话AI中用户满意度评估的扩展性与对齐问题

**关键词**：用户满意度评估, 自举回归探测, 潜在空间几何, 部分最小二乘, A/B测试优化, 推理成本降低

## 3 点简述
- 核心问题：开放对话AI缺乏可靠评估指标，显式反馈稀疏，隐式指标模糊
- 方法要点：利用LLM潜在空间几何特性，基于极化指数自举生成评估准则，使用PLS映射隐藏状态到连续分数
- 实验或效果：在工业数据集上，BoRP显著优于生成基线，与人类判断对齐更好，并大幅降低推理成本

## 摘要（原文）

> Accurate evaluation of user satisfaction is critical for iterative development of conversational AI. However, for open-ended assistants, traditional A/B testing lacks reliable metrics: explicit feedback is sparse, while implicit metrics are ambiguous. To bridge this gap, we introduce BoRP (Bootstrapped Regression Probing), a scalable framework for high-fidelity satisfaction evaluation. Unlike generative approaches, BoRP leverages the geometric properties of LLM latent space. It employs a polarization-index-based bootstrapping mechanism to automate rubric generation and utilizes Partial Least Squares (PLS) to map hidden states to continuous scores. Experiments on industrial datasets show that BoRP (Qwen3-8B/14B) significantly outperforms generative baselines (even Qwen3-Max) in alignment with human judgments. Furthermore, BoRP reduces inference costs by orders of magnitude, enabling full-scale monitoring and highly sensitive A/B testing via CUPED.


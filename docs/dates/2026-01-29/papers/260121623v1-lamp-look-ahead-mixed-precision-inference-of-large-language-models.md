---
layout: default
title: LAMP: Look-Ahead Mixed-Precision Inference of Large Language Models
---

# LAMP: Look-Ahead Mixed-Precision Inference of Large Language Models
**arXiv**：[2601.21623v1](https://arxiv.org/abs/2601.21623) · [PDF](https://arxiv.org/pdf/2601.21623.pdf)  
**作者**：Stanislav Budzinskiy, Marian Gloser, Tolunay Yilmaz, Ying Hong Tham, Yuanyi Lin, Wenyi Fang, Fan Wu, Philipp Petersen  

**一句话要点**：提出LAMP方法以优化大语言模型推理中的混合精度计算，通过前瞻性策略提升精度

**关键词**：混合精度推理, Transformer优化, 舍入误差分析, 自适应策略, 大语言模型部署

## 3 点简述
- 核心问题：混合精度计算在Transformer推理中，如何平衡精度与效率，减少组合函数计算误差
- 方法要点：基于组合函数f(g(x))的舍入误差分析，自适应选择g(x)子集进行高精度计算，其余低精度
- 实验或效果：在GPT-2模型上测试，低重计算率下精度提升可达两个数量级

## 摘要（原文）

> Mixed-precision computations are a hallmark of the current stage of AI, driving the progress in large language models towards efficient, locally deployable solutions. This article addresses the floating-point computation of compositionally-rich functions, concentrating on transformer inference. Based on the rounding error analysis of a composition $f(g(\mathrm{x}))$, we provide an adaptive strategy that selects a small subset of components of $g(\mathrm{x})$ to be computed more accurately while all other computations can be carried out with lower accuracy. We then explain how this strategy can be applied to different compositions within a transformer and illustrate its overall effect on transformer inference. We study the effectiveness of this algorithm numerically on GPT-2 models and demonstrate that already very low recomputation rates allow for improvements of up to two orders of magnitude in accuracy.


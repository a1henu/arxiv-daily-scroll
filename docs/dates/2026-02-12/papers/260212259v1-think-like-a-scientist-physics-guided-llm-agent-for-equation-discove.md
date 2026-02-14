---
layout: default
title: Think like a Scientist: Physics-guided LLM Agent for Equation Discovery
---

# Think like a Scientist: Physics-guided LLM Agent for Equation Discovery
**arXiv**：[2602.12259v1](https://arxiv.org/abs/2602.12259) · [PDF](https://arxiv.org/pdf/2602.12259.pdf)  
**作者**：Jianke Yang, Ohm Venkatachalam, Mohammad Kianezhad, Sharvaree Vadgama, Rose Yu  

**一句话要点**：提出KeplerAgent框架，通过物理引导的LLM代理实现符号方程发现，提升科学推理准确性。

**关键词**：符号方程发现, 物理引导推理, LLM代理, 符号回归, 科学计算

## 3 点简述
- 核心问题：现有LLM系统直接从数据猜测方程，缺乏模拟科学家多步推理过程，如先推断物理属性再约束候选方程。
- 方法要点：KeplerAgent协调物理工具提取中间结构，配置符号回归引擎如PySINDy和PySR，包括函数库和结构约束。
- 实验或效果：在物理方程基准测试中，比LLM和传统基线显著提高符号准确性和对噪声数据的鲁棒性。

## 摘要（原文）

> Explaining observed phenomena through symbolic, interpretable formulas is a fundamental goal of science. Recently, large language models (LLMs) have emerged as promising tools for symbolic equation discovery, owing to their broad domain knowledge and strong reasoning capabilities. However, most existing LLM-based systems try to guess equations directly from data, without modeling the multi-step reasoning process that scientists often follow: first inferring physical properties such as symmetries, then using these as priors to restrict the space of candidate equations. We introduce KeplerAgent, an agentic framework that explicitly follows this scientific reasoning process. The agent coordinates physics-based tools to extract intermediate structure and uses these results to configure symbolic regression engines such as PySINDy and PySR, including their function libraries and structural constraints. Across a suite of physical equation benchmarks, KeplerAgent achieves substantially higher symbolic accuracy and greater robustness to noisy data than both LLM and traditional baselines.


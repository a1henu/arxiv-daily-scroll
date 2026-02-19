---
layout: default
title: Towards a Science of AI Agent Reliability
---

# Towards a Science of AI Agent Reliability
**arXiv**：[2602.16666v1](https://arxiv.org/abs/2602.16666) · [PDF](https://arxiv.org/pdf/2602.16666.pdf)  
**作者**：Stephan Rabanser, Sayash Kapoor, Peter Kirgis, Kangheng Liu, Saiteja Utpala, Arvind Narayanan  

**一句话要点**：提出十二项指标从四个维度评估AI代理可靠性，以弥补传统评估的不足。

**关键词**：AI代理评估, 可靠性指标, 安全关键工程, 一致性分析, 鲁棒性测试, 可预测性度量

## 3 点简述
- 核心问题：当前AI代理评估依赖单一成功率，忽略一致性、鲁棒性等关键操作缺陷。
- 方法要点：基于安全关键工程，定义一致性、鲁棒性、可预测性和安全性四个维度的十二项具体指标。
- 实验或效果：评估14个代理模型，发现能力提升对可靠性改善有限，暴露持续局限性。

## 摘要（原文）

> AI agents are increasingly deployed to execute important tasks. While rising accuracy scores on standard benchmarks suggest rapid progress, many agents still continue to fail in practice. This discrepancy highlights a fundamental limitation of current evaluations: compressing agent behavior into a single success metric obscures critical operational flaws. Notably, it ignores whether agents behave consistently across runs, withstand perturbations, fail predictably, or have bounded error severity. Grounded in safety-critical engineering, we provide a holistic performance profile by proposing twelve concrete metrics that decompose agent reliability along four key dimensions: consistency, robustness, predictability, and safety. Evaluating 14 agentic models across two complementary benchmarks, we find that recent capability gains have only yielded small improvements in reliability. By exposing these persistent limitations, our metrics complement traditional evaluations while offering tools for reasoning about how agents perform, degrade, and fail.


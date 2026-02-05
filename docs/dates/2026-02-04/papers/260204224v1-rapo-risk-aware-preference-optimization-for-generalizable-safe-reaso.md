---
layout: default
title: RAPO: Risk-Aware Preference Optimization for Generalizable Safe Reasoning
---

# RAPO: Risk-Aware Preference Optimization for Generalizable Safe Reasoning
**arXiv**：[2602.04224v1](https://arxiv.org/abs/2602.04224) · [PDF](https://arxiv.org/pdf/2602.04224.pdf)  
**作者**：Zeming Wei, Qiaosheng Zhang, Xia Hu, Xingcheng Xu  

**一句话要点**：提出风险感知偏好优化框架以增强大型推理模型在多样化越狱攻击下的安全推理泛化能力

**关键词**：大型推理模型, 安全推理, 偏好优化, 越狱攻击, 风险感知, 模型对齐

## 3 点简述
- 核心问题：大型推理模型的安全推理过程在复杂越狱攻击下泛化不足，导致安全失效
- 方法要点：基于风险感知的偏好优化，使模型自适应识别并处理安全风险，调整推理粒度
- 实验或效果：广泛实验验证RAPO能自适应泛化多种模型的安全推理，同时保持通用性能

## 摘要（原文）

> Large Reasoning Models (LRMs) have achieved tremendous success with their chain-of-thought (CoT) reasoning, yet also face safety issues similar to those of basic language models. In particular, while algorithms are designed to guide them to deliberately refuse harmful prompts with safe reasoning, this process often fails to generalize against diverse and complex jailbreak attacks. In this work, we attribute these failures to the generalization of the safe reasoning process, particularly their insufficiency against complex attack prompts. We provide both theoretical and empirical evidence to show the necessity of a more sufficient safe reasoning process to defend against advanced attack prompts. Building on this insight, we propose a Risk-Aware Preference Optimization (RAPO) framework that enables LRM to adaptively identify and address the safety risks with appropriate granularity in its thinking content. Extensive experiments demonstrate that RAPO successfully generalizes multiple LRMs' safe reasoning adaptively across diverse attack prompts whilst preserving general utility, contributing a robust alignment technique for LRM safety. Our code is available at https://github.com/weizeming/RAPO.


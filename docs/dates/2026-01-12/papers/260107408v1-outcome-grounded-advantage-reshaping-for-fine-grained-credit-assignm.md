---
layout: default
title: Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning
---

# Outcome-Grounded Advantage Reshaping for Fine-Grained Credit Assignment in Mathematical Reasoning
**arXiv**：[2601.07408v1](https://arxiv.org/abs/2601.07408) · [PDF](https://arxiv.org/pdf/2601.07408.pdf)  
**作者**：Ziheng Li, Liu Kang, Feng Xiao, Luxi Xing, Qingyi Si, Zhuoran Li, Weikang Gong, Deqing Yang, Yanghua Xiao, Hongcheng Guo  

**一句话要点**：提出基于结果的优势重塑方法，以解决数学推理中细粒度信用分配问题。

**关键词**：数学推理, 信用分配, 强化学习, 优势重塑, 细粒度优化

## 3 点简述
- 标准GRPO采用粗粒度信用分配，忽略推理步骤的贡献差异。
- 引入OAR机制，通过扰动和梯度策略估计令牌影响，重塑优势。
- 实验显示OAR显著提升GRPO性能，OAR-G在计算开销可忽略下接近OAR-P上限。

## 摘要（原文）

> Group Relative Policy Optimization (GRPO) has emerged as a promising critic-free reinforcement learning paradigm for reasoning tasks. However, standard GRPO employs a coarse-grained credit assignment mechanism that propagates group-level rewards uniformly to to every token in a sequence, neglecting the varying contribution of individual reasoning steps. We address this limitation by introducing Outcome-grounded Advantage Reshaping (OAR), a fine-grained credit assignment mechanism that redistributes advantages based on how much each token influences the model's final answer. We instantiate OAR via two complementary strategies: (1) OAR-P, which estimates outcome sensitivity through counterfactual token perturbations, serving as a high-fidelity attribution signal; (2) OAR-G, which uses an input-gradient sensitivity proxy to approximate the influence signal with a single backward pass. These importance signals are integrated with a conservative Bi-Level advantage reshaping scheme that suppresses low-impact tokens and boosts pivotal ones while preserving the overall advantage mass. Empirical results on extensive mathematical reasoning benchmarks demonstrate that while OAR-P sets the performance upper bound, OAR-G achieves comparable gains with negligible computational overhead, both significantly outperforming a strong GRPO baseline, pushing the boundaries of critic-free LLM reasoning.


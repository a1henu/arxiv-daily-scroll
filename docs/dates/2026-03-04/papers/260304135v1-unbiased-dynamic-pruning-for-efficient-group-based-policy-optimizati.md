---
layout: default
title: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization
---

# Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization
**arXiv**：[2603.04135v1](https://arxiv.org/abs/2603.04135) · [PDF](https://arxiv.org/pdf/2603.04135.pdf)  
**作者**：Haodong Zhu, Yangyang Ren, Yanjing Li, Mingbao Lin, Linlin Yang, Xuhui Liu, Xiantong Zhen, Haiguang Liu, Baochang Zhang  

**一句话要点**：提出动态剪枝策略优化以解决组相对策略优化计算成本高的问题

**关键词**：策略优化, 动态剪枝, 重要性采样, 计算效率, 大语言模型推理, 数学推理

## 3 点简述
- 核心问题：组相对策略优化因组采样需求导致计算成本过高，现有方法可能引入估计偏差
- 方法要点：通过重要性采样校正实现动态剪枝，保持梯度估计无偏，并引入密集提示打包缓解数据稀疏
- 实验或效果：在Qwen3-4B等模型上加速训练2.37倍，数学推理基准平均准确率提升3.36%

## 摘要（原文）

> Group Relative Policy Optimization (GRPO) effectively scales LLM reasoning but incurs prohibitive computational costs due to its extensive group-based sampling requirement. While recent selective data utilization methods can mitigate this overhead, they could induce estimation bias by altering the underlying sampling distribution, compromising theoretical rigor and convergence behavior. To address this limitation, we propose Dynamic Pruning Policy Optimization (DPPO), a framework that enables dynamic pruning while preserving unbiased gradient estimation through importance sampling-based correction. By incorporating mathematically derived rescaling factors, DPPO significantly accelerates GRPO training without altering the optimization objective of the full-batch baseline. Furthermore, to mitigate the data sparsity induced by pruning, we introduce Dense Prompt Packing, a window-based greedy strategy that maximizes valid token density and hardware utilization. Extensive experiments demonstrate that DPPO consistently accelerates training across diverse models and benchmarks. For instance, on Qwen3-4B trained on MATH, DPPO achieves 2.37$\times$ training speedup and outperforms GRPO by 3.36% in average accuracy across six mathematical reasoning benchmarks.


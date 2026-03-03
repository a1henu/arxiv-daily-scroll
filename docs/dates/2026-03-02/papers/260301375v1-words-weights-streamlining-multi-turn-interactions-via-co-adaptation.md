---
layout: default
title: Words & Weights: Streamlining Multi-Turn Interactions via Co-Adaptation
---

# Words & Weights: Streamlining Multi-Turn Interactions via Co-Adaptation
**arXiv**：[2603.01375v1](https://arxiv.org/abs/2603.01375) · [PDF](https://arxiv.org/pdf/2603.01375.pdf)  
**作者**：Chenxing Wei, Hong Wang, Ying He, Zhongxiang Dai, Bo Jiang, F. Richard Yu, Yao Shu  

**一句话要点**：提出ROSA2框架，通过词语与权重的协同适应优化多轮交互中的测试时策略适应问题。

**关键词**：测试时策略适应, 多轮交互, 协同适应, 词语与权重优化, 大型语言模型对齐

## 3 点简述
- 核心问题：现有方法将测试时适应视为单轴问题，忽略交互失败源于意图模糊与能力不足的耦合。
- 方法要点：ROSA2将交互重构为词语与权重的联合优化，利用文本梯度修正意图模糊，参数更新弥补能力差距。
- 实验或效果：在MATH数据集上性能提升30%，交互轮次减少40%，证明协同适应能有效收敛。

## 摘要（原文）

> Test-time policy adaptation for multi-turn interactions (T2PAM) is essential for aligning Large Language Models (LLMs) with dynamic user needs during inference time. However, existing paradigms commonly treat test-time adaptation as a single-axis problem, either purely refining instructions (Prompt Engineering) or only adjusting weights (Test-Time Training), ignoring that interaction failures stem from a coupled mix of ambiguity and incapacity. We argue that these two optimization paths are not merely additive but synergistic: semantic clarity acts as a pre-conditioner for effective parameter updates. To this end, we propose ROSA2, a framework that reformulates interaction as a joint optimization problem over the heterogeneous space of Words and Weights. By mathematically decomposing the error signal, ROSA2 utilizes textual gradients to rectify intent ambiguity and parameter updates to bridge capability gaps. Theoretically, we prove that this co-adaptation strictly reduces the required parameter shift for convergence. Empirically, ROSA2 outperforms state-of-the-art baselines by 30% on MATH while reducing interaction turns by 40%, demonstrating that refining the context unlocks the true potential of parameter updates.


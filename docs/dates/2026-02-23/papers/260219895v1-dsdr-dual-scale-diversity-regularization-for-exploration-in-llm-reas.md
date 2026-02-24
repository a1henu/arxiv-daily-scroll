---
layout: default
title: DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning
---

# DSDR: Dual-Scale Diversity Regularization for Exploration in LLM Reasoning
**arXiv**：[2602.19895v1](https://arxiv.org/abs/2602.19895) · [PDF](https://arxiv.org/pdf/2602.19895.pdf)  
**作者**：Zhongwei Wan, Yun Shen, Zhihao Dou, Donghao Zhou, Yu Zhang, Xin Wang, Hui Shen, Jing Xiong, Chaofan Tao, Zixuan Zhong, Peizhou Huang, Mi Zhang  

**一句话要点**：提出DSDR框架，通过双尺度多样性正则化解决LLM推理中探索不足的问题。

**关键词**：大语言模型推理, 强化学习, 多样性正则化, 探索策略, 策略优化, 验证器增强学习

## 3 点简述
- 现有RLVR方法探索有限，策略易收敛于少数推理模式，导致学习信号弱。
- DSDR分解多样性为全局和局部尺度，分别促进正确轨迹间多样性和防止模式内熵崩溃。
- 实验表明DSDR在多个推理基准上提升准确率和pass@k，验证双尺度多样性的重要性。

## 摘要（原文）

> Reinforcement learning with verifiers (RLVR) is a central paradigm for improving large language model (LLM) reasoning, yet existing methods often suffer from limited exploration. Policies tend to collapse onto a few reasoning patterns and prematurely stop deep exploration, while conventional entropy regularization introduces only local stochasticity and fails to induce meaningful path-level diversity, leading to weak and unstable learning signals in group-based policy optimization. We propose DSDR, a Dual-Scale Diversity Regularization reinforcement learning framework that decomposes diversity in LLM reasoning into global and coupling components. Globally, DSDR promotes diversity among correct reasoning trajectories to explore distinct solution modes. Locally, it applies a length-invariant, token-level entropy regularization restricted to correct trajectories, preventing entropy collapse within each mode while preserving correctness. The two scales are coupled through a global-to-local allocation mechanism that emphasizes local regularization for more distinctive correct trajectories. We provide theoretical support showing that DSDR preserves optimal correctness under bounded regularization, sustains informative learning signals in group-based optimization, and yields a principled global-to-local coupling rule. Experiments on multiple reasoning benchmarks demonstrate consistent improvements in accuracy and pass@k, highlighting the importance of dual-scale diversity for deep exploration in RLVR. Code is available at https://github.com/SUSTechBruce/DSDR.


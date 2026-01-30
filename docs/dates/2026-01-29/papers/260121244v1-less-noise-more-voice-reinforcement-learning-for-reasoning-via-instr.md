---
layout: default
title: Less Noise, More Voice: Reinforcement Learning for Reasoning via Instruction Purification
---

# Less Noise, More Voice: Reinforcement Learning for Reasoning via Instruction Purification
**arXiv**：[2601.21244v1](https://arxiv.org/abs/2601.21244) · [PDF](https://arxiv.org/pdf/2601.21244.pdf)  
**作者**：Yiju Guo, Tianyi Hu, Zexu Sun, Yankai Lin  

**一句话要点**：提出LENS框架，通过净化指令干扰提升强化学习在LLM推理中的效率

**关键词**：强化学习, 大语言模型推理, 指令净化, 探索效率, 干扰令牌

## 3 点简述
- 核心问题：RLVR在有限探索预算下因干扰令牌导致采样失败和训练不稳定
- 方法要点：先识别并移除干扰令牌进行净化，再转移成功探索监督策略优化
- 实验或效果：相比GRPO平均提升3.88%，加速超1.6倍，验证净化有效性

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has advanced LLM reasoning, but remains constrained by inefficient exploration under limited rollout budgets, leading to low sampling success and unstable training in complex tasks. We find that many exploration failures arise not from problem difficulty, but from a small number of prompt tokens that introduce interference. Building on this insight, we propose the Less Noise Sampling Framework (LENS), which first prompts by identifying and removing interference tokens. then transfers successful rollouts from the purification process to supervise policy optimization on the original noisy prompts, enabling the model to learn to ignore interference in the real-world, noisy prompting settings. Experimental results show that LENS significantly outperforms GRPO, delivering higher performance and faster convergence, with a 3.88% average gain and over 1.6$\times$ speedup. Our work highlights the critical role of pruning interference tokens in improving rollout efficiency, offering a new perspective for RLVR research.


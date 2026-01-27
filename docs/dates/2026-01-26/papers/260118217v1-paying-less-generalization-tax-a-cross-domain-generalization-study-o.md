---
layout: default
title: Paying Less Generalization Tax: A Cross-Domain Generalization Study of RL Training for LLM Agents
---

# Paying Less Generalization Tax: A Cross-Domain Generalization Study of RL Training for LLM Agents
**arXiv**：[2601.18217v1](https://arxiv.org/abs/2601.18217) · [PDF](https://arxiv.org/pdf/2601.18217.pdf)  
**作者**：Zhihan Liu, Lin Guan, Yixin Nie, Kai Zhang, Zhuoqun Hao, Lin Chen, Asli Celikyilmaz, Zhaoran Wang, Na Zhang  

**一句话要点**：提出状态随机化技术以提升LLM智能体在未知领域的跨域泛化能力

**关键词**：跨域泛化, 强化学习训练, 状态信息丰富度, LLM智能体, 随机化技术, 建模选择

## 3 点简述
- 核心问题：LLM智能体在未知测试域泛化性能受RL环境属性影响，而非域真实性或文本相似性
- 方法要点：通过增加状态信息丰富度（如添加无关特征）改善泛化，并分析建模选择如SFT预热和逐步思考的作用
- 实验或效果：在Sokoban和SciWorld等环境中验证状态丰富化有效，且建模选择影响泛化与遗忘平衡

## 摘要（原文）

> Generalist LLM agents are often post-trained on a narrow set of environments but deployed across far broader, unseen domains. In this work, we investigate the challenge of agentic post-training when the eventual test domains are unknown. Specifically, we analyze which properties of reinforcement learning (RL) environments and modeling choices have the greatest influence on out-of-domain performance. First, we identify two environment axes that strongly correlate with cross-domain generalization: (i) state information richness, i.e., the amount of information for the agent to process from the state, and (ii) planning complexity, estimated via goal reachability and trajectory length under a base policy. Notably, domain realism and text-level similarity are not the primary factors; for instance, the simple grid-world domain Sokoban leads to even stronger generalization in SciWorld than the more realistic ALFWorld. Motivated by these findings, we further show that increasing state information richness alone can already effectively improve cross-domain robustness. We propose a randomization technique, which is low-overhead and broadly applicable: add small amounts of distractive goal-irrelevant features to the state to make it richer without altering the task. Beyond environment-side properties, we also examine several modeling choices: (a) SFT warmup or mid-training helps prevent catastrophic forgetting during RL but undermines generalization to domains that are not included in the mid-training datamix; and (b) turning on step-by-step thinking during RL, while not always improving in-domain performance, plays a crucial role in preserving generalization.


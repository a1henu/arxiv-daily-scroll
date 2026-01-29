---
layout: default
title: Policy of Thoughts: Scaling LLM Reasoning via Test-time Policy Evolution
---

# Policy of Thoughts: Scaling LLM Reasoning via Test-time Policy Evolution
**arXiv**：[2601.20379v1](https://arxiv.org/abs/2601.20379) · [PDF](https://arxiv.org/pdf/2601.20379.pdf)  
**作者**：Zhengbo Jiao, Hongyu Xian, Qinglong Wang, Yunpu Ma, Zhebo Wang, Zifan Zhang, Dezhang Kong, Meng Han  

**一句话要点**：提出Policy of Thoughts框架，通过测试时策略演化提升大语言模型在复杂推理任务中的性能。

**关键词**：大语言模型推理, 测试时优化, 策略演化, LoRA适配器, 在线学习, 复杂任务性能

## 3 点简述
- 核心问题：大语言模型在复杂长程推理中因固定策略假设导致不稳定，现有方法未内部化执行反馈。
- 方法要点：引入Policy of Thoughts，基于探索生成候选解，使用Group Relative Policy Optimization更新LoRA适配器，实现实例级策略优化。
- 实验或效果：在LiveCodeBench上，4B模型准确率达49.71%，超越GPT-4o和DeepSeek-V3，模型规模小50倍以上。

## 摘要（原文）

> Large language models (LLMs) struggle with complex, long-horizon reasoning due to instability caused by their frozen policy assumption. Current test-time scaling methods treat execution feedback merely as an external signal for filtering or rewriting trajectories, without internalizing it to improve the underlying reasoning strategy. Inspired by Popper's epistemology of "conjectures and refutations," we argue that intelligence requires real-time evolution of the model's policy through learning from failed attempts. We introduce Policy of Thoughts (PoT), a framework that recasts reasoning as a within-instance online optimization process. PoT first generates diverse candidate solutions via an efficient exploration mechanism, then uses Group Relative Policy Optimization (GRPO) to update a transient LoRA adapter based on execution feedback. This closed-loop design enables dynamic, instance-specific refinement of the model's reasoning priors. Experiments show that PoT dramatically boosts performance: a 4B model achieves 49.71% accuracy on LiveCodeBench, outperforming GPT-4o and DeepSeek-V3 despite being over 50 smaller.


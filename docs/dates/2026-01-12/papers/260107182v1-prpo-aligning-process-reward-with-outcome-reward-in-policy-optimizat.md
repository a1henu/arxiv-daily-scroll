---
layout: default
title: PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization
---

# PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization
**arXiv**：[2601.07182v1](https://arxiv.org/abs/2601.07182) · [PDF](https://arxiv.org/pdf/2601.07182.pdf)  
**作者**：Ruiyi Ding, Yongxuan Lv, Xianhui Meng, Jiahe Song, Chao Wang, Chen Jiang, Yuan Cheng  

**一句话要点**：提出PRPO以结合过程奖励与结果奖励，解决大语言模型多步推理中的稀疏奖励问题。

**关键词**：过程奖励模型, 策略优化, 多步推理, 稀疏奖励, 无评论家方法

## 3 点简述
- 核心问题：大语言模型在多步推理任务中面临稀疏奖励信号，导致中间步骤指导不足。
- 方法要点：PRPO通过语义分割序列，将过程奖励模型分数归一化为令牌级优势，并与结果奖励对齐。
- 实验或效果：在MATH500上，PRPO仅用8次rollouts，将Qwen2.5-Math-1.5B准确率从61.2%提升至64.4%。

## 摘要（原文）

> Policy optimization for large language models often suffers from sparse reward signals in multi-step reasoning tasks. Critic-free methods like GRPO assign a single normalized outcome reward to all tokens, providing limited guidance for intermediate reasoning . While Process Reward Models (PRMs) offer dense feedback, they risk premature collapse when used alone, as early low-reward tokens can drive policies toward truncated outputs. We introduce Process Relative Policy Optimization (PRPO), which combines outcome reliability with process-level guidance in a critic-free framework. PRPO segments reasoning sequences based on semantic clues, normalizes PRM scores into token-level advantages, and aligns their distribution with outcome advantages through location-parameter shift. On MATH500, PRPO improves Qwen2.5-Math-1.5B accuracy from 61.2% to 64.4% over GRPO using only eight rollouts and no value network, demonstrating efficient fine-grained credit assignment within critic-free optimization.


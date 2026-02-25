---
layout: default
title: Why Pass@k Optimization Can Degrade Pass@1: Prompt Interference in LLM Post-training
---

# Why Pass@k Optimization Can Degrade Pass@1: Prompt Interference in LLM Post-training
**arXiv**：[2602.21189v1](https://arxiv.org/abs/2602.21189) · [PDF](https://arxiv.org/pdf/2602.21189.pdf)  
**作者**：Anas Barakat, Souradip Chakraborty, Khushbu Pahwa, Amrit Singh Bedi  

**一句话要点**：揭示Pass@k优化导致Pass@1下降的机制：提示干扰引发的梯度冲突

**关键词**：大语言模型后训练, 多样本推理优化, 梯度冲突, 提示干扰, 可验证任务评估

## 3 点简述
- 核心问题：Pass@k优化方法常导致Pass@1性能下降，影响单次推理的可靠性
- 方法要点：理论分析提示干扰如何通过梯度冲突使Pass@k更新方向偏离Pass@1
- 实验或效果：在可验证数学推理任务上通过大语言模型实验验证理论发现

## 摘要（原文）

> Pass@k is a widely used performance metric for verifiable large language model tasks, including mathematical reasoning, code generation, and short-answer reasoning. It defines success if any of $k$ independently sampled solutions passes a verifier. This multi-sample inference metric has motivated inference-aware fine-tuning methods that directly optimize pass@$k$. However, prior work reports a recurring trade-off: pass@k improves while pass@1 degrades under such methods. This trade-off is practically important because pass@1 often remains a hard operational constraint due to latency and cost budgets, imperfect verifier coverage, and the need for a reliable single-shot fallback. We study the origin of this trade-off and provide a theoretical characterization of when pass@k policy optimization can reduce pass@1 through gradient conflict induced by prompt interference. We show that pass@$k$ policy gradients can conflict with pass@1 gradients because pass@$k$ optimization implicitly reweights prompts toward low-success prompts; when these prompts are what we term negatively interfering, their upweighting can rotate the pass@k update direction away from the pass@1 direction. We illustrate our theoretical findings with large language model experiments on verifiable mathematical reasoning tasks.


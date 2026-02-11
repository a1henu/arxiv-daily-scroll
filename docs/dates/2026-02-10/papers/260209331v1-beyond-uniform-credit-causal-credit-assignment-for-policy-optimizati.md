---
layout: default
title: Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization
---

# Beyond Uniform Credit: Causal Credit Assignment for Policy Optimization
**arXiv**：[2602.09331v1](https://arxiv.org/abs/2602.09331) · [PDF](https://arxiv.org/pdf/2602.09331.pdf)  
**作者**：Mykola Khandoga, Rui Yuan, Vinay Kumar Sankarapu  

**一句话要点**：提出反事实重要性加权方法，解决语言模型推理中策略梯度信用分配不均问题

**关键词**：策略梯度方法, 信用分配, 反事实推理, 语言模型推理, 重要性加权, 数学推理

## 3 点简述
- 核心问题：现有策略梯度方法对生成的所有token分配均匀信用，导致无关文本与关键计算步骤获得相同梯度更新
- 方法要点：通过掩码推理片段并测量答案概率下降，直接根据策略模型自身概率变化估计token重要性，在策略梯度更新中相应加权
- 实验效果：在GSM8K数据集上对Qwen和Llama系列模型测试，相比均匀基线实现性能提升和更快收敛，分析确认方法能正确优先计算步骤

## 摘要（原文）

> Policy gradient methods for language model reasoning, such as GRPO and DAPO, assign uniform credit to all generated tokens - the filler phrase "Let me think" receives the same gradient update as the critical calculation "23 + 45 = 68." We propose counterfactual importance weighting: mask reasoning spans, measure the drop in answer probability, and upweight tokens accordingly during policy gradient updates. Our method requires no auxiliary models or external annotation, instead importance is estimated directly from the policy model's own probability shifts. Experiments on GSM8K across three models spanning the Qwen and Llama families demonstrate consistent improvements over uniform baselines and faster convergence to equivalent accuracy. Inverting the importance signal hurts performance, confirming we capture genuine causal structure rather than noise. Analysis shows the method correctly prioritizes calculation steps over scaffolding text. We view these findings as establishing counterfactual importance weighting as a foundation for further research rather than a complete solution.


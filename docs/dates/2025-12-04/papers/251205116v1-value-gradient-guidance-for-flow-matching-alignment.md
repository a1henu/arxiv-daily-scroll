---
layout: default
title: Value Gradient Guidance for Flow Matching Alignment
---

# Value Gradient Guidance for Flow Matching Alignment
**arXiv**：[2512.05116v1](https://arxiv.org/abs/2512.05116) · [PDF](https://arxiv.org/pdf/2512.05116.pdf)  
**作者**：Zhen Liu, Tim Z. Xiao, Carles Domingo-Enrich, Weiyang Liu, Dinghuai Zhang  

**一句话要点**：提出VGG-Flow方法，基于最优控制理论微调流匹配模型以实现高效对齐与先验保持

**关键词**：流匹配模型, 模型对齐, 最优控制, 微调方法, 价值函数, 生成模型

## 3 点简述
- 现有流匹配模型对齐方法在适应效率和先验保持上存在不足
- VGG-Flow通过匹配微调速度场与价值函数梯度场，结合奖励模型一阶信息
- 在Stable Diffusion 3上实验显示，该方法在有限计算预算下实现有效对齐

## 摘要（原文）

> While methods exist for aligning flow matching models--a popular and effective class of generative models--with human preferences, existing approaches fail to achieve both adaptation efficiency and probabilistically sound prior preservation. In this work, we leverage the theory of optimal control and propose VGG-Flow, a gradient-matching-based method for finetuning pretrained flow matching models. The key idea behind this algorithm is that the optimal difference between the finetuned velocity field and the pretrained one should be matched with the gradient field of a value function. This method not only incorporates first-order information from the reward model but also benefits from heuristic initialization of the value function to enable fast adaptation. Empirically, we show on a popular text-to-image flow matching model, Stable Diffusion 3, that our method can finetune flow matching models under limited computational budgets while achieving effective and prior-preserving alignment.


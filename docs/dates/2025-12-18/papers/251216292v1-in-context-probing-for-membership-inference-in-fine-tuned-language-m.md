---
layout: default
title: In-Context Probing for Membership Inference in Fine-Tuned Language Models
---

# In-Context Probing for Membership Inference in Fine-Tuned Language Models
**arXiv**：[2512.16292v1](https://arxiv.org/abs/2512.16292) · [PDF](https://arxiv.org/pdf/2512.16292.pdf)  
**作者**：Zhexi Lu, Hongliang Chi, Nathalie Baracaldo, Swanand Ravindra Kadhe, Yuseok Jeon, Lei Yu  

**一句话要点**：提出ICP-MIA框架，基于优化间隙理论，通过上下文探测实现微调语言模型的成员推断攻击。

**关键词**：成员推断攻击, 大语言模型, 隐私审计, 优化间隙, 上下文探测, 黑盒攻击

## 3 点简述
- 核心问题：传统黑盒成员推断攻击依赖置信度或似然度，信号易受样本内在属性干扰，导致泛化差和信噪比低。
- 方法要点：引入优化间隙作为成员信号，提出上下文探测方法，通过参考数据或自扰动模拟微调行为，无需训练。
- 实验或效果：在三个任务和多个大语言模型上，ICP-MIA显著优于先前黑盒攻击，尤其在低误报率下表现突出。

## 摘要（原文）

> Membership inference attacks (MIAs) pose a critical privacy threat to fine-tuned large language models (LLMs), especially when models are adapted to domain-specific tasks using sensitive data. While prior black-box MIA techniques rely on confidence scores or token likelihoods, these signals are often entangled with a sample's intrinsic properties - such as content difficulty or rarity - leading to poor generalization and low signal-to-noise ratios. In this paper, we propose ICP-MIA, a novel MIA framework grounded in the theory of training dynamics, particularly the phenomenon of diminishing returns during optimization. We introduce the Optimization Gap as a fundamental signal of membership: at convergence, member samples exhibit minimal remaining loss-reduction potential, while non-members retain significant potential for further optimization. To estimate this gap in a black-box setting, we propose In-Context Probing (ICP), a training-free method that simulates fine-tuning-like behavior via strategically constructed input contexts. We propose two probing strategies: reference-data-based (using semantically similar public samples) and self-perturbation (via masking or generation). Experiments on three tasks and multiple LLMs show that ICP-MIA significantly outperforms prior black-box MIAs, particularly at low false positive rates. We further analyze how reference data alignment, model type, PEFT configurations, and training schedules affect attack effectiveness. Our findings establish ICP-MIA as a practical and theoretically grounded framework for auditing privacy risks in deployed LLMs.


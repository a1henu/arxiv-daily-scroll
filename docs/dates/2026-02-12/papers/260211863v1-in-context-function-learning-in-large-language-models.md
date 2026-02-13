---
layout: default
title: In-Context Function Learning in Large Language Models
---

# In-Context Function Learning in Large Language Models
**arXiv**：[2602.11863v1](https://arxiv.org/abs/2602.11863) · [PDF](https://arxiv.org/pdf/2602.11863.pdf)  
**作者**：Elif Akata, Konstantinos Voudouris, Vincent Fortuin, Eric Schulz  

**一句话要点**：通过高斯过程框架量化大语言模型在上下文中的函数学习能力与归纳偏置

**关键词**：上下文学习, 高斯过程, 归纳偏置, 函数学习, 大语言模型, 样本效率

## 3 点简述
- 研究大语言模型在推理时从少量演示中学习连续函数的能力，以高斯过程为理论框架构建控制实验。
- 评估模型预测误差随演示数量变化，并与高斯过程回归下界和1-最近邻上界比较，分析模型规模与核函数影响。
- 通过似然分析揭示模型归纳偏置，并探索强化学习和监督微调如何调整偏置以提升样本效率。

## 摘要（原文）

> Large language models (LLMs) can learn from a few demonstrations provided at inference time. We study this in-context learning phenomenon through the lens of Gaussian Processes (GPs). We build controlled experiments where models observe sequences of multivariate scalar-valued function samples drawn from known GP priors. We evaluate prediction error in relation to the number of demonstrations and compare against two principled references: (i) an empirical GP-regression learner that gives a lower bound on achievable error, and (ii) the expected error of a 1-nearest-neighbor (1-NN) rule, which gives a data-driven upper bound. Across model sizes, we find that LLM learning curves are strongly influenced by the function-generating kernels and approach the GP lower bound as the number of demonstrations increases. We then study the inductive biases of these models using a likelihood-based analysis. We find that LLM predictions are most likely under less smooth GP kernels. Finally, we explore whether post-training can shift these inductive biases and improve sample-efficiency on functions sampled from GPs with smoother kernels. We find that both reinforcement learning and supervised fine-tuning can effectively shift inductive biases in the direction of the training data. Together, our framework quantifies the extent to which LLMs behave like GP learners and provides tools for steering their inductive biases for continuous function learning tasks.


---
layout: default
title: Learning Dynamics in RL Post-Training for Language Models
---

# Learning Dynamics in RL Post-Training for Language Models
**arXiv**：[2601.04670v1](https://arxiv.org/abs/2601.04670) · [PDF](https://arxiv.org/pdf/2601.04670.pdf)  
**作者**：Akiyoshi Tomihari  

**一句话要点**：提出分类器优先强化学习以分析语言模型RL后训练中的学习动态

**关键词**：强化学习后训练, 学习动态分析, 神经正切核, 输出多样性, 分类器优化, 语言模型对齐

## 3 点简述
- 核心问题：RL后训练中输出多样性降低现象缺乏理论解释
- 方法要点：采用经验神经正切核框架分解RL更新传播机制
- 实验或效果：CF-RL策略验证了模型置信度提升和优化加速

## 摘要（原文）

> Reinforcement learning (RL) post-training is a critical stage in modern language model development, playing a key role in improving alignment and reasoning ability. However, several phenomena remain poorly understood, including the reduction in output diversity. To gain a broader understanding of RL post-training, we analyze the learning dynamics of RL post-training from a perspective that has been studied in supervised learning but remains underexplored in RL. We adopt an empirical neural tangent kernel (NTK) framework and decompose the NTK into two components to characterize how RL updates propagate across training samples. Our analysis reveals that limited variability in feature representations can cause RL updates to systematically increase model confidence, providing an explanation for the commonly observed reduction in output diversity after RL post-training. Furthermore, we show that effective learning in this regime depends on rapidly shaping the classifier, which directly affects the gradient component of the NTK. Motivated by these insights, we propose classifier-first reinforcement learning (CF-RL), a simple two-stage training strategy that prioritizes classifier updates before standard RL optimization. Experimental results validate our theoretical analysis by demonstrating increased model confidence and accelerated optimization under CF-RL. Additional analysis shows that the mechanism underlying CF-RL differs from that of linear-probing-then-fine-tuning in supervised learning. Overall, our study formalizes the learning dynamics of RL post-training and motivates further analysis and improvement.


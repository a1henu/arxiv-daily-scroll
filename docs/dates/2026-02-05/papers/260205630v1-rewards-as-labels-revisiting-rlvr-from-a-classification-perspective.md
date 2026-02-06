---
layout: default
title: Rewards as Labels: Revisiting RLVR from a Classification Perspective
---

# Rewards as Labels: Revisiting RLVR from a Classification Perspective
**arXiv**：[2602.05630v1](https://arxiv.org/abs/2602.05630) · [PDF](https://arxiv.org/pdf/2602.05630.pdf)  
**作者**：Zepeng Zhai, Meilin Chen, Jiaxuan Zhao, Junlang Qian, Lei Shen, Yuan Lu  

**一句话要点**：提出REAL框架，将可验证奖励视为分类标签以解决强化学习中梯度分配问题，提升大语言模型推理性能。

**关键词**：强化学习, 可验证奖励, 分类视角, 梯度分配, 大语言模型, 数学推理

## 3 点简述
- 核心问题：RLVR方法如GRPO存在梯度误分配和梯度主导，导致策略更新低效。
- 方法要点：REAL将奖励重新定义为分类标签，引入锚定logits，将策略优化转化为分类问题。
- 实验或效果：在数学推理基准测试中，REAL稳定训练，性能优于GRPO和DAPO，模型规模扩展时增益持续。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards has recently advanced the capabilities of Large Language Models in complex reasoning tasks by providing explicit rule-based supervision. Among RLVR methods, GRPO and its variants have achieved strong empirical performance. Despite their success, we identify that they suffer from Gradient Misassignment in Positives and Gradient Domination in Negatives, which lead to inefficient and suboptimal policy updates. To address these issues, we propose Rewards as Labels (REAL), a novel framework that revisits verifiable rewards as categorical labels rather than scalar weights, thereby reformulating policy optimization as a classification problem. Building on this, we further introduce anchor logits to enhance policy learning. Our analysis reveals that REAL induces a monotonic and bounded gradient weighting, enabling balanced gradient allocation across rollouts and effectively mitigating the identified mismatches. Extensive experiments on mathematical reasoning benchmarks show that REAL improves training stability and consistently outperforms GRPO and strong variants such as DAPO. On the 1.5B model, REAL improves average Pass@1 over DAPO by 6.7%. These gains further scale to 7B model, REAL continues to outperform DAPO and GSPO by 6.2% and 1.7%, respectively. Notably, even with a vanilla binary cross-entropy, REAL remains stable and exceeds DAPO by 4.5% on average.


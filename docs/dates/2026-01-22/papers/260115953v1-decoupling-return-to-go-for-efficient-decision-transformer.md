---
layout: default
title: Decoupling Return-to-Go for Efficient Decision Transformer
---

# Decoupling Return-to-Go for Efficient Decision Transformer
**arXiv**：[2601.15953v1](https://arxiv.org/abs/2601.15953) · [PDF](https://arxiv.org/pdf/2601.15953.pdf)  
**作者**：Yongyi Wang, Hanyu Liu, Lingfeng Li, Bozhou Chen, Ang Li, Qirui Zheng, Xionghui Yang, Wenxin Li  

**一句话要点**：提出解耦决策变换器以解决离线强化学习中回报到目标冗余问题

**关键词**：离线强化学习, 决策变换器, 序列建模, 回报到目标, 计算效率

## 3 点简述
- 核心问题：决策变换器在训练和推理中全序列使用回报到目标，存在理论冗余，可能损害性能。
- 方法要点：设计解耦决策变换器，仅用观测和动作序列通过变换器，用最新回报到目标指导动作预测。
- 实验或效果：在多个离线强化学习任务中，解耦决策变换器显著优于原版，并减少计算成本。

## 摘要（原文）

> The Decision Transformer (DT) has established a powerful sequence modeling approach to offline reinforcement learning. It conditions its action predictions on Return-to-Go (RTG), using it both to distinguish trajectory quality during training and to guide action generation at inference. In this work, we identify a critical redundancy in this design: feeding the entire sequence of RTGs into the Transformer is theoretically unnecessary, as only the most recent RTG affects action prediction. We show that this redundancy can impair DT's performance through experiments. To resolve this, we propose the Decoupled DT (DDT). DDT simplifies the architecture by processing only observation and action sequences through the Transformer, using the latest RTG to guide the action prediction. This streamlined approach not only improves performance but also reduces computational cost. Our experiments show that DDT significantly outperforms DT and establishes competitive performance against state-of-the-art DT variants across multiple offline RL tasks.


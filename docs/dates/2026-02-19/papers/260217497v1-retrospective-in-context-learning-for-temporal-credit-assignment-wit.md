---
layout: default
title: Retrospective In-Context Learning for Temporal Credit Assignment with Large Language Models
---

# Retrospective In-Context Learning for Temporal Credit Assignment with Large Language Models
**arXiv**：[2602.17497v1](https://arxiv.org/abs/2602.17497) · [PDF](https://arxiv.org/pdf/2602.17497.pdf)  
**作者**：Wen-Tse Chen, Jiayu Chen, Fahim Tajwar, Hao Zhu, Xintong Duan, Ruslan Salakhutdinov, Jeff Schneider  

**一句话要点**：提出基于大语言模型的回顾式上下文学习，用于稀疏奖励下的时序信用分配，提升样本效率。

**关键词**：时序信用分配, 大语言模型, 回顾式上下文学习, 稀疏奖励, 样本效率, 在线强化学习

## 3 点简述
- 核心问题：稀疏环境反馈下，传统时序信用分配方法样本效率低、泛化能力有限。
- 方法要点：利用大语言模型预训练知识，通过回顾式上下文学习将稀疏奖励转化为密集优势函数。
- 实验或效果：在BabyAI场景中，RICOL框架实现与传统在线强化学习算法相当性能，样本效率显著更高。

## 摘要（原文）

> Learning from self-sampled data and sparse environmental feedback remains a fundamental challenge in training self-evolving agents. Temporal credit assignment mitigates this issue by transforming sparse feedback into dense supervision signals. However, previous approaches typically depend on learning task-specific value functions for credit assignment, which suffer from poor sample efficiency and limited generalization. In this work, we propose to leverage pretrained knowledge from large language models (LLMs) to transform sparse rewards into dense training signals (i.e., the advantage function) through retrospective in-context learning (RICL). We further propose an online learning framework, RICOL, which iteratively refines the policy based on the credit assignment results from RICL. We empirically demonstrate that RICL can accurately estimate the advantage function with limited samples and effectively identify critical states in the environment for temporal credit assignment. Extended evaluation on four BabyAI scenarios show that RICOL achieves comparable convergent performance with traditional online RL algorithms with significantly higher sample efficiency. Our findings highlight the potential of leveraging LLMs for temporal credit assignment, paving the way for more sample-efficient and generalizable RL paradigms.


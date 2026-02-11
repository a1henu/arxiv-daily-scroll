---
layout: default
title: Efficient Unsupervised Environment Design through Hierarchical Policy Representation Learning
---

# Efficient Unsupervised Environment Design through Hierarchical Policy Representation Learning
**arXiv**：[2602.09813v1](https://arxiv.org/abs/2602.09813) · [PDF](https://arxiv.org/pdf/2602.09813.pdf)  
**作者**：Dexun Li, Sidney Tio, Pradeep Varakantham  

**一句话要点**：提出分层MDP框架以解决资源受限下无监督环境设计的效率问题

**关键词**：无监督环境设计, 分层MDP, 策略表示学习, 生成模型, 资源受限学习

## 3 点简述
- 核心问题：资源受限场景中，无监督环境设计方法因师生交互机会有限而效率低下
- 方法要点：引入分层MDP框架，教师利用学生策略表示生成训练环境，结合生成模型减少交互需求
- 实验或效果：在多个领域实验中，方法优于基线，单次交互需求更少，适用于训练机会受限场景

## 摘要（原文）

> Unsupervised Environment Design (UED) has emerged as a promising approach to developing general-purpose agents through automated curriculum generation. Popular UED methods focus on Open-Endedness, where teacher algorithms rely on stochastic processes for infinite generation of useful environments. This assumption becomes impractical in resource-constrained scenarios where teacher-student interaction opportunities are limited. To address this challenge, we introduce a hierarchical Markov Decision Process (MDP) framework for environment design. Our framework features a teacher agent that leverages student policy representations derived from discovered evaluation environments, enabling it to generate training environments based on the student's capabilities. To improve efficiency, we incorporate a generative model that augments the teacher's training dataset with synthetic data, reducing the need for teacher-student interactions. In experiments across several domains, we show that our method outperforms baseline approaches while requiring fewer teacher-student interactions in a single episode. The results suggest the applicability of our approach in settings where training opportunities are limited.


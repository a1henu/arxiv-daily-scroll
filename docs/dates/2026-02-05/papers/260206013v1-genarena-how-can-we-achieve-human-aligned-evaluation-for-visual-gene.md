---
layout: default
title: GenArena: How Can We Achieve Human-Aligned Evaluation for Visual Generation Tasks?
---

# GenArena: How Can We Achieve Human-Aligned Evaluation for Visual Generation Tasks?
**arXiv**：[2602.06013v1](https://arxiv.org/abs/2602.06013) · [PDF](https://arxiv.org/pdf/2602.06013.pdf)  
**作者**：Ruihang Li, Leigang Qu, Jingxu Zhang, Dongnan Gui, Mengde Xu, Xiaosong Zhang, Han Hu, Wenjie Wang, Jiaqi Wang  

**一句话要点**：提出GenArena框架，通过成对比较范式解决视觉生成任务中传统评分标准与人类感知不一致的问题。

**关键词**：视觉生成评估, 成对比较, 人类对齐, 自动化基准, 视觉语言模型

## 3 点简述
- 核心问题：传统绝对点评分标准在视觉生成任务中存在随机不一致性和与人类感知对齐差的问题。
- 方法要点：引入GenArena，采用成对比较范式，确保稳定且与人类对齐的自动化评估。
- 实验或效果：成对协议使开源模型超越顶级专有模型，评估准确率提升超20%，与权威榜单相关性达0.86。

## 摘要（原文）

> The rapid advancement of visual generation models has outpaced traditional evaluation approaches, necessitating the adoption of Vision-Language Models as surrogate judges. In this work, we systematically investigate the reliability of the prevailing absolute pointwise scoring standard, across a wide spectrum of visual generation tasks. Our analysis reveals that this paradigm is limited due to stochastic inconsistency and poor alignment with human perception. To resolve these limitations, we introduce GenArena, a unified evaluation framework that leverages a pairwise comparison paradigm to ensure stable and human-aligned evaluation. Crucially, our experiments uncover a transformative finding that simply adopting this pairwise protocol enables off-the-shelf open-source models to outperform top-tier proprietary models. Notably, our method boosts evaluation accuracy by over 20% and achieves a Spearman correlation of 0.86 with the authoritative LMArena leaderboard, drastically surpassing the 0.36 correlation of pointwise methods. Based on GenArena, we benchmark state-of-the-art visual generation models across diverse tasks, providing the community with a rigorous and automated evaluation standard for visual generation.


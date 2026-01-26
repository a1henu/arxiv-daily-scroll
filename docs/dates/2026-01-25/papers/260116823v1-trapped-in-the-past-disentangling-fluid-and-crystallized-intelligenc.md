---
layout: default
title: Trapped in the past? Disentangling fluid and crystallized intelligence of large language models using chess
---

# Trapped in the past? Disentangling fluid and crystallized intelligence of large language models using chess
**arXiv**：[2601.16823v1](https://arxiv.org/abs/2601.16823) · [PDF](https://arxiv.org/pdf/2601.16823.pdf)  
**作者**：Leonard S. Pleiss, Maximilian Schiffer, Robert K. von Weizsäcker  

**一句话要点**：提出基于国际象棋的测试框架，以解耦大语言模型的流体与晶体智力

**关键词**：大语言模型评估, 流体智力, 晶体智力, 国际象棋测试, 分布外泛化, 推理增强

## 3 点简述
- 核心问题：大语言模型的能力源于记忆还是推理，需区分流体与晶体智力
- 方法要点：利用国际象棋构建可控测试集，基于训练语料接近度分类位置
- 实验或效果：性能随流体智力需求增加而下降，分布外任务表现接近随机

## 摘要（原文）

> Large Language Models (LLMs) exhibit remarkable capabilities, yet it remains unclear to what extent these reflect sophisticated recall (crystallized intelligence) or reasoning ability (fluid intelligence). We introduce chess as a controlled testbed for disentangling these faculties. Leveraging the game's structure and scalable engine evaluations, we construct a taxonomy of positions varying in training corpus proximity--ranging from common states solvable by memorization to novel ones requiring first-principles reasoning. We systematically evaluate multiple GPT generations under varying reasoning intensities. Our analysis reveals a clear gradient: performance consistently degrades as fluid intelligence demands increase. Notably, in out-of-distribution tasks, performance collapses to random levels. While newer models improve, progress slows significantly for tasks outside the training distribution. Furthermore, while reasoning-augmented inference improves performance, its marginal benefit per token decreases with distributional proximity. These results suggest current architectures remain limited in systematic generalization, highlighting the need for mechanisms beyond scale to achieve robust fluid intelligence.


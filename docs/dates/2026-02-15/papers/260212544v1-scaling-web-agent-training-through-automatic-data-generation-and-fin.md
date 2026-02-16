---
layout: default
title: Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation
---

# Scaling Web Agent Training through Automatic Data Generation and Fine-grained Evaluation
**arXiv**：[2602.12544v1](https://arxiv.org/abs/2602.12544) · [PDF](https://arxiv.org/pdf/2602.12544.pdf)  
**作者**：Lajanugen Logeswaran, Jaekyeom Kim, Sungryull Sohn, Creighton Glasscock, Honglak Lee  

**一句话要点**：提出基于约束的评估框架以自动生成高质量网络代理训练数据，提升复杂网络任务性能。

**关键词**：网络代理训练, 自动数据生成, 细粒度评估, 轨迹评估, 蒸馏模型, 复杂网络任务

## 3 点简述
- 核心问题：网络代理训练中高质量数据稀缺，轨迹评估困难，难以量化任务完成进度。
- 方法要点：引入基于约束的细粒度评估框架，利用部分成功轨迹扩展可用训练数据。
- 实验或效果：在BookingArena基准上，蒸馏学生模型优于开源方法，匹配或超越商业系统，模型更小。

## 摘要（原文）

> We present a scalable pipeline for automatically generating high-quality training data for web agents. In particular, a major challenge in identifying high-quality training instances is trajectory evaluation - quantifying how much progress was made towards task completion. We introduce a novel constraint-based evaluation framework that provides fine-grained assessment of progress towards task completion. This enables us to leverage partially successful trajectories, which significantly expands the amount of usable training data. We evaluate our method on a new benchmark we propose called BookingArena, which consists of complex booking tasks across 20 popular websites, and demonstrate that our distilled student model outperforms open-source approaches and matches or exceeds commercial systems, while being a significantly smaller model. Our work addresses the challenge of efficiently creating diverse, realistic web interaction datasets and provides a systematic evaluation methodology for complex structured web tasks.


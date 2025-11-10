---
layout: default
title: Dense Motion Captioning
---

# Dense Motion Captioning
**arXiv**：[2511.05369v1](https://arxiv.org/abs/2511.05369) · [PDF](https://arxiv.org/pdf/2511.05369.pdf)  
**作者**：Shiyao Xu, Benedetta Liberatori, Gül Varol, Paolo Rota  

**一句话要点**：提出Dense Motion Captioning任务和DEMO模型，以解决3D人体运动序列中动作的时序定位与描述问题。

**关键词**：3D人体运动理解, 时序动作定位, 密集运动描述, CompMo数据集, DEMO模型

## 3 点简述
- 核心问题：现有3D运动与语言集成研究多关注文本到运动生成，而运动理解任务相对未被充分探索。
- 方法要点：引入DEMO模型，结合大语言模型与简单运动适配器，生成时序锚定的密集描述。
- 实验或效果：在CompMo数据集和适应基准上，DEMO显著优于现有方法，为3D运动理解建立强基线。

## 摘要（原文）

> Recent advances in 3D human motion and language integration have primarily
> focused on text-to-motion generation, leaving the task of motion understanding
> relatively unexplored. We introduce Dense Motion Captioning, a novel task that
> aims to temporally localize and caption actions within 3D human motion
> sequences. Current datasets fall short in providing detailed temporal
> annotations and predominantly consist of short sequences featuring few actions.
> To overcome these limitations, we present the Complex Motion Dataset (CompMo),
> the first large-scale dataset featuring richly annotated, complex motion
> sequences with precise temporal boundaries. Built through a carefully designed
> data generation pipeline, CompMo includes 60,000 motion sequences, each
> composed of multiple actions ranging from at least two to ten, accurately
> annotated with their temporal extents. We further present DEMO, a model that
> integrates a large language model with a simple motion adapter, trained to
> generate dense, temporally grounded captions. Our experiments show that DEMO
> substantially outperforms existing methods on CompMo as well as on adapted
> benchmarks, establishing a robust baseline for future research in 3D motion
> understanding and captioning.


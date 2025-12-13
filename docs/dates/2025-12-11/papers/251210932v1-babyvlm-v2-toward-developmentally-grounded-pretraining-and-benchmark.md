---
layout: default
title: BabyVLM-V2: Toward Developmentally Grounded Pretraining and Benchmarking of Vision Foundation Models
---

# BabyVLM-V2: Toward Developmentally Grounded Pretraining and Benchmarking of Vision Foundation Models
**arXiv**：[2512.10932v1](https://arxiv.org/abs/2512.10932) · [PDF](https://arxiv.org/pdf/2512.10932.pdf)  
**作者**：Shengao Wang, Wenqi Wang, Zecheng Wang, Max Whitton, Michael Wakeham, Arjun Chandra, Joey Huang, Pengyue Zhu, Helen Chen, David Li, Jeffrey Li, Shawn Li, Andrew Zagula, Amy Zhao, Andrew Zhu, Sayaka Nakamura, Yuki Yamamoto, Jerry Jun Yokono, Aaron Mueller, Bryan A. Plummer, Kate Saenko, Venkatesh Saligrama, Boqing Gong  

**一句话要点**：提出BabyVLM-V2框架，基于儿童发展轨迹进行视觉基础模型预训练与评估。

**关键词**：视觉语言模型, 儿童发展预训练, 认知评估基准, 纵向视听数据, 样本高效学习

## 3 点简述
- 核心问题：早期儿童发展轨迹为样本高效预训练视觉基础模型提供自然目标。
- 方法要点：使用纵向婴儿中心视听语料库预训练，并开发DevCV Toolbox进行认知评估。
- 实验或效果：紧凑模型在DevCV Toolbox上表现竞争性，部分任务超越GPT-4o。

## 摘要（原文）

> Early children's developmental trajectories set up a natural goal for sample-efficient pretraining of vision foundation models. We introduce BabyVLM-V2, a developmentally grounded framework for infant-inspired vision-language modeling that extensively improves upon BabyVLM-V1 through a longitudinal, multifaceted pretraining set, a versatile model, and, most importantly, DevCV Toolbox for cognitive evaluation. The pretraining set maximizes coverage while minimizing curation of a longitudinal, infant-centric audiovisual corpus, yielding video-utterance, image-utterance, and multi-turn conversational data that mirror infant experiences. DevCV Toolbox adapts all vision-related measures of the recently released NIH Baby Toolbox into a benchmark suite of ten multimodal tasks, covering spatial reasoning, memory, and vocabulary understanding aligned with early children's capabilities. Experimental results show that a compact model pretrained from scratch can achieve competitive performance on DevCV Toolbox, outperforming GPT-4o on some tasks. We hope the principled, unified BabyVLM-V2 framework will accelerate research in developmentally plausible pretraining of vision foundation models.


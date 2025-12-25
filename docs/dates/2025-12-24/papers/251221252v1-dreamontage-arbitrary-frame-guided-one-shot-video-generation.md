---
layout: default
title: DreaMontage: Arbitrary Frame-Guided One-Shot Video Generation
---

# DreaMontage: Arbitrary Frame-Guided One-Shot Video Generation
**arXiv**：[2512.21252v1](https://arxiv.org/abs/2512.21252) · [PDF](https://arxiv.org/pdf/2512.21252.pdf)  
**作者**：Jiawei Liu, Junqiao Li, Jiangfan Deng, Gen Li, Siyu Zhou, Zetao Fang, Shanshan Lao, Zengde Deng, Jianing Zhu, Tingting Ma, Jiayi Li, Yunqiu Wang, Qian He, Xinglong Wu  

**一句话要点**：提出DreaMontage框架，通过任意帧引导生成解决一镜到底视频制作中的视觉平滑与连贯性问题

**关键词**：一镜到底视频生成, 任意帧引导, DiT架构, 自适应调优, 分段自回归推理, 视觉表达微调

## 3 点简述
- 核心问题：现有视频生成模型依赖简单片段拼接，难以保持视觉平滑与时间连贯性
- 方法要点：在DiT架构中集成轻量级中间条件机制，采用自适应调优策略实现任意帧控制
- 实验效果：通过高质量数据集、视觉表达微调和分段自回归推理，生成视觉震撼且连贯的一镜到底视频

## 摘要（原文）

> The "one-shot" technique represents a distinct and sophisticated aesthetic in filmmaking. However, its practical realization is often hindered by prohibitive costs and complex real-world constraints. Although emerging video generation models offer a virtual alternative, existing approaches typically rely on naive clip concatenation, which frequently fails to maintain visual smoothness and temporal coherence. In this paper, we introduce DreaMontage, a comprehensive framework designed for arbitrary frame-guided generation, capable of synthesizing seamless, expressive, and long-duration one-shot videos from diverse user-provided inputs. To achieve this, we address the challenge through three primary dimensions. (i) We integrate a lightweight intermediate-conditioning mechanism into the DiT architecture. By employing an Adaptive Tuning strategy that effectively leverages base training data, we unlock robust arbitrary-frame control capabilities. (ii) To enhance visual fidelity and cinematic expressiveness, we curate a high-quality dataset and implement a Visual Expression SFT stage. In addressing critical issues such as subject motion rationality and transition smoothness, we apply a Tailored DPO scheme, which significantly improves the success rate and usability of the generated content. (iii) To facilitate the production of extended sequences, we design a Segment-wise Auto-Regressive (SAR) inference strategy that operates in a memory-efficient manner. Extensive experiments demonstrate that our approach achieves visually striking and seamlessly coherent one-shot effects while maintaining computational efficiency, empowering users to transform fragmented visual materials into vivid, cohesive one-shot cinematic experiences.


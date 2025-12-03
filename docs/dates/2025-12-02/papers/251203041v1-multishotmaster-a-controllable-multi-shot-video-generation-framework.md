---
layout: default
title: MultiShotMaster: A Controllable Multi-Shot Video Generation Framework
---

# MultiShotMaster: A Controllable Multi-Shot Video Generation Framework
**arXiv**：[2512.03041v1](https://arxiv.org/abs/2512.03041) · [PDF](https://arxiv.org/pdf/2512.03041.pdf)  
**作者**：Qinghe Wang, Xiaoyu Shi, Baolu Li, Weikang Bian, Quande Liu, Huchuan Lu, Xintao Wang, Pengfei Wan, Kun Gai, Xu Jia  

**一句话要点**：提出MultiShotMaster框架以解决可控多镜头视频生成问题

**关键词**：多镜头视频生成, 可控视频生成, RoPE变体, 时空位置感知, 自动化数据标注, 叙事连贯性

## 3 点简述
- 核心问题：现有视频生成技术难以生成叙事连贯、镜头安排灵活的多镜头视频
- 方法要点：扩展预训练单镜头模型，引入多镜头叙事RoPE和时空位置感知RoPE变体
- 实验或效果：通过自动化数据标注和实验验证了框架的优越性能和可控性

## 摘要（原文）

> Current video generation techniques excel at single-shot clips but struggle to produce narrative multi-shot videos, which require flexible shot arrangement, coherent narrative, and controllability beyond text prompts. To tackle these challenges, we propose MultiShotMaster, a framework for highly controllable multi-shot video generation. We extend a pretrained single-shot model by integrating two novel variants of RoPE. First, we introduce Multi-Shot Narrative RoPE, which applies explicit phase shift at shot transitions, enabling flexible shot arrangement while preserving the temporal narrative order. Second, we design Spatiotemporal Position-Aware RoPE to incorporate reference tokens and grounding signals, enabling spatiotemporal-grounded reference injection. In addition, to overcome data scarcity, we establish an automated data annotation pipeline to extract multi-shot videos, captions, cross-shot grounding signals and reference images. Our framework leverages the intrinsic architectural properties to support multi-shot video generation, featuring text-driven inter-shot consistency, customized subject with motion control, and background-driven customized scene. Both shot count and duration are flexibly configurable. Extensive experiments demonstrate the superior performance and outstanding controllability of our framework.


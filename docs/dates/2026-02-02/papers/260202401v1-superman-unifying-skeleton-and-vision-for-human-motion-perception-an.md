---
layout: default
title: Superman: Unifying Skeleton and Vision for Human Motion Perception and Generation
---

# Superman: Unifying Skeleton and Vision for Human Motion Perception and Generation
**arXiv**：[2602.02401v1](https://arxiv.org/abs/2602.02401) · [PDF](https://arxiv.org/pdf/2602.02401.pdf)  
**作者**：Xinshun Wang, Peiming Li, Ziyi Wang, Zhongbin Fang, Zhichao Deng, Songtao Wu, Jason Li, Mengyuan Liu  

**一句话要点**：提出Superman框架，通过视觉引导运动分词器和统一MLLM，解决运动感知与生成任务碎片化问题。

**关键词**：运动感知, 运动生成, 跨模态学习, 骨架数据, 视觉引导分词器, 统一MLLM

## 3 点简述
- 核心问题：运动分析领域存在感知与生成模型割裂、生成模型局限于静态姿态、运动词汇仅基于骨架数据等问题。
- 方法要点：引入视觉引导运动分词器，从视觉和骨架数据联合学习，构建跨模态运动词汇；基于此训练统一MLLM，处理多种时序任务。
- 实验或效果：在Human3.6M等基准测试中，实现所有运动任务的先进或竞争性能，展示高效可扩展性。

## 摘要（原文）

> Human motion analysis tasks, such as temporal 3D pose estimation, motion prediction, and motion in-betweening, play an essential role in computer vision. However, current paradigms suffer from severe fragmentation. First, the field is split between ``perception'' models that understand motion from video but only output text, and ``generation'' models that cannot perceive from raw visual input. Second, generative MLLMs are often limited to single-frame, static poses using dense, parametric SMPL models, failing to handle temporal motion. Third, existing motion vocabularies are built from skeleton data alone, severing the link to the visual domain. To address these challenges, we introduce Superman, a unified framework that bridges visual perception with temporal, skeleton-based motion generation. Our solution is twofold. First, to overcome the modality disconnect, we propose a Vision-Guided Motion Tokenizer. Leveraging the natural geometric alignment between 3D skeletons and visual data, this module pioneers robust joint learning from both modalities, creating a unified, cross-modal motion vocabulary. Second, grounded in this motion language, a single, unified MLLM architecture is trained to handle all tasks. This module flexibly processes diverse, temporal inputs, unifying 3D skeleton pose estimation from video (perception) with skeleton-based motion prediction and in-betweening (generation). Extensive experiments on standard benchmarks, including Human3.6M, demonstrate that our unified method achieves state-of-the-art or competitive performance across all motion tasks. This showcases a more efficient and scalable path for generative motion analysis using skeletons.


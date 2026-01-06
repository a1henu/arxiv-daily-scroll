---
layout: default
title: Talk2Move: Reinforcement Learning for Text-Instructed Object-Level Geometric Transformation in Scenes
---

# Talk2Move: Reinforcement Learning for Text-Instructed Object-Level Geometric Transformation in Scenes
**arXiv**：[2601.02356v1](https://arxiv.org/abs/2601.02356) · [PDF](https://arxiv.org/pdf/2601.02356.pdf)  
**作者**：Jing Tan, Zhaoyang Zhang, Yantao Shen, Jiarui Cai, Shuo Yang, Jiajun Wu, Wei Xia, Zhuowen Tu, Stefano Soatto  

**一句话要点**：提出Talk2Move强化学习扩散框架，以解决文本指令下场景中对象几何变换的挑战。

**关键词**：强化学习, 扩散模型, 文本引导编辑, 几何变换, 场景理解, 空间奖励

## 3 点简述
- 核心问题：现有文本引导方法难以实现对象级几何变换，如平移、旋转或缩放，因缺乏配对监督和像素级优化限制。
- 方法要点：采用Group Relative Policy Optimization探索几何动作，无需配对数据；设计空间奖励模型对齐变换与语言描述，提升学习效率。
- 实验或效果：在基准测试中，Talk2Move实现精确、一致且语义忠实的对象变换，在空间准确性和场景连贯性上优于现有方法。

## 摘要（原文）

> We introduce Talk2Move, a reinforcement learning (RL) based diffusion framework for text-instructed spatial transformation of objects within scenes. Spatially manipulating objects in a scene through natural language poses a challenge for multimodal generation systems. While existing text-based manipulation methods can adjust appearance or style, they struggle to perform object-level geometric transformations-such as translating, rotating, or resizing objects-due to scarce paired supervision and pixel-level optimization limits. Talk2Move employs Group Relative Policy Optimization (GRPO) to explore geometric actions through diverse rollouts generated from input images and lightweight textual variations, removing the need for costly paired data. A spatial reward guided model aligns geometric transformations with linguistic description, while off-policy step evaluation and active step sampling improve learning efficiency by focusing on informative transformation stages. Furthermore, we design object-centric spatial rewards that evaluate displacement, rotation, and scaling behaviors directly, enabling interpretable and coherent transformations. Experiments on curated benchmarks demonstrate that Talk2Move achieves precise, consistent, and semantically faithful object transformations, outperforming existing text-guided editing approaches in both spatial accuracy and scene coherence.


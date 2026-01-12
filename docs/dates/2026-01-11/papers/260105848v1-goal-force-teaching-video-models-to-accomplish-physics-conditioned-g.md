---
layout: default
title: Goal Force: Teaching Video Models To Accomplish Physics-Conditioned Goals
---

# Goal Force: Teaching Video Models To Accomplish Physics-Conditioned Goals
**arXiv**：[2601.05848v1](https://arxiv.org/abs/2601.05848) · [PDF](https://arxiv.org/pdf/2601.05848.pdf)  
**作者**：Nate Gillman, Yinghua Zhou, Zitian Tang, Evan Luo, Arjan Chakravarthy, Daksh Aggarwal, Michael Freeman, Charles Herrmann, Chen Sun  

**一句话要点**：提出Goal Force框架，通过力向量定义目标，训练视频生成模型实现物理感知规划。

**关键词**：视频生成, 物理建模, 零样本泛化, 目标指定, 因果推理, 神经网络模拟器

## 3 点简述
- 核心问题：视频生成模型难以用文本或图像指定精确物理目标。
- 方法要点：使用合成因果原语数据集，训练模型传播力向量以模拟物理交互。
- 实验或效果：模型在零样本下泛化至复杂真实场景，如工具操作和多对象因果链。

## 摘要（原文）

> Recent advancements in video generation have enabled the development of ``world models'' capable of simulating potential futures for robotics and planning. However, specifying precise goals for these models remains a challenge; text instructions are often too abstract to capture physical nuances, while target images are frequently infeasible to specify for dynamic tasks. To address this, we introduce Goal Force, a novel framework that allows users to define goals via explicit force vectors and intermediate dynamics, mirroring how humans conceptualize physical tasks. We train a video generation model on a curated dataset of synthetic causal primitives-such as elastic collisions and falling dominos-teaching it to propagate forces through time and space. Despite being trained on simple physics data, our model exhibits remarkable zero-shot generalization to complex, real-world scenarios, including tool manipulation and multi-object causal chains. Our results suggest that by grounding video generation in fundamental physical interactions, models can emerge as implicit neural physics simulators, enabling precise, physics-aware planning without reliance on external engines. We release all datasets, code, model weights, and interactive video demos at our project page.


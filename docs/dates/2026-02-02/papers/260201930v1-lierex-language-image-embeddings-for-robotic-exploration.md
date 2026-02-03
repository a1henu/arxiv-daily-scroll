---
layout: default
title: LIEREx: Language-Image Embeddings for Robotic Exploration
---

# LIEREx: Language-Image Embeddings for Robotic Exploration
**arXiv**：[2602.01930v1](https://arxiv.org/abs/2602.01930) · [PDF](https://arxiv.org/pdf/2602.01930.pdf)  
**作者**：Felix Igelbrink, Lennart Niecksch, Marian Renz, Martin Günther, Martin Atzmueller  

**一句话要点**：提出LIEREx方法，集成视觉语言基础模型与3D语义场景图，以支持自主机器人在部分未知环境中的目标导向探索。

**关键词**：视觉语言基础模型, 3D语义场景图, 机器人探索, 开放集映射, 目标导向探索

## 3 点简述
- 核心问题：传统语义地图依赖预定义词汇，难以处理设计时未定义的知识，限制了机器人在开放环境中的探索能力。
- 方法要点：利用CLIP等视觉语言基础模型，将对象编码为高维嵌入而非固定标签，实现开放集映射，并与3D语义场景图结合。
- 实验或效果：未知。

## 摘要（原文）

> Semantic maps allow a robot to reason about its surroundings to fulfill tasks such as navigating known environments, finding specific objects, and exploring unmapped areas. Traditional mapping approaches provide accurate geometric representations but are often constrained by pre-designed symbolic vocabularies. The reliance on fixed object classes makes it impractical to handle out-of-distribution knowledge not defined at design time. Recent advances in Vision-Language Foundation Models, such as CLIP, enable open-set mapping, where objects are encoded as high-dimensional embeddings rather than fixed labels. In LIEREx, we integrate these VLFMs with established 3D Semantic Scene Graphs to enable target-directed exploration by an autonomous agent in partially unknown environments.


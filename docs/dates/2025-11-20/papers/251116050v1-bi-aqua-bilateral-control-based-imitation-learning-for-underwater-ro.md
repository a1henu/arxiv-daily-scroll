---
layout: default
title: Bi-AQUA: Bilateral Control-Based Imitation Learning for Underwater Robot Arms via Lighting-Aware Action Chunking with Transformers
---

# Bi-AQUA: Bilateral Control-Based Imitation Learning for Underwater Robot Arms via Lighting-Aware Action Chunking with Transformers
**arXiv**：[2511.16050v1](https://arxiv.org/abs/2511.16050) · [PDF](https://arxiv.org/pdf/2511.16050.pdf)  
**作者**：Takeru Tsunoori, Masato Kobayashi, Yuki Uranishi  

**一句话要点**：提出Bi-AQUA框架以解决水下机器人手臂在极端光照下的操作问题

**关键词**：水下机器人操作, 模仿学习, 双边控制, 光照适应, Transformer模型

## 3 点简述
- 核心问题：水下操作面临光照变化、颜色失真和低可见度挑战
- 方法要点：集成三层光照适应机制，包括光照编码、FiLM调制和光照令牌
- 实验或效果：在真实水下拾放任务中，性能优于无光照建模基线，组件关键性得到验证

## 摘要（原文）

> Underwater robotic manipulation is fundamentally challenged by extreme lighting variations, color distortion, and reduced visibility. We introduce Bi-AQUA, the first underwater bilateral control-based imitation learning framework that integrates lighting-aware visual processing for underwater robot arms. Bi-AQUA employs a hierarchical three-level lighting adaptation mechanism: a Lighting Encoder that extracts lighting representations from RGB images without manual annotation and is implicitly supervised by the imitation objective, FiLM modulation of visual backbone features for adaptive, lighting-aware feature extraction, and an explicit lighting token added to the transformer encoder input for task-aware conditioning. Experiments on a real-world underwater pick-and-place task under diverse static and dynamic lighting conditions show that Bi-AQUA achieves robust performance and substantially outperforms a bilateral baseline without lighting modeling. Ablation studies further confirm that all three lighting-aware components are critical. This work bridges terrestrial bilateral control-based imitation learning and underwater manipulation, enabling force-sensitive autonomous operation in challenging marine environments. For additional material, please check: https://mertcookimg.github.io/bi-aqua


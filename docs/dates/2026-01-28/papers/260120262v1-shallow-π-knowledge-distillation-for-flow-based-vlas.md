---
layout: default
title: Shallow-π: Knowledge Distillation for Flow-based VLAs
---

# Shallow-π: Knowledge Distillation for Flow-based VLAs
**arXiv**：[2601.20262v1](https://arxiv.org/abs/2601.20262) · [PDF](https://arxiv.org/pdf/2601.20262.pdf)  
**作者**：Boseong Jeon, Yunho Choi, Taehan Kim  

**一句话要点**：提出Shallow-π知识蒸馏框架，压缩基于流的VLA模型深度以实现实时机器人部署。

**关键词**：知识蒸馏, 视觉-语言-动作模型, 模型压缩, 实时推理, 机器人操作, Transformer层减少

## 3 点简述
- 核心问题：基于流的VLA模型在实时机器人部署中深度压缩未受系统研究，影响推理效率。
- 方法要点：通过知识蒸馏将模型从18层压缩至6层，减少VLM骨干和动作头的Transformer深度。
- 实验或效果：在标准操作基准上实现推理速度提升两倍以上，成功率下降小于1%，并在工业级机器人平台验证。

## 摘要（原文）

> The growing demand for real-time robotic deployment necessitates fast and on-device inference for vision-language-action (VLA) models. Within the VLA literature, efficiency has been extensively studied at the token level, such as visual token pruning. In contrast, systematic transformer layer reduction has received limited attention and, to the best of our knowledge, has not been explored for flow-based VLA models under knowledge distillation. In this work, we propose Shallow-pi, a principled knowledge distillation framework that aggressively reduces the transformer depth of both the VLM backbone and the flow-based action head, compressing the model from 18 to 6 layers. Shallow-pi achieves over two times faster inference with less than one percent absolute drop in success rate on standard manipulation benchmarks, establishing state-of-the-art performance among reduced VLA models. Crucially, we validate our approach through industrial-scale real-world experiments on Jetson Orin and Jetson Thor across multiple robot platforms, including humanoid systems, in complex and dynamic manipulation scenarios.


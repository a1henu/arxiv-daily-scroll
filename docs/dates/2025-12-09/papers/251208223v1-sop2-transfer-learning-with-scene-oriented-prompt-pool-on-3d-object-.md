---
layout: default
title: SOP^2: Transfer Learning with Scene-Oriented Prompt Pool on 3D Object Detection
---

# SOP^2: Transfer Learning with Scene-Oriented Prompt Pool on 3D Object Detection
**arXiv**：[2512.08223v1](https://arxiv.org/abs/2512.08223) · [PDF](https://arxiv.org/pdf/2512.08223.pdf)  
**作者**：Ching-Hung Cheng, Hsiu-Fu Wu, Bing-Chen Wu, Khanh-Phong Bui, Van-Tin Luu, Ching-Chun Huang  

**一句话要点**：提出场景导向提示池以提升3D目标检测的迁移学习效果

**关键词**：3D目标检测, 迁移学习, 提示调优, 场景导向提示池, 基础模型

## 3 点简述
- 核心问题：探索提示调优在3D目标检测中的有效性，验证基础模型跨场景适应能力
- 方法要点：研究提示令牌和提示生成器影响，并设计场景导向提示池（SOP^2）
- 实验或效果：在Waymo数据集上验证提示池的有效性，旨在激发3D领域提示潜力研究

## 摘要（原文）

> With the rise of Large Language Models (LLMs) such as GPT-3, these models exhibit strong generalization capabilities. Through transfer learning techniques such as fine-tuning and prompt tuning, they can be adapted to various downstream tasks with minimal parameter adjustments. This approach is particularly common in the field of Natural Language Processing (NLP). This paper aims to explore the effectiveness of common prompt tuning methods in 3D object detection. We investigate whether a model trained on the large-scale Waymo dataset can serve as a foundation model and adapt to other scenarios within the 3D object detection field. This paper sequentially examines the impact of prompt tokens and prompt generators, and further proposes a Scene-Oriented Prompt Pool (\textbf{SOP$^2$}). We demonstrate the effectiveness of prompt pools in 3D object detection, with the goal of inspiring future researchers to delve deeper into the potential of prompts in the 3D field.


---
layout: default
title: Cross-modal Identity Mapping: Minimizing Information Loss in Modality Conversion via Reinforcement Learning
---

# Cross-modal Identity Mapping: Minimizing Information Loss in Modality Conversion via Reinforcement Learning
**arXiv**：[2603.01696v1](https://arxiv.org/abs/2603.01696) · [PDF](https://arxiv.org/pdf/2603.01696.pdf)  
**作者**：Haonan Jia, Shichao Dong, Xin Dong, Zenghui Sun, Jin Wang, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Kaifu Zhang  

**一句话要点**：提出跨模态身份映射框架，通过强化学习减少视觉语言模型在图像描述生成中的信息损失。

**关键词**：跨模态学习, 图像描述生成, 强化学习, 信息损失最小化, 视觉语言模型

## 3 点简述
- 核心问题：视觉语言模型在图像描述生成中常忽略或误传关键视觉内容，导致信息损失。
- 方法要点：基于文本搜索检索图像相似性评估信息损失，设计强化学习框架优化描述生成。
- 实验或效果：在COCO-LN500基准上，Qwen2.5-VL-7B模型的关系推理能力提升20%。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) often omit or misrepresent critical visual content in generated image captions. Minimizing such information loss will force LVLMs to focus on image details to generate precise descriptions. However, measuring information loss during modality conversion is inherently challenging due to the modal gap between visual content and text output. In this paper, we argue that the quality of an image caption is positively correlated with the similarity between images retrieved via text search using that caption. Based on this insight, we further propose Cross-modal Identity Mapping (CIM), a reinforcement learning framework that enhances image captioning without requiring additional annotations. Specifically, the method quantitatively evaluates the information loss from two perspectives: Gallery Representation Consistency and Query-gallery Image Relevance. Supervised under these metrics, LVLM minimizes information loss and aims to achieve identity mapping from images to captions. The experimental results demonstrate the superior performance of our method in image captioning, even when compared with Supervised Fine-Tuning. Particularly, on the COCO-LN500 benchmark, CIM achieves a 20% improvement in relation reasoning on Qwen2.5-VL-7B.The code will be released when the paper is accepted.


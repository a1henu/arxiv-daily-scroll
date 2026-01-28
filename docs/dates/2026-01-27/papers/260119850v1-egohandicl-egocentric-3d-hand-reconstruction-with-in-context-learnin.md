---
layout: default
title: EgoHandICL: Egocentric 3D Hand Reconstruction with In-Context Learning
---

# EgoHandICL: Egocentric 3D Hand Reconstruction with In-Context Learning
**arXiv**：[2601.19850v1](https://arxiv.org/abs/2601.19850) · [PDF](https://arxiv.org/pdf/2601.19850.pdf)  
**作者**：Binzhu Xie, Shi Qiu, Sicheng Zhang, Yinqiao Wang, Hao Xu, Muzammal Naseer, Chi-Wing Fu, Pheng-Ann Heng  

**一句话要点**：提出EgoHandICL框架，通过情境学习解决第一人称视角下3D手部重建的深度模糊和遮挡问题。

**关键词**：第一人称视角, 3D手部重建, 情境学习, 视觉语言模型, 掩码自编码器, 手物交互

## 3 点简述
- 核心问题：第一人称视角下3D手部重建面临深度模糊、自遮挡和复杂手物交互挑战。
- 方法要点：引入基于视觉语言模型的互补示例检索、情境学习定制化分词器和掩码自编码器架构。
- 实验或效果：在ARCTIC和EgoExo4D数据集上优于现有方法，并提升EgoVLM的手物交互推理能力。

## 摘要（原文）

> Robust 3D hand reconstruction in egocentric vision is challenging due to depth ambiguity, self-occlusion, and complex hand-object interactions. Prior methods mitigate these issues by scaling training data or adding auxiliary cues, but they often struggle in unseen contexts. We present EgoHandICL, the first in-context learning (ICL) framework for 3D hand reconstruction that improves semantic alignment, visual consistency, and robustness under challenging egocentric conditions. EgoHandICL introduces complementary exemplar retrieval guided by vision-language models (VLMs), an ICL-tailored tokenizer for multimodal context, and a masked autoencoder (MAE)-based architecture trained with hand-guided geometric and perceptual objectives. Experiments on ARCTIC and EgoExo4D show consistent gains over state-of-the-art methods. We also demonstrate real-world generalization and improve EgoVLM hand-object interaction reasoning by using reconstructed hands as visual prompts. Code and data: https://github.com/Nicous20/EgoHandICL


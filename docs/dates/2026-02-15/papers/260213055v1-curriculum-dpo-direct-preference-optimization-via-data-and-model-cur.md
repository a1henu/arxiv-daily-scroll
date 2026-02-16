---
layout: default
title: Curriculum-DPO++: Direct Preference Optimization via Data and Model Curricula for Text-to-Image Generation
---

# Curriculum-DPO++: Direct Preference Optimization via Data and Model Curricula for Text-to-Image Generation
**arXiv**：[2602.13055v1](https://arxiv.org/abs/2602.13055) · [PDF](https://arxiv.org/pdf/2602.13055.pdf)  
**作者**：Florinel-Alin Croitoru, Vlad Hondru, Radu Tudor Ionescu, Nicu Sebe, Mubarak Shah  

**一句话要点**：提出Curriculum-DPO++，通过数据和模型课程优化文本到图像生成的偏好学习。

**关键词**：文本到图像生成, 直接偏好优化, 课程学习, 低秩适应, 模型容量动态调整, 人类反馈学习

## 3 点简述
- 核心问题：现有偏好优化方法未考虑学习难度差异，导致优化过程不理想。
- 方法要点：结合数据级课程和模型级课程，动态增加去噪网络的学习容量。
- 实验或效果：在九个基准测试中优于其他方法，提升文本对齐、美学和人类偏好。

## 摘要（原文）

> Direct Preference Optimization (DPO) has been proposed as an effective and efficient alternative to reinforcement learning from human feedback (RLHF). However, neither RLHF nor DPO take into account the fact that learning certain preferences is more difficult than learning other preferences, rendering the optimization process suboptimal. To address this gap in text-to-image generation, we recently proposed Curriculum-DPO, a method that organizes image pairs by difficulty. In this paper, we introduce Curriculum-DPO++, an enhanced method that combines the original data-level curriculum with a novel model-level curriculum. More precisely, we propose to dynamically increase the learning capacity of the denoising network as training advances. We implement this capacity increase via two mechanisms. First, we initialize the model with only a subset of the trainable layers used in the original Curriculum-DPO. As training progresses, we sequentially unfreeze layers until the configuration matches the full baseline architecture. Second, as the fine-tuning is based on Low-Rank Adaptation (LoRA), we implement a progressive schedule for the dimension of the low-rank matrices. Instead of maintaining a fixed capacity, we initialize the low-rank matrices with a dimension significantly smaller than that of the baseline. As training proceeds, we incrementally increase their rank, allowing the capacity to grow until it converges to the same rank value as in Curriculum-DPO. Furthermore, we propose an alternative ranking strategy to the one employed by Curriculum-DPO. Finally, we compare Curriculum-DPO++ against Curriculum-DPO and other state-of-the-art preference optimization approaches on nine benchmarks, outperforming the competing methods in terms of text alignment, aesthetics and human preference. Our code is available at https://github.com/CroitoruAlin/Curriculum-DPO.


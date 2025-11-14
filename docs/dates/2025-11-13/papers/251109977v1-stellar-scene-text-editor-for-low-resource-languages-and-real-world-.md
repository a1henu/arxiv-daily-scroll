---
layout: default
title: STELLAR: Scene Text Editor for Low-Resource Languages and Real-World Data
---

# STELLAR: Scene Text Editor for Low-Resource Languages and Real-World Data
**arXiv**：[2511.09977v1](https://arxiv.org/abs/2511.09977) · [PDF](https://arxiv.org/pdf/2511.09977.pdf)  
**作者**：Yongdeuk Seo, Hyun-seok Min, Sungchul Choi  

**一句话要点**：提出STELLAR场景文本编辑器，以解决低资源语言支持和真实数据域差距问题。

**关键词**：场景文本编辑, 低资源语言, 多阶段训练, 文本外观相似性, 真实数据微调, 字形编码器

## 3 点简述
- 核心问题：现有方法缺乏低资源语言支持、合成与真实数据域差距，以及文本风格保留评估指标不足。
- 方法要点：采用语言自适应字形编码器和多阶段训练策略，结合合成与真实数据微调。
- 实验或效果：在视觉一致性和识别准确率上优于现有模型，TAS指标平均提升2.2%。

## 摘要（原文）

> Scene Text Editing (STE) is the task of modifying text content in an image while preserving its visual style, such as font, color, and background. While recent diffusion-based approaches have shown improvements in visual quality, key limitations remain: lack of support for low-resource languages, domain gap between synthetic and real data, and the absence of appropriate metrics for evaluating text style preservation. To address these challenges, we propose STELLAR (Scene Text Editor for Low-resource LAnguages and Real-world data). STELLAR enables reliable multilingual editing through a language-adaptive glyph encoder and a multi-stage training strategy that first pre-trains on synthetic data and then fine-tunes on real images. We also construct a new dataset, STIPLAR(Scene Text Image Pairs of Low-resource lAnguages and Real-world data), for training and evaluation. Furthermore, we propose Text Appearance Similarity (TAS), a novel metric that assesses style preservation by independently measuring font, color, and background similarity, enabling robust evaluation even without ground truth. Experimental results demonstrate that STELLAR outperforms state-of-the-art models in visual consistency and recognition accuracy, achieving an average TAS improvement of 2.2% across languages over the baselines.


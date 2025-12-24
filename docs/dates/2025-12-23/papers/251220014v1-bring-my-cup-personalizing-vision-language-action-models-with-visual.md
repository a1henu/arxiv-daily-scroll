---
layout: default
title: Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting
---

# Bring My Cup! Personalizing Vision-Language-Action Models with Visual Attentive Prompting
**arXiv**：[2512.20014v1](https://arxiv.org/abs/2512.20014) · [PDF](https://arxiv.org/pdf/2512.20014.pdf)  
**作者**：Sangoh Lee, Sangwoo Mo, Wook-Shin Han  

**一句话要点**：提出视觉注意力提示以解决视觉-语言-动作模型在个性化对象操作中的实例识别难题

**关键词**：视觉-语言-动作模型, 个性化对象操作, 视觉注意力提示, 开放词汇检测, 实例识别, 免训练适配器

## 3 点简述
- 核心问题：VLA模型难以处理个性化指令，如从相似对象中识别特定实例
- 方法要点：使用视觉注意力提示作为免训练适配器，通过参考图像进行开放词汇检测和嵌入匹配
- 实验或效果：在仿真和真实基准测试中，VAP在成功率和正确对象操作上优于通用策略和基线方法

## 摘要（原文）

> While Vision-Language-Action (VLA) models generalize well to generic instructions, they struggle with personalized commands such as "bring my cup", where the robot must act on one specific instance among visually similar objects. We study this setting of manipulating personal objects, in which a VLA must identify and control a user-specific object unseen during training using only a few reference images. To address this challenge, we propose Visual Attentive Prompting (VAP), a simple-yet-effective training-free perceptual adapter that equips frozen VLAs with top-down selective attention. VAP treats the reference images as a non-parametric visual memory, grounds the personal object in the scene through open-vocabulary detection and embedding-based matching, and then injects this grounding as a visual prompt by highlighting the object and rewriting the instruction. We construct two simulation benchmarks, Personalized-SIMPLER and Personalized-VLABench, and a real-world tabletop benchmark to evaluate personalized manipulation across multiple robots and tasks. Experiments show that VAP consistently outperforms generic policies and token-learning baselines in both success rate and correct-object manipulation, helping to bridge the gap between semantic understanding and instance-level control.


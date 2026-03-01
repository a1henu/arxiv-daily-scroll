---
layout: default
title: SignVLA: A Gloss-Free Vision-Language-Action Framework for Real-Time Sign Language-Guided Robotic Manipulation
---

# SignVLA: A Gloss-Free Vision-Language-Action Framework for Real-Time Sign Language-Guided Robotic Manipulation
**arXiv**：[2602.22514v1](https://arxiv.org/abs/2602.22514) · [PDF](https://arxiv.org/pdf/2602.22514.pdf)  
**作者**：Xinyu Tan, Ningwei Bai, Harry Gardener, Zhengyang Zhong, Luoyu Zhang, Liuhaichen Yang, Zhekai Duan, Monkgogi Galeitsiwe, Zezhi Tang  

**一句话要点**：提出无注释符的视觉-语言-动作框架，实现实时手语引导的机器人操控

**关键词**：无注释符手语识别, 视觉-语言-动作框架, 实时机器人操控, 字母级手语交互, 多模态人机交互

## 3 点简述
- 核心问题：传统手语交互依赖注释符作为中间监督，导致标注成本高和信息损失。
- 方法要点：采用无注释符范式，直接映射视觉手势到语义指令，通过几何归一化和时间平滑提升稳定性。
- 实验或效果：在多样化交互场景中，系统能有效将手语指令转化为精确机器人动作，支持字母级实时交互。

## 摘要（原文）

> We present, to our knowledge, the first sign language-driven Vision-Language-Action (VLA) framework for intuitive and inclusive human-robot interaction. Unlike conventional approaches that rely on gloss annotations as intermediate supervision, the proposed system adopts a gloss-free paradigm and directly maps visual sign gestures to semantic instructions. This design reduces annotation cost and avoids the information loss introduced by gloss representations, enabling more natural and scalable multimodal interaction.
>   In this work, we focus on a real-time alphabet-level finger-spelling interface that provides a robust and low-latency communication channel for robotic control. Compared with large-scale continuous sign language recognition, alphabet-level interaction offers improved reliability, interpretability, and deployment feasibility in safety-critical embodied environments. The proposed pipeline transforms continuous gesture streams into coherent language commands through geometric normalization, temporal smoothing, and lexical refinement, ensuring stable and consistent interaction.
>   Furthermore, the framework is designed to support future integration of transformer-based gloss-free sign language models, enabling scalable word-level and sentence-level semantic understanding. Experimental results demonstrate the effectiveness of the proposed system in grounding sign-derived instructions into precise robotic actions under diverse interaction scenarios. These results highlight the potential of the framework to advance accessible, scalable, and multimodal embodied intelligence.


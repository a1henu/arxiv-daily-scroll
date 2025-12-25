---
layout: default
title: VisRes Bench: On Evaluating the Visual Reasoning Capabilities of VLMs
---

# VisRes Bench: On Evaluating the Visual Reasoning Capabilities of VLMs
**arXiv**：[2512.21194v1](https://arxiv.org/abs/2512.21194) · [PDF](https://arxiv.org/pdf/2512.21194.pdf)  
**作者**：Brigitta Malagurski Törtei, Yasser Dahou, Ngoc Dung Huynh, Wamiq Reyaz Para, Phúc H. Lê Khac, Ankit Singh, Sofian Chaybouti, Sanath Narayan  

**一句话要点**：提出VisRes Bench基准以评估视觉语言模型在无语言监督下的视觉推理能力

**关键词**：视觉推理评估, 多模态基准, 感知扰动, 属性推理, 组合推理, 语言先验

## 3 点简述
- 核心问题：视觉语言模型是否依赖语言先验而非真正视觉推理，能力范围不明确
- 方法要点：设计三级复杂度基准，隔离感知、关系和组合推理能力，使用扰动和属性控制
- 实验或效果：在19000+图像上测试，发现先进模型在细微扰动下表现接近随机，抽象推理有限

## 摘要（原文）

> Vision-Language Models (VLMs) have achieved remarkable progress across tasks such as visual question answering and image captioning. Yet, the extent to which these models perform visual reasoning as opposed to relying on linguistic priors remains unclear. To address this, we introduce VisRes Bench, a benchmark designed to study visual reasoning in naturalistic settings without contextual language supervision. Analyzing model behavior across three levels of complexity, we uncover clear limitations in perceptual and relational visual reasoning capacities. VisRes isolates distinct reasoning abilities across its levels. Level 1 probes perceptual completion and global image matching under perturbations such as blur, texture changes, occlusion, and rotation; Level 2 tests rule-based inference over a single attribute (e.g., color, count, orientation); and Level 3 targets compositional reasoning that requires integrating multiple visual attributes. Across more than 19,000 controlled task images, we find that state-of-the-art VLMs perform near random under subtle perceptual perturbations, revealing limited abstraction beyond pattern recognition. We conclude by discussing how VisRes provides a unified framework for advancing abstract visual reasoning in multimodal research.


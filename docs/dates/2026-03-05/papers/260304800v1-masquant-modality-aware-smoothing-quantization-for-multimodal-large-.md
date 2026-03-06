---
layout: default
title: MASQuant: Modality-Aware Smoothing Quantization for Multimodal Large Language Models
---

# MASQuant: Modality-Aware Smoothing Quantization for Multimodal Large Language Models
**arXiv**：[2603.04800v1](https://arxiv.org/abs/2603.04800) · [PDF](https://arxiv.org/pdf/2603.04800.pdf)  
**作者**：Lulu Hu, Wenhu Xiao, Xin Chen, Xinhua Xu, Bowen Xu, Kun Li, Yongliang Tao  

**一句话要点**：提出MASQuant以解决多模态大语言模型后训练量化中的平滑错位和跨模态计算不变性问题

**关键词**：多模态大语言模型, 后训练量化, 模态感知平滑, 跨模态补偿, SVD白化, 量化性能

## 3 点简述
- 核心问题：SmoothQuant在多模态大语言模型中存在平滑错位和跨模态计算不变性问题，导致量化性能下降
- 方法要点：引入模态感知平滑学习模态特定平滑因子，以及跨模态补偿使用SVD白化统一量化多模态激活
- 实验或效果：在双模态和三模态MLLMs上展示稳定量化性能，与先进PTQ算法竞争

## 摘要（原文）

> Post-training quantization (PTQ) with computational invariance for Large Language Models~(LLMs) have demonstrated remarkable advances, however, their application to Multimodal Large Language Models~(MLLMs) presents substantial challenges. In this paper, we analyze SmoothQuant as a case study and identify two critical issues: Smoothing Misalignment and Cross-Modal Computational Invariance. To address these issues, we propose Modality-Aware Smoothing Quantization (MASQuant), a novel framework that introduces (1) Modality-Aware Smoothing (MAS), which learns separate, modality-specific smoothing factors to prevent Smoothing Misalignment, and (2) Cross-Modal Compensation (CMC), which addresses Cross-modal Computational Invariance by using SVD whitening to transform multi-modal activation differences into low-rank forms, enabling unified quantization across modalities. MASQuant demonstrates stable quantization performance across both dual-modal and tri-modal MLLMs. Experimental results show that MASQuant is competitive among the state-of-the-art PTQ algorithms. Source code: https://github.com/alibaba/EfficientAI.


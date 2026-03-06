---
layout: default
title: How far have we gone in Generative Image Restoration? A study on its capability, limitations and evaluation practices
---

# How far have we gone in Generative Image Restoration? A study on its capability, limitations and evaluation practices
**arXiv**：[2603.05010v1](https://arxiv.org/abs/2603.05010) · [PDF](https://arxiv.org/pdf/2603.05010.pdf)  
**作者**：Xiang Yin, Jinfan Hu, Zhiyuan You, Kainan Yan, Yu Tang, Chao Dong, Jinjin Gu  

**一句话要点**：提出多维评估流程以系统研究生成式图像修复的实际能力与局限

**关键词**：生成式图像修复, 多维评估, 失败模式分析, 图像质量评估, 感知导向视觉

## 3 点简述
- 核心问题：生成式图像修复在细节、清晰度、语义正确性和整体质量上的实际进展与失败模式演变
- 方法要点：基于扩散、GAN、PSNR导向和通用生成模型，设计大规模评估管道进行对比分析
- 实验或效果：揭示性能差异，训练新图像质量评估模型以更好对齐人类感知判断

## 摘要（原文）

> Generative Image Restoration (GIR) has achieved impressive perceptual realism, but how far have its practical capabilities truly advanced compared with previous methods? To answer this, we present a large-scale study grounded in a new multi-dimensional evaluation pipeline that assesses models on detail, sharpness, semantic correctness, and overall quality. Our analysis covers diverse architectures, including diffusion-based, GAN-based, PSNR-oriented, and general-purpose generation models, revealing critical performance disparities. Furthermore, our analysis uncovers a key evolution in failure modes that signifies a paradigm shift for the perception-oriented low-level vision field. The central challenge is evolving from the previous problem of detail scarcity (under-generation) to the new frontier of detail quality and semantic control (preventing over-generation). We also leverage our benchmark to train a new IQA model that better aligns with human perceptual judgments. Ultimately, this work provides a systematic study of modern generative image restoration models, offering crucial insights that redefine our understanding of their true state and chart a course for future development.


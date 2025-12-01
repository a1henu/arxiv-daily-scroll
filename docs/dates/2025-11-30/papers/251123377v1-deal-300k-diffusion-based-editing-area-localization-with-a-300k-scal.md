---
layout: default
title: DEAL-300K: Diffusion-based Editing Area Localization with a 300K-Scale Dataset and Frequency-Prompted Baseline
---

# DEAL-300K: Diffusion-based Editing Area Localization with a 300K-Scale Dataset and Frequency-Prompted Baseline
**arXiv**：[2511.23377v1](https://arxiv.org/abs/2511.23377) · [PDF](https://arxiv.org/pdf/2511.23377.pdf)  
**作者**：Rui Zhang, Hongxia Wang, Hangqing Liu, Yang Zhou, Qiang Zeng  

**一句话要点**：提出DEAL-300K数据集与频率提示基线，用于扩散编辑区域定位，以解决局部伪造检测难题。

**关键词**：扩散编辑定位, 大规模数据集, 频率域分析, 视觉基础模型, 像素级标注

## 3 点简述
- 核心问题：扩散编辑图像局部伪造难以定位，现有基准不反映其平滑融合特性。
- 方法要点：构建大规模数据集，结合多模态指令生成、无掩码编辑器和主动学习标注。
- 实验或效果：基于冻结视觉基础模型与多频率提示调优，在测试集上达到82.56%像素级F1分数。

## 摘要（原文）

> Diffusion-based image editing has made semantic level image manipulation easy for general users, but it also enables realistic local forgeries that are hard to localize. Existing benchmarks mainly focus on the binary detection of generated images or the localization of manually edited regions and do not reflect the properties of diffusion-based edits, which often blend smoothly into the original content. We present Diffusion-Based Image Editing Area Localization Dataset (DEAL-300K), a large scale dataset for diffusion-based image manipulation localization (DIML) with more than 300,000 annotated images. We build DEAL-300K by using a multi-modal large language model to generate editing instructions, a mask-free diffusion editor to produce manipulated images, and an active-learning change detection pipeline to obtain pixel-level annotations. On top of this dataset, we propose a localization framework that uses a frozen Visual Foundation Model (VFM) together with Multi Frequency Prompt Tuning (MFPT) to capture both semantic and frequency-domain cues of edited regions. Trained on DEAL-300K, our method reaches a pixel-level F1 score of 82.56% on our test split and 80.97% on the external CoCoGlide benchmark, providing strong baselines and a practical foundation for future DIML research.The dataset can be accessed via https://github.com/ymhzyj/DEAL-300K.


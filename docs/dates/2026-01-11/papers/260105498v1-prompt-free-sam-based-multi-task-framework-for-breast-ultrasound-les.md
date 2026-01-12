---
layout: default
title: Prompt-Free SAM-Based Multi-Task Framework for Breast Ultrasound Lesion Segmentation and Classification
---

# Prompt-Free SAM-Based Multi-Task Framework for Breast Ultrasound Lesion Segmentation and Classification
**arXiv**：[2601.05498v1](https://arxiv.org/abs/2601.05498) · [PDF](https://arxiv.org/pdf/2601.05498.pdf)  
**作者**：Samuel E. Johnny, Bernes L. Atabonfack, Israel Alagbe, Assane Gueye  

**一句话要点**：提出基于SAM的无提示多任务框架，用于乳腺超声病灶分割与分类

**关键词**：乳腺超声分割, 多任务学习, SAM模型, 掩码引导注意力, 病灶分类

## 3 点简述
- 核心问题：乳腺超声图像因低对比度、斑点噪声和病灶形态多样，分割与分类准确率低。
- 方法要点：利用SAM视觉编码器特征，通过无提示监督解码进行分割，结合掩码引导注意力增强分类。
- 实验或效果：在PRECISE 2025数据集上，DSC达0.887，准确率92.3%，在挑战榜上名列前茅。

## 摘要（原文）

> Accurate tumor segmentation and classification in breast ultrasound (BUS) imaging remain challenging due to low contrast, speckle noise, and diverse lesion morphology. This study presents a multi-task deep learning framework that jointly performs lesion segmentation and diagnostic classification using embeddings from the Segment Anything Model (SAM) vision encoder. Unlike prompt-based SAM variants, our approach employs a prompt-free, fully supervised adaptation where high-dimensional SAM features are decoded through either a lightweight convolutional head or a UNet-inspired decoder for pixel-wise segmentation. The classification branch is enhanced via mask-guided attention, allowing the model to focus on lesion-relevant features while suppressing background artifacts. Experiments on the PRECISE 2025 breast ultrasound dataset, split per class into 80 percent training and 20 percent testing, show that the proposed method achieves a Dice Similarity Coefficient (DSC) of 0.887 and an accuracy of 92.3 percent, ranking among the top entries on the PRECISE challenge leaderboard. These results demonstrate that SAM-based representations, when coupled with segmentation-guided learning, significantly improve both lesion delineation and diagnostic prediction in breast ultrasound imaging.


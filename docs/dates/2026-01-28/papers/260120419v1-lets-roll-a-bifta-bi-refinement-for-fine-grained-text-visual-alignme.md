---
layout: default
title: Let's Roll a BiFTA: Bi-refinement for Fine-grained Text-visual Alignment in Vision-Language Models
---

# Let's Roll a BiFTA: Bi-refinement for Fine-grained Text-visual Alignment in Vision-Language Models
**arXiv**：[2601.20419v1](https://arxiv.org/abs/2601.20419) · [PDF](https://arxiv.org/pdf/2601.20419.pdf)  
**作者**：Yuhao Sun, Chengyi Cai, Jiacheng Zhang, Zesheng Ye, Xingliang Yuan, Feng Liu  

**一句话要点**：提出BiFTA方法，通过双细化去除冗余信息以提升细粒度文本-视觉对齐效果。

**关键词**：细粒度对齐, 视觉语言模型, 冗余去除, 零样本学习, CLIP优化

## 3 点简述
- 核心问题：细粒度文本描述与局部图像块常含冗余信息，降低对齐效率。
- 方法要点：采用视图细化和描述细化，分别基于IoU和余弦相似度去除冗余。
- 实验或效果：在6个基准数据集上，BiFTA提升了基于ViT和ResNet的CLIP的零样本性能。

## 摘要（原文）

> Recent research has shown that aligning fine-grained text descriptions with localized image patches can significantly improve the zero-shot performance of pre-trained vision-language models (e.g., CLIP). However, we find that both fine-grained text descriptions and localized image patches often contain redundant information, making text-visual alignment less effective. In this paper, we tackle this issue from two perspectives: \emph{View Refinement} and \emph{Description refinement}, termed as \textit{\textbf{Bi}-refinement for \textbf{F}ine-grained \textbf{T}ext-visual \textbf{A}lignment} (BiFTA). \emph{View refinement} removes redundant image patches with high \emph{Intersection over Union} (IoU) ratios, resulting in more distinctive visual samples. \emph{Description refinement} removes redundant text descriptions with high pairwise cosine similarity, ensuring greater diversity in the remaining descriptions. BiFTA achieves superior zero-shot performance on 6 benchmark datasets for both ViT-based and ResNet-based CLIP, justifying the necessity to remove redundant information in visual-text alignment.


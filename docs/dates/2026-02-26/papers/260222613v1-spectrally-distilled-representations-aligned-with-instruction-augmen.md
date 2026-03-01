---
layout: default
title: Spectrally Distilled Representations Aligned with Instruction-Augmented LLMs for Satellite Imagery
---

# Spectrally Distilled Representations Aligned with Instruction-Augmented LLMs for Satellite Imagery
**arXiv**：[2602.22613v1](https://arxiv.org/abs/2602.22613) · [PDF](https://arxiv.org/pdf/2602.22613.pdf)  
**作者**：Minh Kha Do, Wei Xiang, Kang Han, Di Wu, Khoa Phan, Yi-Ping Phoebe Chen, Gaowen Liu, Ramana Rao Kompella  

**一句话要点**：提出SATtxt模型，通过光谱蒸馏与指令增强LLM对齐，实现仅RGB输入的卫星图像视觉语言学习。

**关键词**：卫星图像理解, 光谱蒸馏, 视觉语言模型, 指令增强LLM, 零样本学习

## 3 点简述
- 问题：卫星图像多光谱输入冗余且对齐困难，CLIP文本编码器语义表达受限。
- 方法：先蒸馏多光谱先验到RGB学生，再与指令增强LLM嵌入空间对齐。
- 效果：在EuroSAT等数据集上，零样本分类、检索和线性探测性能平均提升。

## 摘要（原文）

> Vision-language foundation models (VLFMs) promise zero-shot and retrieval understanding for Earth observation. While operational satellite systems often lack full multi-spectral coverage, making RGB-only inference highly desirable for scalable deployment, the adoption of VLFMs for satellite imagery remains hindered by two factors: (1) multi-spectral inputs are informative but difficult to exploit consistently due to band redundancy and misalignment; and (2) CLIP-style text encoders limit semantic expressiveness and weaken fine-grained alignment. We present SATtxt, a spectrum-aware VLFM that operates with RGB inputs only at inference while retaining spectral cues learned during training. Our framework comprises two stages. First, Spectral Representation Distillation transfers spectral priors from a frozen multi-spectral teacher to an RGB student via a lightweight projector. Second, Spectrally Grounded Alignment with Instruction-Augmented LLMs bridges the distilled visual space and an expressive LLM embedding space. Across EuroSAT, BigEarthNet, and ForestNet, SATtxt improves zero-shot classification on average by 4.2%, retrieval by 5.9%, and linear probing by 2.7% over baselines, showing an efficient path toward spectrum-aware vision-language learning for Earth observation. Project page: https://ikhado.github.io/sattxt/


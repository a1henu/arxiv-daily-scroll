---
layout: default
title: PanoGrounder: Bridging 2D and 3D with Panoramic Scene Representations for VLM-based 3D Visual Grounding
---

# PanoGrounder: Bridging 2D and 3D with Panoramic Scene Representations for VLM-based 3D Visual Grounding
**arXiv**：[2512.20907v1](https://arxiv.org/abs/2512.20907) · [PDF](https://arxiv.org/pdf/2512.20907.pdf)  
**作者**：Seongmin Jung, Seongho Choi, Gunwoo Jeon, Minsu Cho, Jongwoo Lim  

**一句话要点**：提出PanoGrounder框架，通过全景场景表示桥接2D与3D，用于基于VLM的3D视觉定位。

**关键词**：3D视觉定位, 全景场景表示, 视觉语言模型, 多模态融合, 泛化能力

## 3 点简述
- 核心问题：传统3D视觉定位模型依赖显式3D几何，但泛化能力有限，受限于数据集稀缺和推理能力不足。
- 方法要点：利用增强3D语义和几何特征的全景渲染作为中间表示，结合预训练2D视觉语言模型进行多阶段推理。
- 实验或效果：在ScanRefer和Nr3D数据集上达到最优结果，并展示对未见3D数据集和文本重述的强泛化能力。

## 摘要（原文）

> 3D Visual Grounding (3DVG) is a critical bridge from vision-language perception to robotics, requiring both language understanding and 3D scene reasoning. Traditional supervised models leverage explicit 3D geometry but exhibit limited generalization, owing to the scarcity of 3D vision-language datasets and the limited reasoning capabilities compared to modern vision-language models (VLMs). We propose PanoGrounder, a generalizable 3DVG framework that couples multi-modal panoramic representation with pretrained 2D VLMs for strong vision-language reasoning. Panoramic renderings, augmented with 3D semantic and geometric features, serve as an intermediate representation between 2D and 3D, and offer two major benefits: (i) they can be directly fed to VLMs with minimal adaptation and (ii) they retain long-range object-to-object relations thanks to their 360-degree field of view. We devise a three-stage pipeline that places a compact set of panoramic viewpoints considering the scene layout and geometry, grounds a text query on each panoramic rendering with a VLM, and fuses per-view predictions into a single 3D bounding box via lifting. Our approach achieves state-of-the-art results on ScanRefer and Nr3D, and demonstrates superior generalization to unseen 3D datasets and text rephrasings.


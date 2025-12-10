---
layout: default
title: EgoX: Egocentric Video Generation from a Single Exocentric Video
---

# EgoX: Egocentric Video Generation from a Single Exocentric Video
**arXiv**：[2512.08269v1](https://arxiv.org/abs/2512.08269) · [PDF](https://arxiv.org/pdf/2512.08269.pdf)  
**作者**：Taewoong Kang, Kinam Kim, Dohyeon Kim, Minho Park, Junha Hyung, Jaegul Choo  

**一句话要点**：提出EgoX框架，通过单视角外中心视频生成内中心视频，解决视角差异大和重叠少的挑战。

**关键词**：视频生成, 视角转换, 扩散模型, 几何一致性, 自注意力机制, 轻量适配

## 3 点简述
- 核心问题：外中心到内中心视频转换因相机姿态变化大和视图重叠少而困难，需保持几何一致性和视觉保真度。
- 方法要点：利用预训练视频扩散模型，通过LoRA轻量适配和统一条件策略结合外中心与内中心先验，引入几何引导自注意力机制。
- 实验或效果：在未见和野外视频上实现连贯真实的内中心视频生成，展示强可扩展性和鲁棒性。

## 摘要（原文）

> Egocentric perception enables humans to experience and understand the world directly from their own point of view. Translating exocentric (third-person) videos into egocentric (first-person) videos opens up new possibilities for immersive understanding but remains highly challenging due to extreme camera pose variations and minimal view overlap. This task requires faithfully preserving visible content while synthesizing unseen regions in a geometrically consistent manner. To achieve this, we present EgoX, a novel framework for generating egocentric videos from a single exocentric input. EgoX leverages the pretrained spatio temporal knowledge of large-scale video diffusion models through lightweight LoRA adaptation and introduces a unified conditioning strategy that combines exocentric and egocentric priors via width and channel wise concatenation. Additionally, a geometry-guided self-attention mechanism selectively attends to spatially relevant regions, ensuring geometric coherence and high visual fidelity. Our approach achieves coherent and realistic egocentric video generation while demonstrating strong scalability and robustness across unseen and in-the-wild videos.


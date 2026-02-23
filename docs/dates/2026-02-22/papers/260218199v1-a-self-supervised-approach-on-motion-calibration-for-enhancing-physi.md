---
layout: default
title: A Self-Supervised Approach on Motion Calibration for Enhancing Physical Plausibility in Text-to-Motion
---

# A Self-Supervised Approach on Motion Calibration for Enhancing Physical Plausibility in Text-to-Motion
**arXiv**：[2602.18199v1](https://arxiv.org/abs/2602.18199) · [PDF](https://arxiv.org/pdf/2602.18199.pdf)  
**作者**：Gahyeon Shim, Soogeun Park, Hyemin Ahn  

**一句话要点**：提出失真感知运动校准器以增强文本到运动生成中的物理合理性

**关键词**：文本到运动生成, 物理合理性校准, 自监督学习, 后处理模块, 运动失真感知

## 3 点简述
- 核心问题：文本到运动生成中语义对齐与物理合理性难以兼顾，如脚部漂浮。
- 方法要点：采用自监督数据驱动方法，通过失真运动与文本输入学习物理合理运动校准。
- 实验或效果：作为后处理模块提升多种模型，降低FID分数和穿透率，增强语义一致性。

## 摘要（原文）

> Generating semantically aligned human motion from textual descriptions has made rapid progress, but ensuring both semantic and physical realism in motion remains a challenge. In this paper, we introduce the Distortion-aware Motion Calibrator (DMC), a post-hoc module that refines physically implausible motions (e.g., foot floating) while preserving semantic consistency with the original textual description. Rather than relying on complex physical modeling, we propose a self-supervised and data-driven approach, whereby DMC learns to obtain physically plausible motions when an intentionally distorted motion and the original textual descriptions are given as inputs. We evaluate DMC as a post-hoc module to improve motions obtained from various text-to-motion generation models and demonstrate its effectiveness in improving physical plausibility while enhancing semantic consistency. The experimental results show that DMC reduces FID score by 42.74% on T2M and 13.20% on T2M-GPT, while also achieving the highest R-Precision. When applied to high-quality models like MoMask, DMC improves the physical plausibility of motions by reducing penetration by 33.0% as well as adjusting floating artifacts closer to the ground-truth reference. These results highlight that DMC can serve as a promising post-hoc motion refinement framework for any kind of text-to-motion models by incorporating textual semantics and physical plausibility.


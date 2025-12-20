---
layout: default
title: Detecting Localized Deepfakes: How Well Do Synthetic Image Detectors Handle Inpainting?
---

# Detecting Localized Deepfakes: How Well Do Synthetic Image Detectors Handle Inpainting?
**arXiv**：[2512.16688v1](https://arxiv.org/abs/2512.16688) · [PDF](https://arxiv.org/pdf/2512.16688.pdf)  
**作者**：Serafino Pandolfini, Lorenzo Pellegrini, Matteo Ferrara, Davide Maltoni  

**一句话要点**：评估合成图像检测器在局部修复检测中的泛化能力

**关键词**：局部修复检测, 合成图像检测, 泛化能力评估, 生成对抗网络, 图像篡改检测

## 3 点简述
- 核心问题：现有合成图像检测器对局部修复操作的泛化能力未充分评估
- 方法要点：系统评估多种先进检测器在局部修复数据集上的表现
- 实验或效果：模型能部分迁移至修复编辑，可靠检测中大面积或再生式修复

## 摘要（原文）

> The rapid progress of generative AI has enabled highly realistic image manipulations, including inpainting and region-level editing. These approaches preserve most of the original visual context and are increasingly exploited in cybersecurity-relevant threat scenarios. While numerous detectors have been proposed for identifying fully synthetic images, their ability to generalize to localized manipulations remains insufficiently characterized. This work presents a systematic evaluation of state-of-the-art detectors, originally trained for the deepfake detection on fully synthetic images, when applied to a distinct challenge: localized inpainting detection. The study leverages multiple datasets spanning diverse generators, mask sizes, and inpainting techniques. Our experiments show that models trained on a large set of generators exhibit partial transferability to inpainting-based edits and can reliably detect medium- and large-area manipulations or regeneration-style inpainting, outperforming many existing ad hoc detection approaches.


---
layout: default
title: EasyControlEdge: A Foundation-Model Fine-Tuning for Edge Detection
---

# EasyControlEdge: A Foundation-Model Fine-Tuning for Edge Detection
**arXiv**：[2602.16238v1](https://arxiv.org/abs/2602.16238) · [PDF](https://arxiv.org/pdf/2602.16238.pdf)  
**作者**：Hiroki Nakamura, Hiroto Iino, Masashi Okada, Tadahiro Taniguchi  

**一句话要点**：提出EasyControlEdge，通过微调图像生成基础模型实现数据高效且边缘清晰的边缘检测。

**关键词**：边缘检测, 基础模型微调, 数据高效学习, 图像生成模型, 像素空间损失, 无条件动态指导

## 3 点简述
- 核心问题：现实世界边缘检测需在有限训练样本下生成清晰边缘图，现有方法未充分利用基础模型的数据高效迁移和高频细节保留能力。
- 方法要点：引入边缘导向目标与高效像素空间损失，微调图像生成基础模型，并基于无条件动态指导控制边缘密度。
- 实验或效果：在BSDS500等数据集上优于先进方法，尤其在无后处理清晰度评估和有限数据下表现突出。

## 摘要（原文）

> We propose EasyControlEdge, adapting an image-generation foundation model to edge detection. In real-world edge detection (e.g., floor-plan walls, satellite roads/buildings, and medical organ boundaries), crispness and data efficiency are crucial, yet producing crisp raw edge maps with limited training samples remains challenging. Although image-generation foundation models perform well on many downstream tasks, their pretrained priors for data-efficient transfer and iterative refinement for high-frequency detail preservation remain underexploited for edge detection. To enable crisp and data-efficient edge detection using these capabilities, we introduce an edge-specialized adaptation of image-generation foundation models. To better specialize the foundation model for edge detection, we incorporate an edge-oriented objective with an efficient pixel-space loss. At inference, we introduce guidance based on unconditional dynamics, enabling a single model to control the edge density through a guidance scale. Experiments on BSDS500, NYUDv2, BIPED, and CubiCasa compare against state-of-the-art methods and show consistent gains, particularly under no-post-processing crispness evaluation and with limited training data.


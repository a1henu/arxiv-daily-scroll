---
layout: default
title: SAM-Body4D: Training-Free 4D Human Body Mesh Recovery from Videos
---

# SAM-Body4D: Training-Free 4D Human Body Mesh Recovery from Videos
**arXiv**：[2512.08406v1](https://arxiv.org/abs/2512.08406) · [PDF](https://arxiv.org/pdf/2512.08406.pdf)  
**作者**：Mingqi Gao, Yunqi Miao, Jungong Han  

**一句话要点**：提出SAM-Body4D框架，无需训练实现视频中4D人体网格恢复，提升时间一致性与遮挡鲁棒性。

**关键词**：4D人体网格恢复, 视频理解, 遮挡鲁棒性, 训练免费框架, 时间一致性

## 3 点简述
- 核心问题：视频中基于图像的HMR方法存在时间不一致和遮挡下性能下降问题。
- 方法要点：利用视频连续性，通过身份一致掩码生成和遮挡感知模块，指导SAM 3D Body恢复网格。
- 实验或效果：在野外视频中验证了时间稳定性和鲁棒性提升，无需额外训练。

## 摘要（原文）

> Human Mesh Recovery (HMR) aims to reconstruct 3D human pose and shape from 2D observations and is fundamental to human-centric understanding in real-world scenarios. While recent image-based HMR methods such as SAM 3D Body achieve strong robustness on in-the-wild images, they rely on per-frame inference when applied to videos, leading to temporal inconsistency and degraded performance under occlusions. We address these issues without extra training by leveraging the inherent human continuity in videos. We propose SAM-Body4D, a training-free framework for temporally consistent and occlusion-robust HMR from videos. We first generate identity-consistent masklets using a promptable video segmentation model, then refine them with an Occlusion-Aware module to recover missing regions. The refined masklets guide SAM 3D Body to produce consistent full-body mesh trajectories, while a padding-based parallel strategy enables efficient multi-human inference. Experimental results demonstrate that SAM-Body4D achieves improved temporal stability and robustness in challenging in-the-wild videos, without any retraining. Our code and demo are available at: https://github.com/gaomingqi/sam-body4d.


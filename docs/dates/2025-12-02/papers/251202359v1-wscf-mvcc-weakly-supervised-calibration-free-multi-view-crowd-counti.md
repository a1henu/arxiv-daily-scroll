---
layout: default
title: WSCF-MVCC: Weakly-supervised Calibration-free Multi-view Crowd Counting
---

# WSCF-MVCC: Weakly-supervised Calibration-free Multi-view Crowd Counting
**arXiv**：[2512.02359v1](https://arxiv.org/abs/2512.02359) · [PDF](https://arxiv.org/pdf/2512.02359.pdf)  
**作者**：Bin Li, Daijie Chen, Qi Zhang  

**一句话要点**：提出弱监督无标定多视角人群计数方法，以降低标注与标定成本。

**关键词**：多视角人群计数, 弱监督学习, 无标定方法, 自监督学习, 语义匹配

## 3 点简述
- 核心问题：现有多视角计数方法依赖昂贵的人群标注和相机标定，限制实际部署。
- 方法要点：使用人群计数作为监督，结合自监督排序损失和语义信息提升感知与匹配精度。
- 实验或效果：在三个数据集上优于现有方法，表明更适用于弱监督场景。

## 摘要（原文）

> Multi-view crowd counting can effectively mitigate occlusion issues that commonly arise in single-image crowd counting. Existing deep-learning multi-view crowd counting methods project different camera view images onto a common space to obtain ground-plane density maps, requiring abundant and costly crowd annotations and camera calibrations. Hence, calibration-free methods are proposed that do not require camera calibrations and scene-level crowd annotations. However, existing calibration-free methods still require expensive image-level crowd annotations for training the single-view counting module. Thus, in this paper, we propose a weakly-supervised calibration-free multi-view crowd counting method (WSCF-MVCC), directly using crowd count as supervision for the single-view counting module rather than density maps constructed from crowd annotations. Instead, a self-supervised ranking loss that leverages multi-scale priors is utilized to enhance the model's perceptual ability without additional annotation costs. What's more, the proposed model leverages semantic information to achieve a more accurate view matching and, consequently, a more precise scene-level crowd count estimation. The proposed method outperforms the state-of-the-art methods on three widely used multi-view counting datasets under weakly supervised settings, indicating that it is more suitable for practical deployment compared with calibrated methods. Code is released in https://github.com/zqyq/Weakly-MVCC.


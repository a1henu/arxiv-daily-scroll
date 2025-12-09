---
layout: default
title: DGGAN: Degradation Guided Generative Adversarial Network for Real-time Endoscopic Video Enhancement
---

# DGGAN: Degradation Guided Generative Adversarial Network for Real-time Endoscopic Video Enhancement
**arXiv**：[2512.07253v1](https://arxiv.org/abs/2512.07253) · [PDF](https://arxiv.org/pdf/2512.07253.pdf)  
**作者**：Handing Xu, Zhenguo Nie, Tairan Peng, Huimin Pan, Xin-Jun Liu  

**一句话要点**：提出DGGAN，通过退化感知建模实现实时内窥镜视频增强

**关键词**：内窥镜视频增强, 退化感知建模, 实时处理, 生成对抗网络, 对比学习, 循环一致性

## 3 点简述
- 核心问题：内窥镜视频因光照不均、组织散射等退化影响手术安全，现有深度学习方法计算量大，难以实时应用。
- 方法要点：采用对比学习提取退化表示，通过融合机制调制图像特征，结合循环一致性约束训练单帧增强模型，实现跨帧退化传播。
- 实验或效果：在性能与效率间取得优越平衡，验证了退化感知建模对实时增强的有效性，为临床应用提供可行路径。

## 摘要（原文）

> Endoscopic surgery relies on intraoperative video, making image quality a decisive factor for surgical safety and efficacy. Yet, endoscopic videos are often degraded by uneven illumination, tissue scattering, occlusions, and motion blur, which obscure critical anatomical details and complicate surgical manipulation. Although deep learning-based methods have shown promise in image enhancement, most existing approaches remain too computationally demanding for real-time surgical use. To address this challenge, we propose a degradation-aware framework for endoscopic video enhancement, which enables real-time, high-quality enhancement by propagating degradation representations across frames. In our framework, degradation representations are first extracted from images using contrastive learning. We then introduce a fusion mechanism that modulates image features with these representations to guide a single-frame enhancement model, which is trained with a cycle-consistency constraint between degraded and restored images to improve robustness and generalization. Experiments demonstrate that our framework achieves a superior balance between performance and efficiency compared with several state-of-the-art methods. These results highlight the effectiveness of degradation-aware modeling for real-time endoscopic video enhancement. Nevertheless, our method suggests that implicitly learning and propagating degradation representation offer a practical pathway for clinical application.


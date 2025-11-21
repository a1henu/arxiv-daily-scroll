---
layout: default
title: ChangeDINO: DINOv3-Driven Building Change Detection in Optical Remote Sensing Imagery
---

# ChangeDINO: DINOv3-Driven Building Change Detection in Optical Remote Sensing Imagery
**arXiv**：[2511.16322v1](https://arxiv.org/abs/2511.16322) · [PDF](https://arxiv.org/pdf/2511.16322.pdf)  
**作者**：Ching-Heng Cheng, Chih-Chung Hsu  

**一句话要点**：提出ChangeDINO以解决光学遥感图像中建筑变化检测的鲁棒性问题

**关键词**：遥感变化检测, DINOv3特征融合, Siamese框架, 多尺度差分变换器, 形态学优化

## 3 点简述
- 核心问题：现有方法依赖变化图标注，忽略非变化区域语义信息，导致光照、视角变化和标签稀缺时鲁棒性差
- 方法要点：结合轻量骨干与冻结DINOv3特征，使用空间-光谱差分变换器解码器突出真实变化
- 实验或效果：在四个公共基准上IoU和F1指标优于最新方法，消融研究验证组件有效性

## 摘要（原文）

> Remote sensing change detection (RSCD) aims to identify surface changes from co-registered bi-temporal images. However, many deep learning-based RSCD methods rely solely on change-map annotations and underuse the semantic information in non-changing regions, which limits robustness under illumination variation, off-nadir views, and scarce labels. This article introduces ChangeDINO, an end-to-end multiscale Siamese framework for optical building change detection. The model fuses a lightweight backbone stream with features transferred from a frozen DINOv3, yielding semantic- and context-rich pyramids even on small datasets. A spatial-spectral differential transformer decoder then exploits multi-scale absolute differences as change priors to highlight true building changes and suppress irrelevant responses. Finally, a learnable morphology module refines the upsampled logits to recover clean boundaries. Experiments on four public benchmarks show that ChangeDINO consistently outperforms recent state-of-the-art methods in IoU and F1, and ablation studies confirm the effectiveness of each component. The source code is available at https://github.com/chingheng0808/ChangeDINO.


---
layout: default
title: Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection
---

# Assisted Refinement Network Based on Channel Information Interaction for Camouflaged and Salient Object Detection
**arXiv**：[2512.11369v1](https://arxiv.org/abs/2512.11369) · [PDF](https://arxiv.org/pdf/2512.11369.pdf)  
**作者**：Kuan Wang, Yanjun Qin, Mengge Lu, Liejun Wang, Xiaoming Tao  

**一句话要点**：提出基于通道信息交互的辅助精炼网络，以解决伪装与显著目标检测中的特征表达与边界重建问题。

**关键词**：伪装目标检测, 显著目标检测, 通道信息交互, 协同解码, 多尺度增强

## 3 点简述
- 核心问题：解码阶段跨通道信息交互不足，边界与区域信息协同建模困难。
- 方法要点：引入通道信息交互模块和先验知识引导的协同解码架构，增强特征表达。
- 实验或效果：在多个基准数据集上验证有效性，并展示下游任务适应性。

## 摘要（原文）

> Camouflaged Object Detection (COD) stands as a significant challenge in computer vision, dedicated to identifying and segmenting objects visually highly integrated with their backgrounds. Current mainstream methods have made progress in cross-layer feature fusion, but two critical issues persist during the decoding stage. The first is insufficient cross-channel information interaction within the same-layer features, limiting feature expressiveness. The second is the inability to effectively co-model boundary and region information, making it difficult to accurately reconstruct complete regions and sharp boundaries of objects. To address the first issue, we propose the Channel Information Interaction Module (CIIM), which introduces a horizontal-vertical integration mechanism in the channel dimension. This module performs feature reorganization and interaction across channels to effectively capture complementary cross-channel information. To address the second issue, we construct a collaborative decoding architecture guided by prior knowledge. This architecture generates boundary priors and object localization maps through Boundary Extraction (BE) and Region Extraction (RE) modules, then employs hybrid attention to collaboratively calibrate decoded features, effectively overcoming semantic ambiguity and imprecise boundaries. Additionally, the Multi-scale Enhancement (MSE) module enriches contextual feature representations. Extensive experiments on four COD benchmark datasets validate the effectiveness and state-of-the-art performance of the proposed model. We further transferred our model to the Salient Object Detection (SOD) task and demonstrated its adaptability across downstream tasks, including polyp segmentation, transparent object detection, and industrial and road defect detection. Code and experimental results are publicly available at: https://github.com/akuan1234/ARNet-v2.


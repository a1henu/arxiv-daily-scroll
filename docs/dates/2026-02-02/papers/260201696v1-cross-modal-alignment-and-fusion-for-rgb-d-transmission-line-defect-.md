---
layout: default
title: Cross-Modal Alignment and Fusion for RGB-D Transmission-Line Defect Detection
---

# Cross-Modal Alignment and Fusion for RGB-D Transmission-Line Defect Detection
**arXiv**：[2602.01696v1](https://arxiv.org/abs/2602.01696) · [PDF](https://arxiv.org/pdf/2602.01696.pdf)  
**作者**：Jiaming Cui, Shuai Zhou, Wenqiang Li, Ruifeng Qin, Feng Shen  

**一句话要点**：提出CMAFNet以解决RGB-D输电线路小缺陷检测中模态噪声与融合挑战

**关键词**：跨模态对齐, 特征纯化, RGB-D检测, 小目标检测, 输电线路缺陷, 轻量网络

## 3 点简述
- 核心问题：RGB检测器在复杂背景和光照下难以区分几何细微缺陷与视觉相似结构
- 方法要点：通过基于字典的特征纯化和全局空间依赖的上下文语义集成，实现跨模态对齐与融合
- 实验或效果：在TLRGBD基准上，CMAFNet以32.2% mAP@50和12.5% APs优于最强基线，轻量版达228 FPS

## 摘要（原文）

> Transmission line defect detection remains challenging for automated UAV inspection due to the dominance of small-scale defects, complex backgrounds, and illumination variations. Existing RGB-based detectors, despite recent progress, struggle to distinguish geometrically subtle defects from visually similar background structures under limited chromatic contrast. This paper proposes CMAFNet, a Cross-Modal Alignment and Fusion Network that integrates RGB appearance and depth geometry through a principled purify-then-fuse paradigm. CMAFNet consists of a Semantic Recomposition Module that performs dictionary-based feature purification via a learned codebook to suppress modality-specific noise while preserving defect-discriminative information, and a Contextual Semantic Integration Framework that captures global spatial dependencies using partial-channel attention to enhance structural semantic reasoning. Position-wise normalization within the purification stage enforces explicit reconstruction-driven cross-modal alignment, ensuring statistical compatibility between heterogeneous features prior to fusion. Extensive experiments on the TLRGBD benchmark, where 94.5% of instances are small objects, demonstrate that CMAFNet achieves 32.2% mAP@50 and 12.5% APs, outperforming the strongest baseline by 9.8 and 4.0 percentage points, respectively. A lightweight variant reaches 24.8% mAP50 at 228 FPS with only 4.9M parameters, surpassing all YOLO-based detectors while matching transformer-based methods at substantially lower computational cost.


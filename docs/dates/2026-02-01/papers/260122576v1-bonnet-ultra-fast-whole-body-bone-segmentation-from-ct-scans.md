---
layout: default
title: Bonnet: Ultra-fast whole-body bone segmentation from CT scans
---

# Bonnet: Ultra-fast whole-body bone segmentation from CT scans
**arXiv**：[2601.22576v1](https://arxiv.org/abs/2601.22576) · [PDF](https://arxiv.org/pdf/2601.22576.pdf)  
**作者**：Hanjiang Zhu, Pedro Martelleto Rezende, Zhang Yang, Tong Ye, Bruce Z. Gao, Feng Luo, Siyu Huang, Jiancheng Yang  

**一句话要点**：提出Bonnet超快速稀疏体积管道，用于CT扫描全身骨骼分割，以解决现有模型计算量大、耗时长的限制。

**关键词**：CT扫描, 骨骼分割, 稀疏卷积, 超快速推理, 3D医学图像, 手术规划

## 3 点简述
- 核心问题：现有3D体素模型如nnU-Net和STU-Net计算繁重，每扫描耗时数分钟，阻碍时间关键应用。
- 方法要点：集成HU阈值、基于稀疏卷积的U-Net补丁推理和多窗口融合，实现快速全体积预测。
- 实验或效果：在多个数据集上评估，达到高Dice分数，每扫描仅需2.69秒，推理时间减少约25倍。

## 摘要（原文）

> This work proposes Bonnet, an ultra-fast sparse-volume pipeline for whole-body bone segmentation from CT scans. Accurate bone segmentation is important for surgical planning and anatomical analysis, but existing 3D voxel-based models such as nnU-Net and STU-Net require heavy computation and often take several minutes per scan, which limits time-critical use. The proposed Bonnet addresses this by integrating a series of novel framework components including HU-based bone thresholding, patch-wise inference with a sparse spconv-based U-Net, and multi-window fusion into a full-volume prediction. Trained on TotalSegmentator and evaluated without additional tuning on RibSeg, CT-Pelvic1K, and CT-Spine1K, Bonnet achieves high Dice across ribs, pelvis, and spine while running in only 2.69 seconds per scan on an RTX A6000. Compared to strong voxel baselines, Bonnet attains a similar accuracy but reduces inference time by roughly 25x on the same hardware and tiling setup. The toolkit and pre-trained models will be released at https://github.com/HINTLab/Bonnet.


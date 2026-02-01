---
layout: default
title: BLO-Inst: Bi-Level Optimization Based Alignment of YOLO and SAM for Robust Instance Segmentation
---

# BLO-Inst: Bi-Level Optimization Based Alignment of YOLO and SAM for Robust Instance Segmentation
**arXiv**：[2601.22061v1](https://arxiv.org/abs/2601.22061) · [PDF](https://arxiv.org/pdf/2601.22061.pdf)  
**作者**：Li Zhang, Pengtao Xie  

**一句话要点**：提出BLO-Inst框架，通过双层优化对齐YOLO和SAM，实现鲁棒的实例分割自动化。

**关键词**：实例分割, 双层优化, YOLO, SAM, 自动化提示生成, 目标对齐

## 3 点简述
- 核心问题：SAM依赖手动提示，现有检测器集成存在目标不匹配和过拟合问题。
- 方法要点：采用双层优化，下层微调SAM，上层更新检测器以优化掩码质量。
- 实验或效果：在通用和生物医学任务中优于基线，提升分割性能。

## 摘要（原文）

> The Segment Anything Model has revolutionized image segmentation with its zero-shot capabilities, yet its reliance on manual prompts hinders fully automated deployment. While integrating object detectors as prompt generators offers a pathway to automation, existing pipelines suffer from two fundamental limitations: objective mismatch, where detectors optimized for geometric localization do not correspond to the optimal prompting context required by SAM, and alignment overfitting in standard joint training, where the detector simply memorizes specific prompt adjustments for training samples rather than learning a generalizable policy. To bridge this gap, we introduce BLO-Inst, a unified framework that aligns detection and segmentation objectives by bi-level optimization. We formulate the alignment as a nested optimization problem over disjoint data splits. In the lower level, the SAM is fine-tuned to maximize segmentation fidelity given the current detection proposals on a subset ($D_1$). In the upper level, the detector is updated to generate bounding boxes that explicitly minimize the validation loss of the fine-tuned SAM on a separate subset ($D_2$). This effectively transforms the detector into a segmentation-aware prompt generator, optimizing the bounding boxes not just for localization accuracy, but for downstream mask quality. Extensive experiments demonstrate that BLO-Inst achieves superior performance, outperforming standard baselines on tasks in general and biomedical domains.


---
layout: default
title: VOIC: Visible-Occluded Decoupling for Monocular 3D Semantic Scene Completion
---

# VOIC: Visible-Occluded Decoupling for Monocular 3D Semantic Scene Completion
**arXiv**：[2512.18954v1](https://arxiv.org/abs/2512.18954) · [PDF](https://arxiv.org/pdf/2512.18954.pdf)  
**作者**：Zaidao Han, Risa Higashita, Jiang Liu  

**一句话要点**：提出VOIC框架，通过可见-遮挡解耦解决单目3D语义场景补全中的特征干扰问题。

**关键词**：单目3D语义场景补全, 可见-遮挡解耦, 双解码器框架, 离线标签提取, 自动驾驶场景理解

## 3 点简述
- 核心问题：单目输入导致可见区域高置信度感知与遮挡区域低置信度推理相互干扰，引发特征稀释和错误传播。
- 方法要点：采用离线可见区域标签提取策略，分离监督，并设计双解码器框架分别处理可见区域语义感知和遮挡区域场景补全。
- 实验或效果：在SemanticKITTI和SSCBench-KITTI360基准上，几何补全和语义分割精度优于现有方法，达到先进水平。

## 摘要（原文）

> Camera-based 3D Semantic Scene Completion (SSC) is a critical task for autonomous driving and robotic scene understanding. It aims to infer a complete 3D volumetric representation of both semantics and geometry from a single image. Existing methods typically focus on end-to-end 2D-to-3D feature lifting and voxel completion. However, they often overlook the interference between high-confidence visible-region perception and low-confidence occluded-region reasoning caused by single-image input, which can lead to feature dilution and error propagation.
>   To address these challenges, we introduce an offline Visible Region Label Extraction (VRLE) strategy that explicitly separates and extracts voxel-level supervision for visible regions from dense 3D ground truth. This strategy purifies the supervisory space for two complementary sub-tasks: visible-region perception and occluded-region reasoning. Building on this idea, we propose the Visible-Occluded Interactive Completion Network (VOIC), a novel dual-decoder framework that explicitly decouples SSC into visible-region semantic perception and occluded-region scene completion. VOIC first constructs a base 3D voxel representation by fusing image features with depth-derived occupancy. The visible decoder focuses on generating high-fidelity geometric and semantic priors, while the occlusion decoder leverages these priors together with cross-modal interaction to perform coherent global scene reasoning.
>   Extensive experiments on the SemanticKITTI and SSCBench-KITTI360 benchmarks demonstrate that VOIC outperforms existing monocular SSC methods in both geometric completion and semantic segmentation accuracy, achieving state-of-the-art performance.


---
layout: default
title: Fusion4CA: Boosting 3D Object Detection via Comprehensive Image Exploitation
---

# Fusion4CA: Boosting 3D Object Detection via Comprehensive Image Exploitation
**arXiv**：[2603.05305v1](https://arxiv.org/abs/2603.05305) · [PDF](https://arxiv.org/pdf/2603.05305.pdf)  
**作者**：Kang Luo, Xin Chen, Yangyi Xiao, Hesheng Wang  

**一句话要点**：提出Fusion4CA以增强自动驾驶中基于BEV的3D物体检测，通过全面利用RGB信息提升性能。

**关键词**：3D物体检测, BEV融合, RGB信息利用, 对比对齐, 自动驾驶, nuScenes数据集

## 3 点简述
- 现有方法过度依赖LiDAR，RGB信息利用不足，导致检测性能受限。
- 引入对比对齐模块和相机辅助分支，校准图像特征并充分挖掘RGB信息。
- 在nuScenes数据集上仅用6个训练周期达到69.7% mAP，比基线提升1.2%。

## 摘要（原文）

> Nowadays, an increasing number of works fuse LiDAR and RGB data in the bird's-eye view (BEV) space for 3D object detection in autonomous driving systems. However, existing methods suffer from over-reliance on the LiDAR branch, with insufficient exploration of RGB information. To tackle this issue, we propose Fusion4CA, which is built upon the classic BEVFusion framework and dedicated to fully exploiting visual input with plug-and-play components. Specifically, a contrastive alignment module is designed to calibrate image features with 3D geometry, and a camera auxiliary branch is introduced to mine RGB information sufficiently during training. For further performance enhancement, we leverage an off-the-shelf cognitive adapter to make the most of pretrained image weights, and integrate a standard coordinate attention module into the fusion stage as a supplementary boost. Experiments on the nuScenes dataset demonstrate that our method achieves 69.7% mAP with only 6 training epochs and a mere 3.48% increase in inference parameters, yielding a 1.2% improvement over the baseline which is fully trained for 20 epochs. Extensive experiments in a simulated lunar environment further validate the effectiveness and generalization of our method. Our code will be released through Fusion4CA.


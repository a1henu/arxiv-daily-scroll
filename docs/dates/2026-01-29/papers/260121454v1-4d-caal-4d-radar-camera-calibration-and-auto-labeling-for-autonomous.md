---
layout: default
title: 4D-CAAL: 4D Radar-Camera Calibration and Auto-Labeling for Autonomous Driving
---

# 4D-CAAL: 4D Radar-Camera Calibration and Auto-Labeling for Autonomous Driving
**arXiv**：[2601.21454v1](https://arxiv.org/abs/2601.21454) · [PDF](https://arxiv.org/pdf/2601.21454.pdf)  
**作者**：Shanliang Yao, Zhuoxiao Li, Runwei Guan, Kebin Cao, Meng Xia, Fuping Hu, Sen Xu, Yong Yue, Xiaohui Zhu, Weiping Ding, Ryan Wen Liu  

**一句话要点**：提出4D-CAAL框架以解决4D雷达-相机标定与自动标注问题

**关键词**：4D雷达标定, 传感器融合, 自动标注, 多模态感知, 自动驾驶

## 3 点简述
- 核心问题：现有标定方法使用分离目标，难以建立对应关系；雷达数据稀疏，手动标注费时且不可靠。
- 方法要点：设计双用途标定目标，结合棋盘格和角反射器；开发对应匹配算法，实现精确外参标定；利用标定关系通过几何投影和多特征优化进行自动标注。
- 实验或效果：实验表明方法标定精度高，显著减少手动标注工作量，加速多模态感知系统开发。

## 摘要（原文）

> 4D radar has emerged as a critical sensor for autonomous driving, primarily due to its enhanced capabilities in elevation measurement and higher resolution compared to traditional 3D radar. Effective integration of 4D radar with cameras requires accurate extrinsic calibration, and the development of radar-based perception algorithms demands large-scale annotated datasets. However, existing calibration methods often employ separate targets optimized for either visual or radar modalities, complicating correspondence establishment. Furthermore, manually labeling sparse radar data is labor-intensive and unreliable. To address these challenges, we propose 4D-CAAL, a unified framework for 4D radar-camera calibration and auto-labeling. Our approach introduces a novel dual-purpose calibration target design, integrating a checkerboard pattern on the front surface for camera detection and a corner reflector at the center of the back surface for radar detection. We develop a robust correspondence matching algorithm that aligns the checkerboard center with the strongest radar reflection point, enabling accurate extrinsic calibration. Subsequently, we present an auto-labeling pipeline that leverages the calibrated sensor relationship to transfer annotations from camera-based segmentations to radar point clouds through geometric projection and multi-feature optimization. Extensive experiments demonstrate that our method achieves high calibration accuracy while significantly reducing manual annotation effort, thereby accelerating the development of robust multi-modal perception systems for autonomous driving.


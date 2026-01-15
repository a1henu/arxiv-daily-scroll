---
layout: default
title: AquaFeat+: an Underwater Vision Learning-based Enhancement Method for Object Detection, Classification, and Tracking
---

# AquaFeat+: an Underwater Vision Learning-based Enhancement Method for Object Detection, Classification, and Tracking
**arXiv**：[2601.09652v1](https://arxiv.org/abs/2601.09652) · [PDF](https://arxiv.org/pdf/2601.09652.pdf)  
**作者**：Emanuel da Costa Silva, Tatiana Taís Schein, José David García Ramos, Eduardo Lawson da Silva, Stephanie Loi Brião, Felipe Gomes de Oliveira, Paulo Lilles Jorge Drews-Jr  

**一句话要点**：提出AquaFeat+以增强水下机器人视觉任务中的特征提取

**关键词**：水下视觉增强, 特征提取, 端到端训练, 目标检测, 机器人感知

## 3 点简述
- 核心问题：水下视频分析受低光照、颜色失真和浑浊度影响，降低感知模块性能。
- 方法要点：采用端到端训练的插件式管道，包括颜色校正、分层特征增强和自适应残差输出模块。
- 实验或效果：在FishTrack23数据集上训练评估，显著提升目标检测、分类和跟踪指标。

## 摘要（原文）

> Underwater video analysis is particularly challenging due to factors such as low lighting, color distortion, and turbidity, which compromise visual data quality and directly impact the performance of perception modules in robotic applications. This work proposes AquaFeat+, a plug-and-play pipeline designed to enhance features specifically for automated vision tasks, rather than for human perceptual quality. The architecture includes modules for color correction, hierarchical feature enhancement, and an adaptive residual output, which are trained end-to-end and guided directly by the loss function of the final application. Trained and evaluated in the FishTrack23 dataset, AquaFeat+ achieves significant improvements in object detection, classification, and tracking metrics, validating its effectiveness for enhancing perception tasks in underwater robotic applications.


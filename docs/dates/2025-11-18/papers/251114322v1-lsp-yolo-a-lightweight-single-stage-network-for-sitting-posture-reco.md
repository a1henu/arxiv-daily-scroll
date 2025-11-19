---
layout: default
title: LSP-YOLO: A Lightweight Single-Stage Network for Sitting Posture Recognition on Embedded Devices
---

# LSP-YOLO: A Lightweight Single-Stage Network for Sitting Posture Recognition on Embedded Devices
**arXiv**：[2511.14322v1](https://arxiv.org/abs/2511.14322) · [PDF](https://arxiv.org/pdf/2511.14322.pdf)  
**作者**：Nanjun Li, Ziyue Hao, Quanqiang Wang, Xuanyin Wang  

**一句话要点**：提出LSP-YOLO轻量单阶段网络，用于嵌入式设备坐姿识别，提升效率与实时性。

**关键词**：坐姿识别, 轻量网络, 嵌入式设备, 单阶段检测, 姿态估计

## 3 点简述
- 核心问题：现有坐姿识别方法计算密集、实时性差，不适用于嵌入式设备。
- 方法要点：集成PConv和SimAM设计Light-C3k2模块，降低计算成本并保持特征提取能力。
- 实验效果：在PC上模型准确率达94.2%，帧率251 FPS，模型大小仅1.9 MB。

## 摘要（原文）

> With the rise in sedentary behavior, health problems caused by poor sitting posture have drawn increasing attention. Most existing methods, whether using invasive sensors or computer vision, rely on two-stage pipelines, which result in high intrusiveness, intensive computation, and poor real-time performance on embedded edge devices. Inspired by YOLOv11-Pose, a lightweight single-stage network for sitting posture recognition on embedded edge devices termed LSP-YOLO was proposed. By integrating partial convolution(PConv) and Similarity-Aware Activation Module(SimAM), a lightweight module, Light-C3k2, was designed to reduce computational cost while maintaining feature extraction capability. In the recognition head, keypoints were directly mapped to posture classes through pointwise convolution, and intermediate supervision was employed to enable efficient fusion of pose estimation and classification. Furthermore, a dataset containing 5,000 images across six posture categories was constructed for model training and testing. The smallest trained model, LSP-YOLO-n, achieved 94.2% accuracy and 251 Fps on personal computer(PC) with a model size of only 1.9 MB. Meanwhile, real-time and high-accuracy inference under constrained computational resources was demonstrated on the SV830C + GC030A platform. The proposed approach is characterized by high efficiency, lightweight design and deployability, making it suitable for smart classrooms, rehabilitation, and human-computer interaction applications.


---
layout: default
title: DexEMG: Towards Dexterous Teleoperation System via EMG2Pose Generalization
---

# DexEMG: Towards Dexterous Teleoperation System via EMG2Pose Generalization
**arXiv**：[2603.05861v1](https://arxiv.org/abs/2603.05861) · [PDF](https://arxiv.org/pdf/2603.05861.pdf)  
**作者**：Qianyou Zhao, Wenqiao Li, Chiyu Wang, Kaifeng Zhang  

**一句话要点**：提出DexEMG系统，利用表面肌电信号实现灵巧机器人手的高保真远程操作

**关键词**：表面肌电信号, 远程操作, 手部姿态预测, 机器人手控制, 泛化能力, 实时重定向

## 3 点简述
- 核心问题：现有远程操作系统在性能与便携性间存在权衡，如视觉系统成本高、机械外骨骼笨重。
- 方法要点：通过收集肌电信号与手部姿态同步数据，训练EMG2Pose神经网络直接预测手部运动学，并开发实时手部重定向算法。
- 实验或效果：系统在多样化远程操作任务中实现高精度，并展现出对新物体和复杂环境的强泛化能力，无需大量个体校准。

## 摘要（原文）

> High-fidelity teleoperation of dexterous robotic hands is essential for bringing robots into unstructured domestic environments. However, existing teleoperation systems often face a trade-off between performance and portability: vision-based capture systems are constrained by costs and line-of-sight requirements, while mechanical exoskeletons are bulky and physically restrictive. In this paper, we present DexEMG, a lightweight and cost-effective teleoperation system leveraging surface electromyography (sEMG) to bridge the gap between human intent and robotic execution. We first collect a synchronized dataset of sEMG signals and hand poses via a MoCap glove to train EMG2Pose, a neural network capable of continuously predicting hand kinematics directly from muscle activity. To ensure seamless control, we develop a robust hand retargeting algorithm that maps the predicted poses onto a multi-fingered dexterous hand in real-time. Experimental results demonstrate that DexEMG achieves high precision in diverse teleoperation tasks. Notably, our system exhibits strong generalization capabilities across novel objects and complex environments without the need for intensive individual-specific recalibration. This work offers a scalable and intuitive interface for both general-purpose robotic manipulation and assistive technologies.


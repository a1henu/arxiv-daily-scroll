---
layout: default
title: Stable Offline Hand-Eye Calibration for any Robot with Just One Mark
---

# Stable Offline Hand-Eye Calibration for any Robot with Just One Mark
**arXiv**：[2511.17001v1](https://arxiv.org/abs/2511.17001) · [PDF](https://arxiv.org/pdf/2511.17001.pdf)  
**作者**：Sicheng Xie, Lingchen Meng, Zhiying Du, Shuyuan Tu, Haidong Cao, Jiaqi Leng, Zuxuan Wu, Yu-Gang Jiang  

**一句话要点**：提出CalibAll方法，仅需单一标记实现稳定离线手眼标定

**关键词**：手眼标定, 相机外参估计, 视觉基础模型, 离线校准, 机器人视觉

## 3 点简述
- 核心问题：机器人手眼标定中相机外参估计常不可用，现有方法易陷局部最优且泛化差
- 方法要点：利用视觉基础模型定位标记，结合点跟踪与3D轨迹，通过粗到精流程优化外参
- 实验或效果：在三个机器人平台上超越先进方法，展现强鲁棒性和通用性

## 摘要（原文）

> Imitation learning has achieved remarkable success in a variety of robotic tasks by learning a mapping function from camera-space observations to robot-space actions. Recent work indicates that the use of robot-to-camera transformation information ({\ie}, camera extrinsics) benefits the learning process and produces better results. However, camera extrinsics are oftentimes unavailable and estimation methods usually suffer from local minima and poor generalizations. In this paper, we present CalibAll, a simple yet effective method that \textbf{requires only a single mark} and performs training-free, stable, and accurate camera extrinsic estimation across diverse robots and datasets through a coarse-to-fine calibration pipeline. In particular, we annotate a single mark on an end-effector (EEF), and leverage the correspondence ability emerged from vision foundation models (VFM) to automatically localize the corresponding mark across robots in diverse datasets. Using this mark, together with point tracking and the 3D EEF trajectory, we obtain a coarse camera extrinsic via temporal Perspective-n-Point (PnP). This estimate is further refined through a rendering-based optimization that aligns rendered and ground-true masks, yielding accurate and stable camera extrinsic. Experimental results demonstrate that our method outperforms state-of-the-art approaches, showing strong robustness and general effectiveness across three robot platforms. It also produces useful auxiliary annotations such as depth maps, link-wise masks, and end-effector 2D trajectories, which can further support downstream tasks.


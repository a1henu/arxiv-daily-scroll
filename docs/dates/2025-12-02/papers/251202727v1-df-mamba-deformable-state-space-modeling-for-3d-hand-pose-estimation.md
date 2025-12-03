---
layout: default
title: DF-Mamba: Deformable State Space Modeling for 3D Hand Pose Estimation in Interactions
---

# DF-Mamba: Deformable State Space Modeling for 3D Hand Pose Estimation in Interactions
**arXiv**：[2512.02727v1](https://arxiv.org/abs/2512.02727) · [PDF](https://arxiv.org/pdf/2512.02727.pdf)  
**作者**：Yifan Zhou, Takehiko Ohkawa, Guwenxiao Zhou, Kanoko Goto, Takumi Hirose, Yusuke Sekikawa, Nakamasa Inoue  

**一句话要点**：提出DF-Mamba框架，通过可变形状态空间建模解决交互中3D手部姿态估计的遮挡问题

**关键词**：3D手部姿态估计, 状态空间建模, 可变形扫描, 遮挡处理, 全局上下文学习, 交互场景

## 3 点简述
- 核心问题：日常手部交互中严重遮挡（如双手重叠）导致3D手部姿态估计困难，需增强局部与全局特征关系学习
- 方法要点：基于Mamba的状态空间建模，引入可变形状态扫描，选择性聚合局部特征以捕获全局上下文
- 实验或效果：在五个数据集上评估，优于VMamba和Spatial-Mamba等最新骨干网络，达到最先进性能，推理速度与ResNet-50相当

## 摘要（原文）

> Modeling daily hand interactions often struggles with severe occlusions, such as when two hands overlap, which highlights the need for robust feature learning in 3D hand pose estimation (HPE). To handle such occluded hand images, it is vital to effectively learn the relationship between local image features (e.g., for occluded joints) and global context (e.g., cues from inter-joints, inter-hands, or the scene). However, most current 3D HPE methods still rely on ResNet for feature extraction, and such CNN's inductive bias may not be optimal for 3D HPE due to its limited capability to model the global context. To address this limitation, we propose an effective and efficient framework for visual feature extraction in 3D HPE using recent state space modeling (i.e., Mamba), dubbed Deformable Mamba (DF-Mamba). DF-Mamba is designed to capture global context cues beyond standard convolution through Mamba's selective state modeling and the proposed deformable state scanning. Specifically, for local features after convolution, our deformable scanning aggregates these features within an image while selectively preserving useful cues that represent the global context. This approach significantly improves the accuracy of structured 3D HPE, with comparable inference speed to ResNet-50. Our experiments involve extensive evaluations on five divergent datasets including single-hand and two-hand scenarios, hand-only and hand-object interactions, as well as RGB and depth-based estimation. DF-Mamba outperforms the latest image backbones, including VMamba and Spatial-Mamba, on all datasets and achieves state-of-the-art performance.


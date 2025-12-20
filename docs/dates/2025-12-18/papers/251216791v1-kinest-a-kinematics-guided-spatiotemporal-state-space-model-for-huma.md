---
layout: default
title: KineST: A Kinematics-guided Spatiotemporal State Space Model for Human Motion Tracking from Sparse Signals
---

# KineST: A Kinematics-guided Spatiotemporal State Space Model for Human Motion Tracking from Sparse Signals
**arXiv**：[2512.16791v1](https://arxiv.org/abs/2512.16791) · [PDF](https://arxiv.org/pdf/2512.16791.pdf)  
**作者**：Shuting Zhao, Zeyu Xiao, Xinrong Chen  

**一句话要点**：提出KineST模型，基于稀疏信号实现AR/VR中全身运动跟踪，提升准确性与时间一致性。

**关键词**：全身运动跟踪, 稀疏信号重建, 状态空间模型, 时空依赖, AR/VR应用, 运动学引导

## 3 点简述
- 问题：AR/VR中基于头戴设备稀疏信号重建全身姿态时，现有方法难以平衡准确性、时间连贯性和效率。
- 方法：采用运动学引导的双向扫描策略和混合时空表示学习，紧密耦合时空上下文，并引入几何角速度损失增强稳定性。
- 效果：在轻量级框架下，实验显示KineST在准确性和时间一致性方面表现优越。

## 摘要（原文）

> Full-body motion tracking plays an essential role in AR/VR applications, bridging physical and virtual interactions. However, it is challenging to reconstruct realistic and diverse full-body poses based on sparse signals obtained by head-mounted displays, which are the main devices in AR/VR scenarios. Existing methods for pose reconstruction often incur high computational costs or rely on separately modeling spatial and temporal dependencies, making it difficult to balance accuracy, temporal coherence, and efficiency. To address this problem, we propose KineST, a novel kinematics-guided state space model, which effectively extracts spatiotemporal dependencies while integrating local and global pose perception. The innovation comes from two core ideas. Firstly, in order to better capture intricate joint relationships, the scanning strategy within the State Space Duality framework is reformulated into kinematics-guided bidirectional scanning, which embeds kinematic priors. Secondly, a mixed spatiotemporal representation learning approach is employed to tightly couple spatial and temporal contexts, balancing accuracy and smoothness. Additionally, a geometric angular velocity loss is introduced to impose physically meaningful constraints on rotational variations for further improving motion stability. Extensive experiments demonstrate that KineST has superior performance in both accuracy and temporal consistency within a lightweight framework. Project page: https://kaka-1314.github.io/KineST/


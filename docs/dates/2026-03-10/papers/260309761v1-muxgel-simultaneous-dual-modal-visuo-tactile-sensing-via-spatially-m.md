---
layout: default
title: MuxGel: Simultaneous Dual-Modal Visuo-Tactile Sensing via Spatially Multiplexing and Deep Reconstruction
---

# MuxGel: Simultaneous Dual-Modal Visuo-Tactile Sensing via Spatially Multiplexing and Deep Reconstruction
**arXiv**：[2603.09761v1](https://arxiv.org/abs/2603.09761) · [PDF](https://arxiv.org/pdf/2603.09761.pdf)  
**作者**：Zhixian Hu, Zhengtong Xu, Sheeraz Athar, Juan Wachs, Yu She  

**一句话要点**：提出MuxGel传感器，通过空间复用和深度重建实现同时视觉-触觉感知，解决不透明涂层阻碍预接触视觉的问题。

**关键词**：视觉触觉传感器, 空间复用, 深度重建, 机器人操作, 多模态感知, 仿真到真实迁移

## 3 点简述
- 核心问题：传统视觉触觉传感器因不透明涂层在触觉感知时阻挡外部视觉，限制机器人精确操作。
- 方法要点：采用棋盘格涂层模式，空间复用透明窗口和触觉敏感区域，结合U-Net重建框架从单摄像头恢复全分辨率视觉和触觉信号。
- 实验或效果：在未见物体上验证泛化能力，应用于抓取任务，提升感知性能并保持硬件兼容性。

## 摘要（原文）

> High-fidelity visuo-tactile sensing is important for precise robotic manipulation. However, most vision-based tactile sensors face a fundamental trade-off: opaque coatings enable tactile sensing but block pre-contact vision. To address this, we propose MuxGel, a spatially multiplexed sensor that captures both external visual information and contact-induced tactile signals through a single camera. By using a checkerboard coating pattern, MuxGel interleaves tactile-sensitive regions with transparent windows for external vision. This design maintains standard form factors, allowing for plug-and-play integration into GelSight-style sensors by simply replacing the gel pad. To recover full-resolution vision and tactile signals from the multiplexed inputs, we develop a U-Net-based reconstruction framework. Leveraging a sim-to-real pipeline, our model effectively decouples and restores high-fidelity tactile and visual fields simultaneously. Experiments on unseen objects demonstrate the framework's generalization and accuracy. Furthermore, we demonstrate MuxGel's utility in grasping tasks, where dual-modality feedback facilitates both pre-contact alignment and post-contact interaction. Results show that MuxGel enhances the perceptual capabilities of existing vision-based tactile sensors while maintaining compatibility with their hardware stacks. Project webpage: https://zhixianhu.github.io/muxgel/.


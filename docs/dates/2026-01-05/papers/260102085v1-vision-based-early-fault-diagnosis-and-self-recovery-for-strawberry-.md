---
layout: default
title: Vision-Based Early Fault Diagnosis and Self-Recovery for Strawberry Harvesting Robots
---

# Vision-Based Early Fault Diagnosis and Self-Recovery for Strawberry Harvesting Robots
**arXiv**：[2601.02085v1](https://arxiv.org/abs/2601.02085) · [PDF](https://arxiv.org/pdf/2601.02085.pdf)  
**作者**：Meili Sun, Chunjiang Zhao, Lichao Yang, Hao Liu, Shimin Hu, Ya Xiong  

**一句话要点**：提出视觉故障诊断与自恢复框架，以提升草莓采摘机器人的稳定性和效率。

**关键词**：草莓采摘机器人, 视觉故障诊断, 多任务感知, 自恢复控制, 实时视觉反馈

## 3 点简述
- 核心问题：草莓采摘机器人存在视觉感知集成度低、位置偏差、空抓和果实滑落等问题，影响稳定性。
- 方法要点：基于SRR-Net多任务感知模型，结合误差补偿和早期中止策略，实现故障诊断与自恢复。
- 实验效果：SRR-Net在检测、分割和成熟度估计中保持高精度，推理速度达163.35 FPS。

## 摘要（原文）

> Strawberry harvesting robots faced persistent challenges such as low integration of visual perception, fruit-gripper misalignment, empty grasping, and strawberry slippage from the gripper due to insufficient gripping force, all of which compromised harvesting stability and efficiency in orchard environments. To overcome these issues, this paper proposed a visual fault diagnosis and self-recovery framework that integrated multi-task perception with corrective control strategies. At the core of this framework was SRR-Net, an end-to-end multi-task perception model that simultaneously performed strawberry detection, segmentation, and ripeness estimation, thereby unifying visual perception with fault diagnosis. Based on this integrated perception, a relative error compensation method based on the simultaneous target-gripper detection was designed to address positional misalignment, correcting deviations when error exceeded the tolerance threshold. To mitigate empty grasping and fruit-slippage faults, an early abort strategy was implemented. A micro-optical camera embedded in the end-effector provided real-time visual feedback, enabling grasp detection during the deflating stage and strawberry slip prediction during snap-off through MobileNet V3-Small classifier and a time-series LSTM classifier. Experiments demonstrated that SRR-Net maintained high perception accuracy. For detection, it achieved a precision of 0.895 and recall of 0.813 on strawberries, and 0.972/0.958 on hands. In segmentation, it yielded a precision of 0.887 and recall of 0.747 for strawberries, and 0.974/0.947 for hands. For ripeness estimation, SRR-Net attained a mean absolute error of 0.035, while simultaneously supporting multi-task perception and sustaining a competitive inference speed of 163.35 FPS.


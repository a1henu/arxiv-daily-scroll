---
layout: default
title: Scalable Injury-Risk Screening in Baseball Pitching From Broadcast Video
---

# Scalable Injury-Risk Screening in Baseball Pitching From Broadcast Video
**arXiv**：[2603.04864v1](https://arxiv.org/abs/2603.04864) · [PDF](https://arxiv.org/pdf/2603.04864.pdf)  
**作者**：Jerrin Bright, Justin Mende, John Zelek  

**一句话要点**：提出基于单目广播视频的棒球投球损伤风险筛查方法，以替代昂贵多相机系统。

**关键词**：单目视频分析, 生物力学恢复, 损伤风险预测, 运动学细化, 棒球投球, 广播视频处理

## 3 点简述
- 核心问题：棒球投球损伤预测依赖精确生物力学信号，但专业多相机系统成本高且难以普及。
- 方法要点：通过漂移控制全局提升模块和运动学细化管道，从广播视频恢复18个临床相关生物力学指标。
- 实验或效果：在13名职业投手数据上，16/18指标误差小于1度，损伤预测模型AUC达0.811-0.825。

## 摘要（原文）

> Injury prediction in pitching depends on precise biomechanical signals, yet gold-standard measurements come from expensive, stadium-installed multi-camera systems that are unavailable outside professional venues. We present a monocular video pipeline that recovers 18 clinically relevant biomechanics metrics from broadcast footage, positioning pose-derived kinematics as a scalable source for injury-risk modeling. Built on DreamPose3D, our approach introduces a drift-controlled global lifting module that recovers pelvis trajectory via velocity-based parameterization and sliding-window inference, lifting pelvis-rooted poses into global space. To address motion blur, compression artifacts, and extreme pitching poses, we incorporate a kinematics refinement pipeline with bone-length constraints, joint-limited inverse kinematics, smoothing, and symmetry constraints to ensure temporally stable and physically plausible kinematics. On 13 professional pitchers (156 paired pitches), 16/18 metrics achieve sub-degree agreement (MAE $< 1^{\circ}$). Using these metrics for injury prediction, an automated screening model achieves AUC 0.811 for Tommy John surgery and 0.825 for significant arm injuries on 7,348 pitchers. The resulting pose-derived metrics support scalable injury-risk screening, establishing monocular broadcast video as a viable alternative to stadium-scale motion capture for biomechanics.


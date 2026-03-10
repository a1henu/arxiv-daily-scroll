---
layout: default
title: Omnidirectional Humanoid Locomotion on Stairs via Unsafe Stepping Penalty and Sparse LiDAR Elevation Mapping
---

# Omnidirectional Humanoid Locomotion on Stairs via Unsafe Stepping Penalty and Sparse LiDAR Elevation Mapping
**arXiv**：[2603.07928v1](https://arxiv.org/abs/2603.07928) · [PDF](https://arxiv.org/pdf/2603.07928.pdf)  
**作者**：Yuzhi Jiang, Yujun Liang, Junhao Li, Han Ding, Lijun Zhu  

**一句话要点**：提出密集不安全步态惩罚与稀疏LiDAR高程映射，实现人形机器人全向楼梯安全行走

**关键词**：人形机器人行走, 楼梯导航, 不安全步态惩罚, 稀疏LiDAR映射, 高程图重建, 仿真到真实迁移

## 3 点简述
- 核心问题：人形机器人楼梯行走存在盲区和不安全步态惩罚稀疏，导致全向移动受限和学习效率低。
- 方法要点：引入密集不安全步态惩罚提供连续反馈，并构建滚动点云映射系统结合EGAU网络优化高程图重建。
- 实验或效果：仿真中接近100%安全步态率，真实部署保持高安全率，完成复杂户外地形长距离行走测试。

## 摘要（原文）

> Humanoid robots, characterized by numerous degrees of freedom and a high center of gravity, are inherently unstable. Safe omnidirectional locomotion on stairs requires both omnidirectional terrain perception and reliable foothold selection. Existing methods often rely on forward-facing depth cameras, which create blind zones that restrict omnidirectional mobility. Furthermore, sparse post-contact unsafe stepping penalties lead to low learning efficiency and suboptimal strategies. To realize safe stair-traversal gaits, this paper introduces a single-stage training framework incorporating a dense unsafe stepping penalty that provides continuous feedback as the foot approaches a hazardous placement. To obtain stable and reliable elevation maps, we build a rolling point-cloud mapping system with spatiotemporal confidence decay and a self-protection zone mechanism, producing temporally consistent local maps. These maps are further refined by an Edge-Guided Asymmetric U-Net (EGAU), which mitigates reconstruction distortion caused by sparse LiDAR returns on stair risers. Simulation and real-robot experiments show that the proposed method achieves a near-100\% safe stepping rate on stair terrains in simulation, while maintaining a remarkably high safe stepping rate in real-world deployments. Furthermore, it completes a continuous long-distance walking test on complex outdoor terrains, demonstrating reliable sim-to-real transfer and long-term stability.


---
layout: default
title: Sim2Sea: Sim-to-Real Policy Transfer for Maritime Vessel Navigation in Congested Waters
---

# Sim2Sea: Sim-to-Real Policy Transfer for Maritime Vessel Navigation in Congested Waters
**arXiv**：[2603.04057v1](https://arxiv.org/abs/2603.04057) · [PDF](https://arxiv.org/pdf/2603.04057.pdf)  
**作者**：Xinyu Cui, Xuanfa Jin, Xue Yan, Yongcheng Zeng, Luoyang Sun, Siying Wei, Ruizhi Zhang, Jian Zhao, Haifeng Zhang, Jun Wang  

**一句话要点**：提出Sim2Sea框架，通过仿真到真实策略迁移解决拥挤水域船舶自主导航问题。

**关键词**：仿真到真实迁移, 船舶自主导航, 拥挤水域, 双流时空策略, 域随机化, GPU加速仿真

## 3 点简述
- 核心问题：拥挤水域自主导航存在仿真到真实差距，源于仿真不精确、态势感知不足和不安全探索。
- 方法要点：开发GPU加速并行仿真器，设计双流时空策略结合速度障碍引导动作掩码，采用针对性域随机化。
- 实验或效果：仿真中收敛更快、轨迹更安全，零样本迁移至17吨无人船在真实拥挤水域成功导航。

## 摘要（原文）

> Autonomous navigation in congested maritime environments is a critical capability for a wide range of real-world applications. However, it remains an unresolved challenge due to complex vessel interactions and significant environmental uncertainties. Existing methods often fail in practical deployment due to a substantial sim-to-real gap, which stems from imprecise simulation, inadequate situational awareness, and unsafe exploration strategies. To address these, we propose \textbf{Sim2Sea}, a comprehensive framework designed to bridge simulation and real-world execution. Sim2Sea advances in three key aspects. First, we develop a GPU-accelerated parallel simulator for scalable and accurate maritime scenario simulation. Second, we design a dual-stream spatiotemporal policy that handles complex dynamics and multi-modal perception, augmented with a velocity-obstacle-guided action masking mechanism to ensure safe and efficient exploration. Finally, a targeted domain randomization scheme helps bridge the sim-to-real gap. Simulation results demonstrate that our method achieves faster convergence and safer trajectories than established baselines. In addition, our policy trained purely in simulation successfully transfers zero-shot to a 17-ton unmanned vessel operating in real-world congested waters. These results validate the effectiveness of Sim2Sea in achieving reliable sim-to-real transfer for practical autonomous maritime navigation.


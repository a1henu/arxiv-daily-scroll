---
layout: default
title: DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints
---

# DWPP: Dynamic Window Pure Pursuit Considering Velocity and Acceleration Constraints
**arXiv**：[2601.15006v1](https://arxiv.org/abs/2601.15006) · [PDF](https://arxiv.org/pdf/2601.15006.pdf)  
**作者**：Fumiya Ohnishi, Masaki Takahashi  

**一句话要点**：提出动态窗口纯追踪方法以解决移动机器人路径跟踪中的速度与加速度约束问题

**关键词**：移动机器人, 路径跟踪, 纯追踪算法, 动态窗口, 速度约束, 加速度约束

## 3 点简述
- 核心问题：传统纯追踪方法未显式考虑速度与加速度约束，导致指令与实际速度不符，引发超调和跟踪性能下降。
- 方法要点：在速度空间（v-ω平面）中重新定义指令速度计算，通过动态窗口选择最接近ω=κv线的点，显式融入约束。
- 实验或效果：实验表明DWPP避免违反约束的指令，相比传统方法实现更优的路径跟踪精度，并已集成至Nav2官方库。

## 摘要（原文）

> Pure pursuit and its variants are widely used for mobile robot path tracking owing to their simplicity and computational efficiency. However, many conventional approaches do not explicitly account for velocity and acceleration constraints, resulting in discrepancies between commanded and actual velocities that result in overshoot and degraded tracking performance. To address this problem, this paper proposes dynamic window pure pursuit (DWPP), which fundamentally reformulates the command velocity computation process to explicitly incorporate velocity and acceleration constraints. Specifically, DWPP formulates command velocity computation in the velocity space (the $v$-$ω$ plane) and selects the command velocity as the point within the dynamic window that is closest to the line $ω= κv$. Experimental results demonstrate that DWPP avoids constraint-violating commands and achieves superior path-tracking accuracy compared with conventional pure pursuit methods. The proposed method has been integrated into the official Nav2 repository and is publicly available (https://github.com/ros-navigation/navigation2).


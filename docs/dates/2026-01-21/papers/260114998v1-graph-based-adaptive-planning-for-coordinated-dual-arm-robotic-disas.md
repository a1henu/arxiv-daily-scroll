---
layout: default
title: Graph-Based Adaptive Planning for Coordinated Dual-Arm Robotic Disassembly of Electronic Devices (eGRAP)
---

# Graph-Based Adaptive Planning for Coordinated Dual-Arm Robotic Disassembly of Electronic Devices (eGRAP)
**arXiv**：[2601.14998v1](https://arxiv.org/abs/2601.14998) · [PDF](https://arxiv.org/pdf/2601.14998.pdf)  
**作者**：Adip Ranjan Das, Maria Koskinopoulou  

**一句话要点**：提出电子设备图基自适应规划方法，用于双机器人臂协同拆卸电子设备。

**关键词**：双机器人臂协同, 图基规划, 电子设备拆卸, 自适应调度, 视觉引导

## 3 点简述
- 核心问题：电子废弃物快速增长，回收率低，需自动化拆卸解决方案。
- 方法要点：集成视觉、动态规划和双臂执行，基于有向图编码拆卸顺序，实现自适应调度。
- 实验或效果：在3.5英寸硬盘上验证，成功完成全拆卸，高效协调双臂实时任务。

## 摘要（原文）

> E-waste is growing rapidly while recycling rates remain low. We propose an electronic-device Graph-based Adaptive Planning (eGRAP) that integrates vision, dynamic planning, and dual-arm execution for autonomous disassembly. A camera-equipped arm identifies parts and estimates their poses, and a directed graph encodes which parts must be removed first. A scheduler uses topological ordering of this graph to select valid next steps and assign them to two robot arms, allowing independent tasks to run in parallel. One arm carries a screwdriver (with an eye-in-hand depth camera) and the other holds or handles components. We demonstrate eGRAP on 3.5in hard drives: as parts are unscrewed and removed, the system updates its graph and plan online. Experiments show consistent full disassembly of each HDD, with high success rates and efficient cycle times, illustrating the method's ability to adaptively coordinate dual-arm tasks in real time.


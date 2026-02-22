---
layout: default
title: Bluetooth Phased-array Aided Inertial Navigation Using Factor Graphs: Experimental Verification
---

# Bluetooth Phased-array Aided Inertial Navigation Using Factor Graphs: Experimental Verification
**arXiv**：[2602.17407v1](https://arxiv.org/abs/2602.17407) · [PDF](https://arxiv.org/pdf/2602.17407.pdf)  
**作者**：Glen Hjelmerud Mørkbak Sørensen, Torleiv H. Bryne, Kristoffer Gryte, Tor Arne Johansen  

**一句话要点**：提出基于因子图的蓝牙相控阵辅助惯性导航方法，用于GNSS拒止场景如仓库物流。

**关键词**：蓝牙相控阵, 因子图优化, 惯性导航, GNSS拒止, 无人机导航, 稳健估计

## 3 点简述
- 核心问题：在GNSS拒止场景下，低成本蓝牙相控阵系统测量噪声大、范围短，需稳健导航方案。
- 方法要点：采用因子图优化估计器，结合蓝牙角度测量、距离或气压数据辅助惯性导航。
- 实验或效果：通过多旋翼无人机飞行实验数据，评估不同辅助测量在GNSS丢失时的性能表现。

## 摘要（原文）

> Phased-array Bluetooth systems have emerged as a low-cost alternative for performing aided inertial navigation in GNSS-denied use cases such as warehouse logistics, drone landings, and autonomous docking. Basing a navigation system off of commercial-off-the-shelf components may reduce the barrier of entry for phased-array radio navigation systems, albeit at the cost of significantly noisier measurements and relatively short feasible range. In this paper, we compare robust estimation strategies for a factor graph optimisation-based estimator using experimental data collected from multirotor drone flight. We evaluate performance in loss-of-GNSS scenarios when aided by Bluetooth angular measurements, as well as range or barometric pressure.


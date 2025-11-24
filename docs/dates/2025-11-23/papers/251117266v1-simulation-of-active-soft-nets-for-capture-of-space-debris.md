---
layout: default
title: Simulation of Active Soft Nets for Capture of Space Debris
---

# Simulation of Active Soft Nets for Capture of Space Debris
**arXiv**：[2511.17266v1](https://arxiv.org/abs/2511.17266) · [PDF](https://arxiv.org/pdf/2511.17266.pdf)  
**作者**：Leone Costi, Dario Izzo  

**一句话要点**：提出基于MuJoCo的软网模拟器，用于空间碎片自主捕获

**关键词**：软机器人, 空间碎片捕获, 物理模拟, 滑模控制, 轨道力学

## 3 点简述
- 核心问题：空间碎片自主捕获，需模拟软网动态与轨道力学
- 方法要点：集成软网动态、接触模型和控制器，支持不同柔顺度
- 实验或效果：软网与滑模控制器结合，捕获成功率100%，接触点更多

## 摘要（原文）

> In this work, we propose a simulator, based on the open-source physics engine MuJoCo, for the design and control of soft robotic nets for the autonomous removal of space debris. The proposed simulator includes net dynamics, contact between the net and the debris, self-contact of the net, orbital mechanics, and a controller that can actuate thrusters on the four satellites at the corners of the net. It showcases the case of capturing Envisat, a large ESA satellite that remains in orbit as space debris following the end of its mission. This work investigates different mechanical models, which can be used to simulate the net dynamics, simulating various degrees of compliance, and different control strategies to achieve the capture of the debris, depending on the relative position of the net and the target. Unlike previous works on this topic, we do not assume that the net has been previously ballistically thrown toward the target, and we start from a relatively static configuration. The results show that a more compliant net achieves higher performance when attempting the capture of Envisat. Moreover, when paired with a sliding mode controller, soft nets are able to achieve successful capture in 100% of the tested cases, whilst also showcasing a higher effective area at contact and a higher number of contact points between net and Envisat.


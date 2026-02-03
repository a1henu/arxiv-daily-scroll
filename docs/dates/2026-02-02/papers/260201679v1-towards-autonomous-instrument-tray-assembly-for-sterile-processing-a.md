---
layout: default
title: Towards Autonomous Instrument Tray Assembly for Sterile Processing Applications
---

# Towards Autonomous Instrument Tray Assembly for Sterile Processing Applications
**arXiv**：[2602.01679v1](https://arxiv.org/abs/2602.01679) · [PDF](https://arxiv.org/pdf/2602.01679.pdf)  
**作者**：Raghavasimhan Sankaranarayanan, Paul Stuart, Nicholas Ahn, Arno Sungarian, Yash Chitalia  

**一句话要点**：提出全自动机器人系统以解决无菌处理中器械托盘组装问题

**关键词**：机器人系统, 混合感知, 器械分类, 规则打包, 无菌处理, 碰撞减少

## 3 点简述
- 核心问题：无菌处理部门手动组装器械托盘耗时、易错且易污染。
- 方法要点：采用混合感知流水线检测分类器械，结合机器人臂与规则打包算法。
- 实验或效果：系统感知准确率高，显著减少器械碰撞，提升安全性与一致性。

## 摘要（原文）

> The Sterile Processing and Distribution (SPD) department is responsible for cleaning, disinfecting, inspecting, and assembling surgical instruments between surgeries. Manual inspection and preparation of instrument trays is a time-consuming, error-prone task, often prone to contamination and instrument breakage. In this work, we present a fully automated robotic system that sorts and structurally packs surgical instruments into sterile trays, focusing on automation of the SPD assembly stage. A custom dataset comprising 31 surgical instruments and 6,975 annotated images was collected to train a hybrid perception pipeline using YOLO12 for detection and a cascaded ResNet-based model for fine-grained classification. The system integrates a calibrated vision module, a 6-DOF Staubli TX2-60L robotic arm with a custom dual electromagnetic gripper, and a rule-based packing algorithm that reduces instrument collisions during transport. The packing framework uses 3D printed dividers and holders to physically isolate instruments, reducing collision and friction during transport. Experimental evaluations show high perception accuracy and statistically significant reduction in tool-to-tool collisions compared to human-assembled trays. This work serves as the scalable first step toward automating SPD workflows, improving safety, and consistency of surgical preparation while reducing SPD processing times.


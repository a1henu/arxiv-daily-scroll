---
layout: default
title: Docking and Persistent Operations for a Resident Underwater Vehicle
---

# Docking and Persistent Operations for a Resident Underwater Vehicle
**arXiv**：[2602.16360v1](https://arxiv.org/abs/2602.16360) · [PDF](https://arxiv.org/pdf/2602.16360.pdf)  
**作者**：Leonard Günzel, Gabrielė Kasparavičiūtė, Ambjørn Grimsrud Waldum, Bjørn-Magnus Moslått, Abubakar Aliyu Badawi, Celil Yılmaz, Md Shamin Yeasher Yousha, Robert Staven, Martin Ludvigsen  

**一句话要点**：提出基于对接站和增强感知的驻留式水下机器人系统，以解决深海长期自主监测的挑战。

**关键词**：驻留式水下机器人, 自主对接, 视觉声学融合导航, 长期水下监测, ROV系统, 扩展卡尔曼滤波

## 3 点简述
- 核心问题：海洋监测受限于高成本和稀疏观测，驻留式水下机器人面临自主性、鲁棒性和机械耐久性难题。
- 方法要点：开发对接站与小型ROV，融合USBL声学导航和ArUco视觉定位，通过扩展卡尔曼滤波实现自主对接。
- 实验或效果：在90米深度实现90%自主对接成功率，4分钟内完成巡检任务，验证了无缆持久操作的可行性。

## 摘要（原文）

> Our understanding of the oceans remains limited by sparse and infrequent observations, primarily because current methods are constrained by the high cost and logistical effort of underwater monitoring, relying either on sporadic surveys across broad areas or on long-term measurements at fixed locations. To overcome these limitations, monitoring systems must enable persistent and autonomous operations without the need for continuous surface support. Despite recent advances, resident underwater vehicles remain uncommon due to persistent challenges in autonomy, robotic resilience, and mechanical robustness, particularly under long-term deployment in harsh and remote environments. This work addresses these problems by presenting the development, deployment, and operation of a resident infrastructure using a docking station with a mini-class Remotely Operated Vehicle (ROV) at 90m depth. The ROVis equipped with enhanced onboard processing and perception, allowing it to autonomously navigate using USBL signals, dock via ArUco marker-based visual localisation fused through an Extended Kalman Filter, and carry out local inspection routines. The system demonstrated a 90% autonomous docking success rate and completed full inspection missions within four minutes, validating the integration of acoustic and visual navigation in real-world conditions. These results show that reliable, untethered operations at depth are feasible, highlighting the potential of resident ROV systems for scalable, cost-effective underwater monitoring.


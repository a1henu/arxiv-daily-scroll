---
layout: default
title: Learning From a Steady Hand: A Weakly Supervised Agent for Robot Assistance under Microscopy
---

# Learning From a Steady Hand: A Weakly Supervised Agent for Robot Assistance under Microscopy
**arXiv**：[2601.20776v1](https://arxiv.org/abs/2601.20776) · [PDF](https://arxiv.org/pdf/2601.20776.pdf)  
**作者**：Huanyu Tian, Martin Huber, Lingyun Zeng, Zhe Han, Wayne Bennett, Giuseppe Silvestri, Gerardo Mendizabal-Ruiz, Tom Vercauteren, Alejandro Chavez-Badiola, Christos Bergeles  

**一句话要点**：提出弱监督框架融合校准感知与导纳控制，提升显微镜下机器人辅助操作的可靠性

**关键词**：弱监督学习, 机器人辅助操作, 显微镜引导, 校准感知, 导纳控制, 微米级精度

## 3 点简述
- 核心问题：传统显微镜下机器人操作依赖费力的2D标注，缺乏校准感知和深度感知能力
- 方法要点：利用可重复预热轨迹提取隐式空间信息，实现无外部标记的校准感知深度感知
- 实验或效果：在用户研究中，该代理将NASA-TLX工作量降低77.1%，并达到微米级精度

## 摘要（原文）

> This paper rethinks steady-hand robotic manipulation by using a weakly supervised framework that fuses calibration-aware perception with admittance control. Unlike conventional automation that relies on labor-intensive 2D labeling, our framework leverages reusable warm-up trajectories to extract implicit spatial information, thereby achieving calibration-aware, depth-resolved perception without the need for external fiducials or manual depth annotation. By explicitly characterizing residuals from observation and calibration models, the system establishes a task-space error budget from recorded warm-ups. The uncertainty budget yields a lateral closed-loop accuracy of approx. 49 micrometers at 95% confidence (worst-case testing subset) and a depth accuracy of <= 291 micrometers at 95% confidence bound during large in-plane moves. In a within-subject user study (N=8), the learned agent reduces overall NASA-TLX workload by 77.1% relative to the simple steady-hand assistance baseline. These results demonstrate that the weakly supervised agent improves the reliability of microscope-guided biomedical micromanipulation without introducing complex setup requirements, offering a practical framework for microscope-guided intervention.


---
layout: default
title: Zero Wrench Control via Wrench Disturbance Observer for Learning-free Peg-in-hole Assembly
---

# Zero Wrench Control via Wrench Disturbance Observer for Learning-free Peg-in-hole Assembly
**arXiv**：[2601.04881v1](https://arxiv.org/abs/2601.04881) · [PDF](https://arxiv.org/pdf/2601.04881.pdf)  
**作者**：Kiyoung Choi, Juwon Jeong, Sehoon Oh  

**一句话要点**：提出动态力矩扰动观测器以实现接触丰富操作中的高灵敏度零力矩控制

**关键词**：零力矩控制, 力矩扰动观测器, 接触丰富操作, 孔轴装配, 动态稳定性, 学习无关方法

## 3 点简述
- 核心问题：传统观测器无法补偿惯性效应，导致零力矩控制灵敏度不足
- 方法要点：通过将任务空间惯性嵌入观测器名义模型，分离动态反应与真实外部力矩
- 实验或效果：在工业公差下进行孔轴装配实验，实现更深更柔顺插入，优于传统方法

## 摘要（原文）

> This paper proposes a Dynamic Wrench Disturbance Observer (DW-DOB) designed to achieve highly sensitive zero-wrench control in contact-rich manipulation. By embedding task-space inertia into the observer nominal model, DW-DOB cleanly separates intrinsic dynamic reactions from true external wrenches. This preserves sensitivity to small forces and moments while ensuring robust regulation of contact wrenches. A passivity-based analysis further demonstrates that DW-DOB guarantees stable interactions under dynamic conditions, addressing the shortcomings of conventional observers that fail to compensate for inertial effects. Peg-in-hole experiments at industrial tolerances (H7/h6) validate the approach, yielding deeper and more compliant insertions with minimal residual wrenches and outperforming a conventional wrench disturbance observer and a PD baseline. These results highlight DW-DOB as a practical learning-free solution for high-precision zero-wrench control in contact-rich tasks.


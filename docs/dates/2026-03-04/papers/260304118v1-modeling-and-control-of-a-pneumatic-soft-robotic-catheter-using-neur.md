---
layout: default
title: Modeling and Control of a Pneumatic Soft Robotic Catheter Using Neural Koopman Operators
---

# Modeling and Control of a Pneumatic Soft Robotic Catheter Using Neural Koopman Operators
**arXiv**：[2603.04118v1](https://arxiv.org/abs/2603.04118) · [PDF](https://arxiv.org/pdf/2603.04118.pdf)  
**作者**：Yiyao Yue, Noah Barnes, Lingyun Di, Olivia Young, Ryan D. Sochol, Jeremy D. Brown, Axel Krieger  

**一句话要点**：提出神经Koopman算子框架以提升软体机器人导管建模与控制精度

**关键词**：软体机器人导管, Koopman算子, 神经网络建模, 数据驱动控制, 心脏介入手术

## 3 点简述
- 软体机器人导管因非线性行为导致建模与控制困难
- 采用神经网络联合学习提升空间表示与Koopman算子，实现端到端数据驱动控制
- 在交互位置控制和模拟心脏消融任务中验证，平均位置误差2.1±0.4毫米，优于基线方法

## 摘要（原文）

> Catheter-based interventions are widely used for the diagnosis and treatment of cardiac diseases. Recently, robotic catheters have attracted attention for their ability to improve precision and stability over conventional manual approaches. However, accurate modeling and control of soft robotic catheters remain challenging due to their complex, nonlinear behavior. The Koopman operator enables lifting the original system data into a linear "lifted space", offering a data-driven framework for predictive control; however, manually chosen basis functions in the lifted space often oversimplify system behaviors and degrade control performance. To address this, we propose a neural network-enhanced Koopman operator framework that jointly learns the lifted space representation and Koopman operator in an end-to-end manner. Moreover, motivated by the need to minimize radiation exposure during X-ray fluoroscopy in cardiac ablation, we investigate open-loop control strategies using neural Koopman operators to reliably reach target poses without continuous imaging feedback. The proposed method is validated in two experimental scenarios: interactive position control and a simulated cardiac ablation task using an atrium-like cavity. Our approach achieves average errors of 2.1 +- 0.4 mm in position and 4.9 +- 0.6 degrees in orientation, outperforming not only model-based baselines but also other Koopman variants in targeting accuracy and efficiency. These results highlight the potential of the proposed framework for advancing soft robotic catheter systems and improving catheter-based interventions.


---
layout: default
title: CT-Enabled Patient-Specific Simulation and Contact-Aware Robotic Planning for Cochlear Implantation
---

# CT-Enabled Patient-Specific Simulation and Contact-Aware Robotic Planning for Cochlear Implantation
**arXiv**：[2603.05333v1](https://arxiv.org/abs/2603.05333) · [PDF](https://arxiv.org/pdf/2603.05333.pdf)  
**作者**：Lingxiao Xun, Gang Zheng, Alexandre Kruszewski, Renato Torres  

**一句话要点**：提出基于CT的患者特异性模拟与接触感知机器人规划方法，以优化人工耳蜗植入手术。

**关键词**：人工耳蜗植入, 机器人手术规划, CT成像模拟, 接触力建模, 患者特异性解剖

## 3 点简述
- 核心问题：机器人植入人工耳蜗时需精确预测接触力，以减少创伤和防止锁定或屈曲失败。
- 方法要点：开发低维可微Cosserat杆模型，结合摩擦接触和伪动力学正则化，实现连续粘滑过渡。
- 实验或效果：通过仿真和实验验证，显示能降低锁定/屈曲风险并提高植入深度。

## 摘要（原文）

> Robotic cochlear-implant (CI) insertion requires precise prediction and regulation of contact forces to minimize intracochlear trauma and prevent failure modes such as locking and buckling. Aligned with the integration of advanced medical imaging and robotics for autonomous, precision interventions, this paper presents a unified CT-to-simulation pipeline for contact-aware insertion planning and validation. We develop a low-dimensional, differentiable Cosserat-rod model of the electrode array coupled with frictional contact and pseudo-dynamics regularization to ensure continuous stick-slip transitions. Patient-specific cochlear anatomy is reconstructed from CT imaging and encoded via an analytic parametrization of the scala-tympani lumen, enabling efficient and differentiable contact queries through closest-point projection. Based on a differentiated equilibrium-constraint formulation, we derive an online direction-update law under an RCM-like constraint that suppresses lateral insertion forces while maintaining axial advancement. Simulations and benchtop experiments validate deformation and force trends, demonstrating reduced locking/buckling risk and improved insertion depth. The study highlights how CT-based imaging enhances modeling, planning, and safety capabilities in robot-assisted inner-ear procedures.


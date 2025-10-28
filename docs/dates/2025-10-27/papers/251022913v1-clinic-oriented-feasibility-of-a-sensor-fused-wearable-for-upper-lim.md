---
layout: default
title: Clinic-Oriented Feasibility of a Sensor-Fused Wearable for Upper-Limb Function
---

# Clinic-Oriented Feasibility of a Sensor-Fused Wearable for Upper-Limb Function
**arXiv**：[2510.22913v1](https://arxiv.org/abs/2510.22913) · [PDF](https://arxiv.org/pdf/2510.22913.pdf)  
**作者**：Thanyanee Srichaisak, Arissa Ieochai, Aueaphum Aueawattthanaphisut  

**一句话要点**：提出传感器融合可穿戴设备，用于改善上肢功能康复的震颤和活动范围。

**关键词**：传感器融合, 上肢康复, 震颤检测, 设备端推理, 安全辅助策略, 技术可行性

## 3 点简述
- 核心问题：上肢无力和震颤限制日常生活活动，降低家庭康复依从性。
- 方法要点：集成表面肌电、IMU和弯曲/力传感器，采用低延迟设备端推理和安全辅助策略。
- 实验或效果：在健康成人中测试，震颤指数降低，活动范围和重复次数增加，无不良事件。

## 摘要（原文）

> Background: Upper-limb weakness and tremor (4--12 Hz) limit activities of
> daily living (ADL) and reduce adherence to home rehabilitation. Objective: To
> assess technical feasibility and clinician-relevant signals of a sensor-fused
> wearable targeting the triceps brachii and extensor pollicis brevis. Methods: A
> lightweight node integrates surface EMG (1 kHz), IMU (100--200 Hz), and
> flex/force sensors with on-device INT8 inference (Tiny 1D-CNN/Transformer) and
> a safety-bounded assist policy (angle/torque/jerk limits; stall/time-out).
> Healthy adults (n = 12) performed three ADL-like tasks. Primary outcomes:
> Tremor Index (TI), range of motion (ROM), repetitions (Reps min$^{-1}$).
> Secondary: EMG median-frequency slope (fatigue trend), closed-loop latency,
> session completion, and device-related adverse events. Analyses used
> subject-level paired medians with BCa 95\% CIs; exact Wilcoxon $p$-values are
> reported in the Results. Results: Assistance was associated with lower tremor
> prominence and improved task throughput: TI decreased by $-0.092$ (95\% CI
> [$-0.102$, $-0.079$]), ROM increased by $+12.65\%$ (95\% CI [$+8.43$,
> $+13.89$]), and Reps rose by $+2.99$ min$^{-1}$ (95\% CI [$+2.61$, $+3.35$]).
> Median on-device latency was 8.7 ms at a 100 Hz loop rate; all sessions were
> completed with no device-related adverse events. Conclusions: Multimodal
> sensing with low-latency, safety-bounded assistance produced improved movement
> quality (TI $\downarrow$) and throughput (ROM, Reps $\uparrow$) in a pilot
> technical-feasibility setting, supporting progression to IRB-approved patient
> studies. Trial registration: Not applicable (pilot non-clinical).


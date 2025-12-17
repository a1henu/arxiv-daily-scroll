---
layout: default
title: A data-physics hybrid generative model for patient-specific post-stroke motor rehabilitation using wearable sensor data
---

# A data-physics hybrid generative model for patient-specific post-stroke motor rehabilitation using wearable sensor data
**arXiv**：[2512.14329v1](https://arxiv.org/abs/2512.14329) · [PDF](https://arxiv.org/pdf/2512.14329.pdf)  
**作者**：Yanning Dai, Chenyu Tang, Ruizhi Zhang, Wenyu Yang, Yilan Zhang, Yuhui Wang, Junliang Chen, Xuhang Chen, Ruimou Xie, Yangyue Cao, Qiaoying Li, Jin Cao, Tao Li, Hubin Zhao, Yu Pan, Arokia Nathan, Xin Gao, Peter Smielewski, Shuo Gao  

**一句话要点**：提出数据-物理混合生成模型，基于单次平地行走数据预测中风患者个性化康复任务步态。

**关键词**：中风康复, 生成模型, 可穿戴传感器, 深度强化学习, 步态模拟, 个性化医疗

## 3 点简述
- 核心问题：中风后运动康复需动态预测患者任务能力，但现有评估仅提供静态分数，无法指导安全任务执行。
- 方法要点：结合可穿戴传感器数据、物理控制器、健康运动图谱和深度强化学习，生成个性化、物理合理的坡道和楼梯步态模拟。
- 实验或效果：在11名患者中提升关节角度和端点保真度，多中心试点显示使用预测指导康复可改善临床评分。

## 摘要（原文）

> Dynamic prediction of locomotor capacity after stroke is crucial for tailoring rehabilitation, yet current assessments provide only static impairment scores and do not indicate whether patients can safely perform specific tasks such as slope walking or stair climbing. Here, we develop a data-physics hybrid generative framework that reconstructs an individual stroke survivor's neuromuscular control from a single 20 m level-ground walking trial and predicts task-conditioned locomotion across rehabilitation scenarios. The system combines wearable-sensor kinematics, a proportional-derivative physics controller, a population Healthy Motion Atlas, and goal-conditioned deep reinforcement learning with behaviour cloning and generative adversarial imitation learning to generate physically plausible, patient-specific gait simulations for slopes and stairs. In 11 stroke survivors, the personalized controllers preserved idiosyncratic gait patterns while improving joint-angle and endpoint fidelity by 4.73% and 12.10%, respectively, and reducing training time to 25.56% relative to a physics-only baseline. In a multicentre pilot involving 21 inpatients, clinicians who used our locomotion predictions to guide task selection and difficulty obtained larger gains in Fugl-Meyer lower-extremity scores over 28 days of standard rehabilitation than control clinicians (mean change 6.0 versus 3.7 points). These findings indicate that our generative, task-predictive framework can augment clinical decision-making in post-stroke gait rehabilitation and provide a template for dynamically personalized motor recovery strategies.


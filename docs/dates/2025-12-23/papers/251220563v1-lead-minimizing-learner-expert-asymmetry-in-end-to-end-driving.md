---
layout: default
title: LEAD: Minimizing Learner-Expert Asymmetry in End-to-End Driving
---

# LEAD: Minimizing Learner-Expert Asymmetry in End-to-End Driving
**arXiv**：[2512.20563v1](https://arxiv.org/abs/2512.20563) · [PDF](https://arxiv.org/pdf/2512.20563.pdf)  
**作者**：Long Nguyen, Micha Fauth, Bernhard Jaeger, Daniel Dauner, Maximilian Igl, Andreas Geiger, Kashyap Chitta  

**一句话要点**：提出LEAD方法以减少专家与学生间的不对称性，提升端到端驾驶性能

**关键词**：端到端驾驶, 模仿学习, 专家-学生不对称, CARLA基准, 感知监督, sim-to-real

## 3 点简述
- 核心问题：专家与学生间存在可见性和不确定性不对称，限制模仿学习效果
- 方法要点：通过干预措施缩小专家与学生差距，如改进导航意图指定
- 实验或效果：在CARLA基准上达到新SOTA，并在真实世界基准上展示一致增益

## 摘要（原文）

> Simulators can generate virtually unlimited driving data, yet imitation learning policies in simulation still struggle to achieve robust closed-loop performance. Motivated by this gap, we empirically study how misalignment between privileged expert demonstrations and sensor-based student observations can limit the effectiveness of imitation learning. More precisely, experts have significantly higher visibility (e.g., ignoring occlusions) and far lower uncertainty (e.g., knowing other vehicles' actions), making them difficult to imitate reliably. Furthermore, navigational intent (i.e., the route to follow) is under-specified in student models at test time via only a single target point. We demonstrate that these asymmetries can measurably limit driving performance in CARLA and offer practical interventions to address them. After careful modifications to narrow the gaps between expert and student, our TransFuser v6 (TFv6) student policy achieves a new state of the art on all major publicly available CARLA closed-loop benchmarks, reaching 95 DS on Bench2Drive and more than doubling prior performances on Longest6~v2 and Town13. Additionally, by integrating perception supervision from our dataset into a shared sim-to-real pipeline, we show consistent gains on the NAVSIM and Waymo Vision-Based End-to-End driving benchmarks. Our code, data, and models are publicly available at https://github.com/autonomousvision/lead.


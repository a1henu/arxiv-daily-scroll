---
layout: default
title: Dynamic Deception: When Pedestrians Team Up to Fool Autonomous Cars
---

# Dynamic Deception: When Pedestrians Team Up to Fool Autonomous Cars
**arXiv**：[2602.18079v1](https://arxiv.org/abs/2602.18079) · [PDF](https://arxiv.org/pdf/2602.18079.pdf)  
**作者**：Masoud Jamshidiyan Tehrani, Marco Gabriel, Jinhan Kim, Paolo Tonella  

**一句话要点**：提出动态合谋攻击，通过多行人协调运动放大对抗补丁效果，以诱导自动驾驶系统级故障。

**关键词**：自动驾驶安全, 对抗攻击, 系统级评估, 动态协调, 模拟器测试, 行人检测

## 3 点简述
- 系统级攻击常因时空短暂性失效，本文聚焦动态元素协调以延长对抗信号影响。
- 方法利用多行人携带对抗补丁，通过运动合谋增强攻击，在CARLA模拟器中评估。
- 实验显示双行人动态合谋可导致车辆完全停止，成功率高达50%，突显模型与系统级安全差距。

## 摘要（原文）

> Many adversarial attacks on autonomous-driving perception models fail to cause system-level failures once deployed in a full driving stack. The main reason for such ineffectiveness is that once deployed in a system (e.g., within a simulator), attacks tend to be spatially or temporally short-lived, due to the vehicle's dynamics, hence rarely influencing the vehicle behaviour. In this paper, we address both limitations by introducing a system-level attack in which multiple dynamic elements (e.g., two pedestrians) carry adversarial patches (e.g., on cloths) and jointly amplify their effect through coordination and motion. We evaluate our attacks in the CARLA simulator using a state-of-the-art autonomous driving agent. At the system level, single-pedestrian attacks fail in all runs (out of 10), while dynamic collusion by two pedestrians induces full vehicle stops in up to 50\% of runs, with static collusion yielding no successful attack at all. These results show that system-level failures arise only when adversarial signals persist over time and are amplified through coordinated actors, exposing a gap between model-level robustness and end-to-end safety.


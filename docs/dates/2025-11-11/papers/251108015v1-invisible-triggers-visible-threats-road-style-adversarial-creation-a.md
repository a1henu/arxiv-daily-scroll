---
layout: default
title: Invisible Triggers, Visible Threats! Road-Style Adversarial Creation Attack for Visual 3D Detection in Autonomous Driving
---

# Invisible Triggers, Visible Threats! Road-Style Adversarial Creation Attack for Visual 3D Detection in Autonomous Driving
**arXiv**：[2511.08015v1](https://arxiv.org/abs/2511.08015) · [PDF](https://arxiv.org/pdf/2511.08015.pdf)  
**作者**：Jian Wang, Lijun He, Yixing Yong, Haixia Bi, Fan Li  

**一句话要点**：提出AdvRoad方法生成道路风格对抗海报，以隐蔽攻击自动驾驶3D视觉检测系统。

**关键词**：自动驾驶安全, 对抗攻击, 3D视觉检测, 道路风格生成, 隐蔽攻击

## 3 点简述
- 核心问题：现有对抗海报外观不自然，易被人类察觉且防御性强，威胁自动驾驶安全。
- 方法要点：采用两阶段方法生成自然道路风格对抗海报，确保隐蔽性并诱导检测器误判。
- 实验或效果：AdvRoad泛化性强，适用于多种检测器、场景和位置，物理实验验证现实威胁。

## 摘要（原文）

> Modern autonomous driving (AD) systems leverage 3D object detection to perceive foreground objects in 3D environments for subsequent prediction and planning. Visual 3D detection based on RGB cameras provides a cost-effective solution compared to the LiDAR paradigm. While achieving promising detection accuracy, current deep neural network-based models remain highly susceptible to adversarial examples. The underlying safety concerns motivate us to investigate realistic adversarial attacks in AD scenarios. Previous work has demonstrated the feasibility of placing adversarial posters on the road surface to induce hallucinations in the detector. However, the unnatural appearance of the posters makes them easily noticeable by humans, and their fixed content can be readily targeted and defended. To address these limitations, we propose the AdvRoad to generate diverse road-style adversarial posters. The adversaries have naturalistic appearances resembling the road surface while compromising the detector to perceive non-existent objects at the attack locations. We employ a two-stage approach, termed Road-Style Adversary Generation and Scenario-Associated Adaptation, to maximize the attack effectiveness on the input scene while ensuring the natural appearance of the poster, allowing the attack to be carried out stealthily without drawing human attention. Extensive experiments show that AdvRoad generalizes well to different detectors, scenes, and spoofing locations. Moreover, physical attacks further demonstrate the practical threats in real-world environments.


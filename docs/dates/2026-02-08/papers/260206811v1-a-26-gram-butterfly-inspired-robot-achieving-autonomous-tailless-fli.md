---
layout: default
title: A 26-Gram Butterfly-Inspired Robot Achieving Autonomous Tailless Flight
---

# A 26-Gram Butterfly-Inspired Robot Achieving Autonomous Tailless Flight
**arXiv**：[2602.06811v1](https://arxiv.org/abs/2602.06811) · [PDF](https://arxiv.org/pdf/2602.06811.pdf)  
**作者**：Weibin Gu, Chenrui Feng, Lian Liu, Chen Yang, Xingchi Jiao, Yuhe Ding, Xiaofei Shi, Chao Gao, Alessandro Rizzo, Guyue Zhou  

**一句话要点**：提出26克蝴蝶仿生扑翼机器人AirPulse，实现无尾自主飞行，用于受限空间探测。

**关键词**：扑翼微飞行器, 蝴蝶仿生, 无尾飞行, 自主控制, 受限空间探测, 流体-结构耦合

## 3 点简述
- 核心问题：无尾双翼扑翼微飞行器因复杂流体-结构和翼-体耦合而难以稳定控制。
- 方法要点：采用低展弦比柔性碳纤维翼和STAR生成器，通过扑动调制参数映射力-力矩，实现线性参数化不对称扑动控制。
- 实验或效果：自由飞行实验展示稳定爬升和转向，首次实现最轻无尾蝴蝶仿生扑翼机器人的机载控制飞行。

## 摘要（原文）

> Flapping-wing micro air vehicles (FWMAVs) have demonstrated remarkable bio-inspired agility, yet tailless two-winged configurations remain largely unexplored due to their complex fluid-structure and wing-body coupling. Here we present \textit{AirPulse}, a 26-gram butterfly-inspired FWMAV that achieves fully onboard, closed-loop, untethered flight without auxiliary control surfaces. The AirPulse robot replicates key biomechanical traits of butterfly flight, including low wing aspect ratio, compliant carbon-fiber-reinforced wings, and low-frequency, high-amplitude flapping that induces cyclic variations in the center of gravity and moment of inertia, producing characteristic body undulation. We establish a quantitative mapping between flapping modulation parameters and force-torque generation, and introduce the Stroke Timing Asymmetry Rhythm (STAR) generator, enabling smooth, stable, and linearly parameterized wingstroke asymmetry for flapping control. Integrating these with an attitude controller, the AirPulse robot maintains pitch and yaw stability despite strong oscillatory dynamics. Free-flight experiments demonstrate stable climbing and turning maneuvers via either angle offset or stroke timing modulation, marking the first onboard controlled flight of the lightest two-winged, tailless butterfly-inspired FWMAV reported in peer-reviewed literature. This work corroborates a foundational platform for lightweight, collision-proof FWMAVs, bridging biological inspiration with practical aerial robotics. Their non-invasive maneuverability is ideally suited for real-world applications, such as confined-space inspection and ecological monitoring, inaccessible to traditional drones, while their biomechanical fidelity provides a physical model to decode the principles underlying the erratic yet efficient flight of real butterflies.


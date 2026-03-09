---
layout: default
title: Towards Driver Behavior Understanding: Weakly-Supervised Risk Perception in Driving Scenes
---

# Towards Driver Behavior Understanding: Weakly-Supervised Risk Perception in Driving Scenes
**arXiv**：[2603.05926v1](https://arxiv.org/abs/2603.05926) · [PDF](https://arxiv.org/pdf/2603.05926.pdf)  
**作者**：Nakul Agarwal, Yi-Ting Chen, Behzad Dariush  

**一句话要点**：提出弱监督风险对象识别框架与RAID数据集，以理解驾驶场景中的风险感知。

**关键词**：驾驶员风险感知, 弱监督学习, 风险评估, 驾驶场景数据集, 行人注意力

## 3 点简述
- 核心问题：理解驾驶员风险感知，需建模驾驶员意图、响应与外部风险源的关系。
- 方法要点：基于RAID数据集，弱监督识别风险对象，结合驾驶员意图与响应建模。
- 实验或效果：在RAID和HDDS数据集上，性能分别提升20.6%和23.1%。

## 摘要（原文）

> Achieving zero-collision mobility remains a key objective for intelligent vehicle systems, which requires understanding driver risk perception-a complex cognitive process shaped by voluntary response of the driver to external stimuli and the attentiveness of surrounding road users towards the ego-vehicle. To support progress in this area, we introduce RAID (Risk Assessment In Driving scenes)-a large-scale dataset specifically curated for research on driver risk perception and contextual risk assessment. RAID comprises 4,691 annotated video clips, covering diverse traffic scenarios with labels for driver's intended maneuver, road topology, risk situations (e.g., crossing pedestrians), driver responses, and pedestrian attentiveness. Leveraging RAID, we propose a weakly supervised risk object identification framework that models the relationship between driver's intended maneuver and responses to identify potential risk sources. Additionally, we analyze the role of pedestrian attention in estimating risk and demonstrate the value of the proposed dataset. Experimental evaluations demonstrate that our method achieves 20.6% and 23.1% performance gains over prior state-of-the-art approaches on the RAID and HDDS datasets, respectively.


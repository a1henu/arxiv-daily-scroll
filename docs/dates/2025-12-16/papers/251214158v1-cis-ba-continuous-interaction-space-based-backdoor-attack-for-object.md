---
layout: default
title: CIS-BA: Continuous Interaction Space Based Backdoor Attack for Object Detection in the Real-World
---

# CIS-BA: Continuous Interaction Space Based Backdoor Attack for Object Detection in the Real-World
**arXiv**：[2512.14158v1](https://arxiv.org/abs/2512.14158) · [PDF](https://arxiv.org/pdf/2512.14158.pdf)  
**作者**：Shuxin Zhao, Bo Lang, Nan Xiao, Yilang Zhang  

**一句话要点**：提出CIS-BA，基于连续交互空间的后门攻击，以增强自动驾驶等场景中目标检测的攻击能力与鲁棒性。

**关键词**：后门攻击, 目标检测, 连续交互空间, 多触发攻击, 鲁棒性, 自动驾驶安全

## 3 点简述
- 现有后门攻击依赖单触发-单对象映射和脆弱像素线索，能力与鲁棒性受限。
- CIS-BA通过建模对象间连续交互模式，设计空间触发，实现多触发-多对象攻击和几何不变性。
- 在MS-COCO和真实视频上，攻击成功率超97%，动态多触发下保持超95%效果，并规避先进防御。

## 摘要（原文）

> Object detection models deployed in real-world applications such as autonomous driving face serious threats from backdoor attacks. Despite their practical effectiveness,existing methods are inherently limited in both capability and robustness due to their dependence on single-trigger-single-object mappings and fragile pixel-level cues. We propose CIS-BA, a novel backdoor attack paradigm that redefines trigger design by shifting from static object features to continuous inter-object interaction patterns that describe how objects co-occur and interact in a scene. By modeling these patterns as a continuous interaction space, CIS-BA introduces space triggers that, for the first time, enable a multi-trigger-multi-object attack mechanism while achieving robustness through invariant geometric relations. To implement this paradigm, we design CIS-Frame, which constructs space triggers via interaction analysis, formalizes them as class-geometry constraints for sample poisoning, and embeds the backdoor during detector training. CIS-Frame supports both single-object attacks (object misclassification and disappearance) and multi-object simultaneous attacks, enabling complex and coordinated effects across diverse interaction states. Experiments on MS-COCO and real-world videos show that CIS-BA achieves over 97% attack success under complex environments and maintains over 95% effectiveness under dynamic multi-trigger conditions, while evading three state-of-the-art defenses. In summary, CIS-BA extends the landscape of backdoor attacks in interaction-intensive scenarios and provides new insights into the security of object detection systems.


---
layout: default
title: Higher-Order Adversarial Patches for Real-Time Object Detectors
---

# Higher-Order Adversarial Patches for Real-Time Object Detectors
**arXiv**：[2601.04991v1](https://arxiv.org/abs/2601.04991) · [PDF](https://arxiv.org/pdf/2601.04991.pdf)  
**作者**：Jens Bayer, Stefan Becker, David Münch, Michael Arens, Jürgen Beyerer  

**一句话要点**：提出高阶对抗补丁以增强对实时目标检测器的攻击泛化能力

**关键词**：高阶对抗攻击, 目标检测器, 对抗补丁, 对抗训练, YOLOv10, 泛化能力

## 3 点简述
- 研究高阶对抗攻击对目标检测器的影响，通过迭代训练攻击模式与对抗训练
- 使用YOLOv10作为代表，采用对抗补丁进行规避攻击，评估攻击效果
- 结果显示高阶对抗补丁具有更强的泛化能力，仅对抗训练不足以有效防御

## 摘要（原文）

> Higher-order adversarial attacks can directly be considered the result of a cat-and-mouse game -- an elaborate action involving constant pursuit, near captures, and repeated escapes. This idiom describes the enduring circular training of adversarial attack patterns and adversarial training the best. The following work investigates the impact of higher-order adversarial attacks on object detectors by successively training attack patterns and hardening object detectors with adversarial training. The YOLOv10 object detector is chosen as a representative, and adversarial patches are used in an evasion attack manner. Our results indicate that higher-order adversarial patches are not only affecting the object detector directly trained on but rather provide a stronger generalization capacity compared to lower-order adversarial patches. Moreover, the results highlight that solely adversarial training is not sufficient to harden an object detector efficiently against this kind of adversarial attack. Code: https://github.com/JensBayer/HigherOrder


---
layout: default
title: Strategy-Supervised Autonomous Laparoscopic Camera Control via Event-Driven Graph Mining
---

# Strategy-Supervised Autonomous Laparoscopic Camera Control via Event-Driven Graph Mining
**arXiv**：[2602.20500v1](https://arxiv.org/abs/2602.20500) · [PDF](https://arxiv.org/pdf/2602.20500.pdf)  
**作者**：Keyu Zhou, Peisen Xu, Yahao Wu, Jiming Chen, Gaofeng Li, Shunlei Li  

**一句话要点**：提出基于事件图挖掘的策略监督框架，实现腹腔镜手术中自主相机控制，提升稳定性和可解释性。

**关键词**：腹腔镜相机控制, 事件图挖掘, 视觉语言模型, 自主手术, 策略监督, 安全约束

## 3 点简述
- 核心问题：腹腔镜手术中相机需在快速工具-组织交互下保持稳定、安全视图，同时确保可解释性。
- 方法要点：离线解析手术视频为事件图，挖掘策略原语；在线用VLM预测策略和运动命令，结合IBVS-RCM控制器执行。
- 实验或效果：在硅胶模型和猪组织实验中，系统优于初级外科医生，减少中心误差35.26%和图像抖动62.33%。

## 摘要（原文）

> Autonomous laparoscopic camera control must maintain a stable and safe surgical view under rapid tool-tissue interactions while remaining interpretable to surgeons. We present a strategy-grounded framework that couples high-level vision-language inference with low-level closed-loop control. Offline, raw surgical videos are parsed into camera-relevant temporal events (e.g., interaction, working-distance deviation, and view-quality degradation) and structured as attributed event graphs. Mining these graphs yields a compact set of reusable camera-handling strategy primitives, which provide structured supervision for learning. Online, a fine-tuned Vision-Language Model (VLM) processes the live laparoscopic view to predict the dominant strategy and discrete image-based motion commands, executed by an IBVS-RCM controller under strict safety constraints; optional speech input enables intuitive human-in-the-loop conditioning. On a surgeon-annotated dataset, event parsing achieves reliable temporal localization (F1-score 0.86), and the mined strategies show strong semantic alignment with expert interpretation (cluster purity 0.81). Extensive ex vivo experiments on silicone phantoms and porcine tissues demonstrate that the proposed system outperforms junior surgeons in standardized camera-handling evaluations, reducing field-of-view centering error by 35.26% and image shaking by 62.33%, while preserving smooth motion and stable working-distance regulation.


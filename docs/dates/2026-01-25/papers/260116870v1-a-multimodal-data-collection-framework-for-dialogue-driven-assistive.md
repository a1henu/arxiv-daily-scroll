---
layout: default
title: A Multimodal Data Collection Framework for Dialogue-Driven Assistive Robotics to Clarify Ambiguities: A Wizard-of-Oz Pilot Study
---

# A Multimodal Data Collection Framework for Dialogue-Driven Assistive Robotics to Clarify Ambiguities: A Wizard-of-Oz Pilot Study
**arXiv**：[2601.16870v1](https://arxiv.org/abs/2601.16870) · [PDF](https://arxiv.org/pdf/2601.16870.pdf)  
**作者**：Guangping Liu, Nicholas Hawkins, Billy Madden, Tipu Sultan, Flavio Esposito, Madi Babaiasl  

**一句话要点**：提出多模态数据收集框架以解决对话驱动辅助机器人中的歧义问题

**关键词**：多模态数据收集, 对话驱动控制, 辅助机器人, Wizard-of-Oz实验, 人机交互, 歧义处理

## 3 点简述
- 核心问题：现有辅助机器人接口缺乏灵活性，且缺乏捕捉自然人机交互的多模态数据集，特别是对话歧义。
- 方法要点：采用基于对话的交互协议和两室Wizard-of-Oz设置，记录五种同步模态数据，模拟机器人自主性以引发自然用户行为。
- 实验或效果：通过53次试验的试点数据集验证，框架能有效捕捉歧义类型并支持自然对话交互，适合扩展用于学习与评估。

## 摘要（原文）

> Integrated control of wheelchairs and wheelchair-mounted robotic arms (WMRAs) has strong potential to increase independence for users with severe motor limitations, yet existing interfaces often lack the flexibility needed for intuitive assistive interaction. Although data-driven AI methods show promise, progress is limited by the lack of multimodal datasets that capture natural Human-Robot Interaction (HRI), particularly conversational ambiguity in dialogue-driven control. To address this gap, we propose a multimodal data collection framework that employs a dialogue-based interaction protocol and a two-room Wizard-of-Oz (WoZ) setup to simulate robot autonomy while eliciting natural user behavior. The framework records five synchronized modalities: RGB-D video, conversational audio, inertial measurement unit (IMU) signals, end-effector Cartesian pose, and whole-body joint states across five assistive tasks. Using this framework, we collected a pilot dataset of 53 trials from five participants and validated its quality through motion smoothness analysis and user feedback. The results show that the framework effectively captures diverse ambiguity types and supports natural dialogue-driven interaction, demonstrating its suitability for scaling to a larger dataset for learning, benchmarking, and evaluation of ambiguity-aware assistive control.


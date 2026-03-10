---
layout: default
title: Long-Short Term Agents for Pure-Vision Bronchoscopy Robotic Autonomy
---

# Long-Short Term Agents for Pure-Vision Bronchoscopy Robotic Autonomy
**arXiv**：[2603.07909v1](https://arxiv.org/abs/2603.07909) · [PDF](https://arxiv.org/pdf/2603.07909.pdf)  
**作者**：Junyang Wu, Mingyi Luo, Fangfang Xie, Minghui Zhang, Hanxiao Zhang, Chunxi Zhang, Junhao Wang, Jiayuan Sun, Yun Gu, Guang-Zhong Yang  

**一句话要点**：提出纯视觉支气管镜机器人自主导航框架，结合长短时智能体解决术中导航难题。

**关键词**：支气管镜导航, 纯视觉自主, 长短时智能体, 机器人辅助干预, 世界模型预测, 术中定位

## 3 点简述
- 核心问题：支气管镜术中导航因视野有限和动态伪影而困难，现有方法依赖外部定位技术增加硬件复杂度。
- 方法要点：采用分层长短时智能体，短时反应智能体控制运动，长时策略智能体提供决策支持，冲突时通过世界模型预测选择动作。
- 实验或效果：在高保真气道模型、离体猪肺和活体猪模型中评估，达到专家级导航性能，支持临床前可行性。

## 摘要（原文）

> Accurate intraoperative navigation is essential for robot-assisted endoluminal intervention, but remains difficult because of limited endoscopic field of view and dynamic artifacts. Existing navigation platforms often rely on external localization technologies, such as electromagnetic tracking or shape sensing, which increase hardware complexity and remain vulnerable to intraoperative anatomical mismatch. We present a vision-only autonomy framework that performs long-horizon bronchoscopic navigation using preoperative CT-derived virtual targets and live endoscopic video, without external tracking during navigation. The framework uses hierarchical long-short agents: a short-term reactive agent for continuous low-latency motion control, and a long-term strategic agent for decision support at anatomically ambiguous points. When their recommendations conflict, a world-model critic predicts future visual states for candidate actions and selects the action whose predicted state best matches the target view. We evaluated the system in a high-fidelity airway phantom, three ex vivo porcine lungs, and a live porcine model. The system reached all planned segmental targets in the phantom, maintained 80\% success to the eighth generation ex vivo, and achieved in vivo navigation performance comparable to the expert bronchoscopist. These results support the preclinical feasibility of sensor-free autonomous bronchoscopic navigation.


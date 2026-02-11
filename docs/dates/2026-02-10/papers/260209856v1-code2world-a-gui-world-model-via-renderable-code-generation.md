---
layout: default
title: Code2World: A GUI World Model via Renderable Code Generation
---

# Code2World: A GUI World Model via Renderable Code Generation
**arXiv**：[2602.09856v1](https://arxiv.org/abs/2602.09856) · [PDF](https://arxiv.org/pdf/2602.09856.pdf)  
**作者**：Yuhao Zheng, Li'an Zhong, Yi Wang, Rui Dai, Kaikui Liu, Xiangxiang Chu, Linyuan Lv, Philip Torr, Kevin Qinghong Lin  

**一句话要点**：提出Code2World，通过可渲染代码生成构建GUI世界模型以提升自主GUI代理的预测能力。

**关键词**：GUI世界模型, 可渲染代码生成, 视觉语言编码器, 强化学习, Android导航

## 3 点简述
- 现有文本和像素方法在视觉保真度和结构可控性上存在不足，阻碍GUI世界模型发展。
- 通过构建AndroidCode数据集并采用视觉反馈修订机制，结合SFT和渲染感知强化学习训练模型。
- 实验显示Code2World-8B在UI预测上表现优异，并显著提升下游导航任务成功率。

## 摘要（原文）

> Autonomous GUI agents interact with environments by perceiving interfaces and executing actions. As a virtual sandbox, the GUI World model empowers agents with human-like foresight by enabling action-conditioned prediction. However, existing text- and pixel-based approaches struggle to simultaneously achieve high visual fidelity and fine-grained structural controllability. To this end, we propose Code2World, a vision-language coder that simulates the next visual state via renderable code generation. Specifically, to address the data scarcity problem, we construct AndroidCode by translating GUI trajectories into high-fidelity HTML and refining synthesized code through a visual-feedback revision mechanism, yielding a corpus of over 80K high-quality screen-action pairs. To adapt existing VLMs into code prediction, we first perform SFT as a cold start for format layout following, then further apply Render-Aware Reinforcement Learning which uses rendered outcome as the reward signal by enforcing visual semantic fidelity and action consistency. Extensive experiments demonstrate that Code2World-8B achieves the top-performing next UI prediction, rivaling the competitive GPT-5 and Gemini-3-Pro-Image. Notably, Code2World significantly enhances downstream navigation success rates in a flexible manner, boosting Gemini-2.5-Flash by +9.5% on AndroidWorld navigation. The code is available at https://github.com/AMAP-ML/Code2World.


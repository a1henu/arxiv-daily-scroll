---
layout: default
title: PhysTalk: Language-driven Real-time Physics in 3D Gaussian Scenes
---

# PhysTalk: Language-driven Real-time Physics in 3D Gaussian Scenes
**arXiv**：[2512.24986v1](https://arxiv.org/abs/2512.24986) · [PDF](https://arxiv.org/pdf/2512.24986.pdf)  
**作者**：Luca Collorone, Mert Kiray, Indro Spinelli, Fabio Galasso, Benjamin Busam  

**一句话要点**：提出PhysTalk框架，通过语言驱动实现3D高斯场景的实时物理动画

**关键词**：3D高斯溅射, 语言驱动动画, 实时物理模拟, 开放词汇生成, 交互式4D动画

## 3 点简述
- 核心问题：现有文本生成视觉特效方法缺乏物理真实性和实时交互性，依赖耗时离线优化
- 方法要点：利用大语言模型生成代码，直接修改3D高斯参数，结合轻量代理和粒子动力学实现物理模拟
- 实验或效果：无需训练，计算轻量，支持开放词汇、多材质物体的碰撞感知交互式4D动画

## 摘要（原文）

> Realistic visual simulations are omnipresent, yet their creation requires computing time, rendering, and expert animation knowledge. Open-vocabulary visual effects generation from text inputs emerges as a promising solution that can unlock immense creative potential. However, current pipelines lack both physical realism and effective language interfaces, requiring slow offline optimization. In contrast, PhysTalk takes a 3D Gaussian Splatting (3DGS) scene as input and translates arbitrary user prompts into real time, physics based, interactive 4D animations. A large language model (LLM) generates executable code that directly modifies 3DGS parameters through lightweight proxies and particle dynamics. Notably, PhysTalk is the first framework to couple 3DGS directly with a physics simulator without relying on time consuming mesh extraction. While remaining open vocabulary, this design enables interactive 3D Gaussian animation via collision aware, physics based manipulation of arbitrary, multi material objects. Finally, PhysTalk is train-free and computationally lightweight: this makes 4D animation broadly accessible and shifts these workflows from a "render and wait" paradigm toward an interactive dialogue with a modern, physics-informed pipeline.


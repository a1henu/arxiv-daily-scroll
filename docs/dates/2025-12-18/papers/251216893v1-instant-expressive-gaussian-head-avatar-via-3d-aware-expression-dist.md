---
layout: default
title: Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation
---

# Instant Expressive Gaussian Head Avatar via 3D-Aware Expression Distillation
**arXiv**：[2512.16893v1](https://arxiv.org/abs/2512.16893) · [PDF](https://arxiv.org/pdf/2512.16893.pdf)  
**作者**：Kaiwen Jiang, Xueting Li, Seonwook Park, Ravi Ramamoorthi, Shalini De Mello, Koki Nagano  

**一句话要点**：提出基于3D感知表达蒸馏的即时高斯头像方法，以结合2D扩散模型与3D表示优势，实现快速且表达丰富的头像动画。

**关键词**：头像动画, 3D感知蒸馏, 高斯溅射, 轻量融合, 实时渲染

## 3 点简述
- 核心问题：现有2D方法缺乏3D一致性且速度慢，3D方法表达细节不足，需平衡质量与速度。
- 方法要点：从2D扩散模型蒸馏知识到前馈编码器，采用轻量局部融合策略，解耦3D表示与动画学习。
- 实验或效果：运行速度达107.31 FPS，动画质量媲美先进方法，超越速度与质量的权衡设计。

## 摘要（原文）

> Portrait animation has witnessed tremendous quality improvements thanks to recent advances in video diffusion models. However, these 2D methods often compromise 3D consistency and speed, limiting their applicability in real-world scenarios, such as digital twins or telepresence. In contrast, 3D-aware facial animation feedforward methods -- built upon explicit 3D representations, such as neural radiance fields or Gaussian splatting -- ensure 3D consistency and achieve faster inference speed, but come with inferior expression details. In this paper, we aim to combine their strengths by distilling knowledge from a 2D diffusion-based method into a feed-forward encoder, which instantly converts an in-the-wild single image into a 3D-consistent, fast yet expressive animatable representation. Our animation representation is decoupled from the face's 3D representation and learns motion implicitly from data, eliminating the dependency on pre-defined parametric models that often constrain animation capabilities. Unlike previous computationally intensive global fusion mechanisms (e.g., multiple attention layers) for fusing 3D structural and animation information, our design employs an efficient lightweight local fusion strategy to achieve high animation expressivity. As a result, our method runs at 107.31 FPS for animation and pose control while achieving comparable animation quality to the state-of-the-art, surpassing alternative designs that trade speed for quality or vice versa. Project website is https://research.nvidia.com/labs/amri/projects/instant4d


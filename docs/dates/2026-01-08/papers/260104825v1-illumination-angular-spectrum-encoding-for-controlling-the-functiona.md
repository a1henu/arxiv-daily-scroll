---
layout: default
title: Illumination Angular Spectrum Encoding for Controlling the Functionality of Diffractive Networks
---

# Illumination Angular Spectrum Encoding for Controlling the Functionality of Diffractive Networks
**arXiv**：[2601.04825v1](https://arxiv.org/abs/2601.04825) · [PDF](https://arxiv.org/pdf/2601.04825.pdf)  
**作者**：Matan Kleiner, Lior Michaeli, Tomer Michaeli  

**一句话要点**：提出基于照明角度谱编码的方法，以控制衍射网络的多功能光学计算。

**关键词**：衍射神经网络, 光学计算, 角度谱编码, 多任务控制, 图像翻译

## 3 点简述
- 核心问题：衍射神经网络通常针对单一任务训练，限制了其在需要多功能系统中的应用。
- 方法要点：通过振幅掩模选择性控制照明的角度谱，实现不同网络功能，掩模作为任务编码器。
- 实验或效果：数值模拟中，训练单一网络执行多图像翻译任务，如手写数字转印刷数字，输出类型由照明角度分量决定。

## 摘要（原文）

> Diffractive neural networks have recently emerged as a promising framework for all-optical computing. However, these networks are typically trained for a single task, limiting their potential adoption in systems requiring multiple functionalities. Existing approaches to achieving multi-task functionality either modify the mechanical configuration of the network per task or use a different illumination wavelength or polarization state for each task. In this work, we propose a new control mechanism, which is based on the illumination's angular spectrum. Specifically, we shape the illumination using an amplitude mask that selectively controls its angular spectrum. We employ different illumination masks for achieving different network functionalities, so that the mask serves as a unique task encoder. Interestingly, we show that effective control can be achieved over a very narrow angular range, within the paraxial regime. We numerically illustrate the proposed approach by training a single diffractive network to perform multiple image-to-image translation tasks. In particular, we demonstrate translating handwritten digits into typeset digits of different values, and translating handwritten English letters into typeset numbers and typeset Greek letters, where the type of the output is determined by the illumination's angular components. As we show, the proposed framework can work under different coherence conditions, and can be combined with existing control strategies, such as different wavelengths. Our results establish the illumination angular spectrum as a powerful degree of freedom for controlling diffractive networks, enabling a scalable and versatile framework for multi-task all-optical computing.


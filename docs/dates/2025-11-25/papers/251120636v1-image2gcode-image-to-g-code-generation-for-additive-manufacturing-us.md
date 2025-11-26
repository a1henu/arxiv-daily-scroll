---
layout: default
title: Image2Gcode: Image-to-G-code Generation for Additive Manufacturing Using Diffusion-Transformer Model
---

# Image2Gcode: Image-to-G-code Generation for Additive Manufacturing Using Diffusion-Transformer Model
**arXiv**：[2511.20636v1](https://arxiv.org/abs/2511.20636) · [PDF](https://arxiv.org/pdf/2511.20636.pdf)  
**作者**：Ziyue Wang, Yayati Jadhav, Peter Pak, Amir Barati Farimani  

**一句话要点**：提出Image2Gcode框架，直接从图像生成G代码以加速增材制造设计流程

**关键词**：图像到G代码生成, 扩散概率模型, 增材制造, 端到端框架, 设计自动化

## 3 点简述
- 核心问题：传统制造依赖CAD建模，导致设计迭代缓慢且难以扩展
- 方法要点：使用扩散-Transformer模型从2D图像直接生成可执行G代码序列
- 实验或效果：消除CAD中间步骤，降低制造门槛并加速原型制作

## 摘要（原文）

> Mechanical design and manufacturing workflows conventionally begin with conceptual design, followed by the creation of a computer-aided design (CAD) model and fabrication through material-extrusion (MEX) printing. This process requires converting CAD geometry into machine-readable G-code through slicing and path planning. While each step is well established, dependence on CAD modeling remains a major bottleneck: constructing object-specific 3D geometry is slow and poorly suited to rapid prototyping. Even minor design variations typically necessitate manual updates in CAD software, making iteration time-consuming and difficult to scale. To address this limitation, we introduce Image2Gcode, an end-to-end data-driven framework that bypasses the CAD stage and generates printer-ready G-code directly from images and part drawings. Instead of relying on an explicit 3D model, a hand-drawn or captured 2D image serves as the sole input. The framework first extracts slice-wise structural cues from the image and then employs a denoising diffusion probabilistic model (DDPM) over G-code sequences. Through iterative denoising, the model transforms Gaussian noise into executable print-move trajectories with corresponding extrusion parameters, establishing a direct mapping from visual input to native toolpaths. By producing structured G-code directly from 2D imagery, Image2Gcode eliminates the need for CAD or STL intermediates, lowering the entry barrier for additive manufacturing and accelerating the design-to-fabrication cycle. This approach supports on-demand prototyping from simple sketches or visual references and integrates with upstream 2D-to-3D reconstruction modules to enable an automated pipeline from concept to physical artifact. The result is a flexible, computationally efficient framework that advances accessibility in design iteration, repair workflows, and distributed manufacturing.


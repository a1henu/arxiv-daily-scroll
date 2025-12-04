---
layout: default
title: DirectDrag: High-Fidelity, Mask-Free, Prompt-Free Drag-based Image Editing via Readout-Guided Feature Alignment
---

# DirectDrag: High-Fidelity, Mask-Free, Prompt-Free Drag-based Image Editing via Readout-Guided Feature Alignment
**arXiv**：[2512.03981v1](https://arxiv.org/abs/2512.03981) · [PDF](https://arxiv.org/pdf/2512.03981.pdf)  
**作者**：Sheng-Hao Liao, Shang-Fu Chen, Tai-Ming Huang, Wen-Huang Cheng, Kai-Lung Hua  

**一句话要点**：提出DirectDrag框架，实现无需掩码和提示的高保真拖拽式图像编辑

**关键词**：拖拽式图像编辑, 掩码生成, 特征对齐, 生成模型, 图像保真度, 交互式编辑

## 3 点简述
- 现有拖拽编辑方法依赖手动掩码和文本提示，去除后易产生视觉伪影或空间控制差
- 引入自动软掩码生成和读出引导特征对齐机制，智能推断可编辑区域并保持结构一致性
- 在DragBench和真实场景实验中，DirectDrag在图像质量和拖拽精度上优于现有方法

## 摘要（原文）

> Drag-based image editing using generative models provides intuitive control over image structures. However, existing methods rely heavily on manually provided masks and textual prompts to preserve semantic fidelity and motion precision. Removing these constraints creates a fundamental trade-off: visual artifacts without masks and poor spatial control without prompts. To address these limitations, we propose DirectDrag, a novel mask- and prompt-free editing framework. DirectDrag enables precise and efficient manipulation with minimal user input while maintaining high image fidelity and accurate point alignment. DirectDrag introduces two key innovations. First, we design an Auto Soft Mask Generation module that intelligently infers editable regions from point displacement, automatically localizing deformation along movement paths while preserving contextual integrity through the generative model's inherent capacity. Second, we develop a Readout-Guided Feature Alignment mechanism that leverages intermediate diffusion activations to maintain structural consistency during point-based edits, substantially improving visual fidelity. Despite operating without manual mask or prompt, DirectDrag achieves superior image quality compared to existing methods while maintaining competitive drag accuracy. Extensive experiments on DragBench and real-world scenarios demonstrate the effectiveness and practicality of DirectDrag for high-quality, interactive image manipulation. Project Page: https://frakw.github.io/DirectDrag/. Code is available at: https://github.com/frakw/DirectDrag.


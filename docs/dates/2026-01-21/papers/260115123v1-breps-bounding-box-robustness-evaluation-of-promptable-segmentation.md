---
layout: default
title: BREPS: Bounding-Box Robustness Evaluation of Promptable Segmentation
---

# BREPS: Bounding-Box Robustness Evaluation of Promptable Segmentation
**arXiv**：[2601.15123v1](https://arxiv.org/abs/2601.15123) · [PDF](https://arxiv.org/pdf/2601.15123.pdf)  
**作者**：Andrey Moskalenko, Danil Kuznetsov, Irina Dudko, Anastasiia Iasakova, Nikita Boldyrev, Denis Shepelev, Andrei Spiridonov, Andrey Kuznetsov, Vlad Shakhuro  

**一句话要点**：提出BREPS方法以评估可提示分割模型对边界框提示自然变化的鲁棒性

**关键词**：可提示分割, 边界框鲁棒性, 对抗性提示, 白盒优化, 用户研究, 分割评估

## 3 点简述
- 核心问题：可提示分割模型对真实用户边界框提示的自然变化敏感，现有评估协议基于合成提示，无法反映实际鲁棒性。
- 方法要点：通过用户研究收集真实边界框标注，将鲁棒性评估重构为白盒优化问题，生成符合自然约束的对抗性边界框以最小化或最大化分割误差。
- 实验或效果：在10个数据集上对先进模型进行基准测试，涵盖日常场景和医学影像，代码已开源。

## 摘要（原文）

> Promptable segmentation models such as SAM have established a powerful paradigm, enabling strong generalization to unseen objects and domains with minimal user input, including points, bounding boxes, and text prompts. Among these, bounding boxes stand out as particularly effective, often outperforming points while significantly reducing annotation costs. However, current training and evaluation protocols typically rely on synthetic prompts generated through simple heuristics, offering limited insight into real-world robustness. In this paper, we investigate the robustness of promptable segmentation models to natural variations in bounding box prompts. First, we conduct a controlled user study and collect thousands of real bounding box annotations. Our analysis reveals substantial variability in segmentation quality across users for the same model and instance, indicating that SAM-like models are highly sensitive to natural prompt noise. Then, since exhaustive testing of all possible user inputs is computationally prohibitive, we reformulate robustness evaluation as a white-box optimization problem over the bounding box prompt space. We introduce BREPS, a method for generating adversarial bounding boxes that minimize or maximize segmentation error while adhering to naturalness constraints. Finally, we benchmark state-of-the-art models across 10 datasets, spanning everyday scenes to medical imaging. Code - https://github.com/emb-ai/BREPS.


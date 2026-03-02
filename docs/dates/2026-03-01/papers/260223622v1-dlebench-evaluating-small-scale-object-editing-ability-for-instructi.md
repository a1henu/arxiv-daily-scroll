---
layout: default
title: DLEBench: Evaluating Small-scale Object Editing Ability for Instruction-based Image Editing Model
---

# DLEBench: Evaluating Small-scale Object Editing Ability for Instruction-based Image Editing Model
**arXiv**：[2602.23622v1](https://arxiv.org/abs/2602.23622) · [PDF](https://arxiv.org/pdf/2602.23622.pdf)  
**作者**：Shibo Hong, Boxian Ai, Jun Kuang, Wei Wang, FengJiao Chen, Zhongyuan Peng, Chenhao Huang, Yixin Cao  

**一句话要点**：提出DLEBench以评估指令图像编辑模型的小物体编辑能力

**关键词**：指令图像编辑, 小物体编辑, 基准评估, 视觉一致性, 多对象编辑, 评估协议

## 3 点简述
- 核心问题：现有指令图像编辑模型在小物体编辑能力上未充分探索，影响精确局部编辑
- 方法要点：构建包含1889个样本的基准，覆盖小物体、遮挡和多对象编辑等复杂场景
- 实验或效果：评估10个模型显示性能差距，提出双模式评估协议以减少主观性

## 摘要（原文）

> Significant progress has been made in the field of Instruction-based Image Editing Models (IIEMs). However, while these models demonstrate plausible adherence to instructions and strong reasoning ability on current benchmarks, their ability to edit small objects remains underexplored, despite its importance for precise local editing and refining details in both real and generated images. In this paper, we introduce DeepLookEditBench (DLEBench), the first benchmark dedicated to assessing the abilities of IIEMs in editing small-scale objects. Specifically, we construct a challenging testbed comprising 1889 samples across seven instruction types. In these samples, target objects occupy only 1%-10% of the image area, covering complex scenarios such as partial occlusion and multi-object editing. To ensure robust evaluation on this benchmark, we propose an evaluation protocol with refined score rubrics to minimize subjectivity and ambiguity in two criteria: Instruction Following and Visual Consistency. This protocol also introduces a dual-mode evaluation framework (Tool-driven and Oracle-guided Modes) addressing the misalignment between LMM-as-a-Judge and human judgements on DLEBench. Empirical results on 10 IIEMs reveal significant performance gaps in small-scale object editing, highlighting the need for specialized benchmarks to advance this ability.


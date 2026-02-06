---
layout: default
title: Benchmarking Affordance Generalization with BusyBox
---

# Benchmarking Affordance Generalization with BusyBox
**arXiv**：[2602.05441v1](https://arxiv.org/abs/2602.05441) · [PDF](https://arxiv.org/pdf/2602.05441.pdf)  
**作者**：Dean Fortier, Timothy Adamson, Tess Hellebrekers, Teresa LaScala, Kofi Ennin, Michael Murray, Andrey Kolobov, Galen Mullins  

**一句话要点**：提出BusyBox物理基准以评估视觉-语言-动作模型的物性泛化能力

**关键词**：物性泛化, 视觉-语言-动作模型, 物理基准, 机器人操作, 泛化评估, 开源数据集

## 3 点简述
- 核心问题：物性泛化是VLA模型的关键元技能，但现有评估缺乏系统性
- 方法要点：设计可互换模块的BusyBox，通过视觉变化测试泛化，提供CAD文件和数据集
- 实验或效果：实证显示强VLA模型在BusyBox变体上泛化困难，鼓励社区评估与创新

## 摘要（原文）

> Vision-Language-Action (VLA) models have been attracting the attention of researchers and practitioners thanks to their promise of generalization. Although single-task policies still offer competitive performance, VLAs are increasingly able to handle commands and environments unseen in their training set. While generalization in vision and language space is undoubtedly important for robust versatile behaviors, a key meta-skill VLAs need to possess is affordance generalization -- the ability to manipulate new objects with familiar physical features.
>   In this work, we present BusyBox, a physical benchmark for systematic semi-automatic evaluation of VLAs' affordance generalization. BusyBox consists of 6 modules with switches, sliders, wires, buttons, a display, and a dial. The modules can be swapped and rotated to create a multitude of BusyBox variations with different visual appearances but the same set of affordances. We empirically demonstrate that generalization across BusyBox variants is highly challenging even for strong open-weights VLAs such as $π_{0.5}$ and GR00T-N1.6. To encourage the research community to evaluate their own VLAs on BusyBox and to propose new affordance generalization experiments, we have designed BusyBox to be easy to build in most robotics labs. We release the full set of CAD files for 3D-printing its parts as well as a bill of materials for (optionally) assembling its electronics. We also publish a dataset of language-annotated demonstrations that we collected using the common bimanual Mobile Aloha robot on the canonical BusyBox configuration. All of the released materials are available at https://microsoft.github.io/BusyBox.


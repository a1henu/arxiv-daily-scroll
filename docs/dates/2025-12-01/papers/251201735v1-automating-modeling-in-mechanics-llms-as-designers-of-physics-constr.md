---
layout: default
title: Automating modeling in mechanics: LLMs as designers of physics-constrained neural networks for constitutive modeling of materials
---

# Automating modeling in mechanics: LLMs as designers of physics-constrained neural networks for constitutive modeling of materials
**arXiv**：[2512.01735v1](https://arxiv.org/abs/2512.01735) · [PDF](https://arxiv.org/pdf/2512.01735.pdf)  
**作者**：Marius Tacke, Matthias Busch, Kian Abdolazizi, Jonas Eichinger, Kevin Linka, Christian Cyron, Roland Aydin  

**一句话要点**：提出基于大语言模型的框架，自动生成物理约束神经网络以解决材料本构建模中的专家依赖问题。

**关键词**：大语言模型, 本构建模, 物理约束神经网络, 自动化建模, 固体力学

## 3 点简述
- 核心问题：材料本构建模需大量专家知识，数据驱动方法如CANN仍依赖人工设计。
- 方法要点：利用LLM按需生成CANN，集成物理约束并自动生成完整代码。
- 实验或效果：在三个基准问题上，LLM生成的CANN达到或超越手动设计模型的精度和泛化能力。

## 摘要（原文）

> Large language model (LLM)-based agentic frameworks increasingly adopt the paradigm of dynamically generating task-specific agents. We suggest that not only agents but also specialized software modules for scientific and engineering tasks can be generated on demand. We demonstrate this concept in the field of solid mechanics. There, so-called constitutive models are required to describe the relationship between mechanical stress and body deformation. Constitutive models are essential for both the scientific understanding and industrial application of materials. However, even recent data-driven methods of constitutive modeling, such as constitutive artificial neural networks (CANNs), still require substantial expert knowledge and human labor. We present a framework in which an LLM generates a CANN on demand, tailored to a given material class and dataset provided by the user. The framework covers LLM-based architecture selection, integration of physical constraints, and complete code generation. Evaluation on three benchmark problems demonstrates that LLM-generated CANNs achieve accuracy comparable to or greater than manually engineered counterparts, while also exhibiting reliable generalization to unseen loading scenarios and extrapolation to large deformations. These findings indicate that LLM-based generation of physics-constrained neural networks can substantially reduce the expertise required for constitutive modeling and represent a step toward practical end-to-end automation.


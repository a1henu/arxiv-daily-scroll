---
layout: default
title: LangDriveCTRL: Natural Language Controllable Driving Scene Editing with Multi-modal Agents
---

# LangDriveCTRL: Natural Language Controllable Driving Scene Editing with Multi-modal Agents
**arXiv**：[2512.17445v1](https://arxiv.org/abs/2512.17445) · [PDF](https://arxiv.org/pdf/2512.17445.pdf)  
**作者**：Yun He, Francesco Pittaluga, Ziyu Jiang, Matthias Zwicker, Manmohan Chandraker, Zaid Tasneem  

**一句话要点**：提出LangDriveCTRL框架，通过自然语言指令编辑真实驾驶视频以合成多样化交通场景。

**关键词**：自然语言可控编辑, 驾驶场景合成, 多智能体系统, 3D场景分解, 视频扩散模型

## 3 点简述
- 核心问题：如何基于自然语言指令精细编辑真实驾驶视频，实现对象和行为的多模态控制。
- 方法要点：利用3D场景分解构建场景图，通过多智能体管道协调对象定位、行为编辑和审查。
- 实验或效果：指令对齐度比先前最佳方法提升近2倍，保持结构、光感和交通真实性。

## 摘要（原文）

> LangDriveCTRL is a natural-language-controllable framework for editing real-world driving videos to synthesize diverse traffic scenarios. It leverages explicit 3D scene decomposition to represent driving videos as a scene graph, containing static background and dynamic objects. To enable fine-grained editing and realism, it incorporates an agentic pipeline in which an Orchestrator transforms user instructions into execution graphs that coordinate specialized agents and tools. Specifically, an Object Grounding Agent establishes correspondence between free-form text descriptions and target object nodes in the scene graph; a Behavior Editing Agent generates multi-object trajectories from language instructions; and a Behavior Reviewer Agent iteratively reviews and refines the generated trajectories. The edited scene graph is rendered and then refined using a video diffusion tool to address artifacts introduced by object insertion and significant view changes. LangDriveCTRL supports both object node editing (removal, insertion and replacement) and multi-object behavior editing from a single natural-language instruction. Quantitatively, it achieves nearly $2\times$ higher instruction alignment than the previous SoTA, with superior structural preservation, photorealism, and traffic realism. Project page is available at: https://yunhe24.github.io/langdrivectrl/.


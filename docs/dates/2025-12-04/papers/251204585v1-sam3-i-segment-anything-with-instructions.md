---
layout: default
title: SAM3-I: Segment Anything with Instructions
---

# SAM3-I: Segment Anything with Instructions
**arXiv**：[2512.04585v1](https://arxiv.org/abs/2512.04585) · [PDF](https://arxiv.org/pdf/2512.04585.pdf)  
**作者**：Jingjing Li, Yue Feng, Yuchen Guo, Jincai Huang, Yongri Piao, Qi Bi, Miao Zhang, Xiaoqi Zhao, Qiang Chen, Shihao Zou, Wei Ji, Huchuan Lu, Li Cheng  

**一句话要点**：提出SAM3-I框架以增强SAM3的指令级分割能力，支持复杂自然语言指令。

**关键词**：指令感知分割, 视觉语言对齐, 开放词汇分割, 级联适配, 自然语言指令

## 3 点简述
- SAM3依赖名词短语提示，难以处理包含属性、空间关系等的复杂指令。
- 引入指令感知级联适配机制，对齐指令语义与视觉语言表示，实现直接指令跟随分割。
- 实验显示SAM3-I在保持概念驱动能力的同时，有效扩展至自然语言指令分割。

## 摘要（原文）

> Segment Anything Model 3 (SAM3) has advanced open-vocabulary segmentation through promptable concept segmentation, allowing users to segment all instances corresponding to a given concept, typically specified with short noun-phrase (NP) prompts. While this marks the first integration of language-level concepts within the SAM family, real-world usage typically requires far richer expressions that include attributes, spatial relations, functionalities, actions, states, and even implicit reasoning over instances. Currently, SAM3 relies on external multi-modal agents to convert complex instructions into NPs and then conduct iterative mask filtering. However, these NP-level concepts remain overly coarse, often failing to precisely represent a specific instance. In this work, we present SAM3-I, an enhanced framework that unifies concept-level understanding and instruction-level reasoning within the SAM family. SAM3-I introduces an instruction-aware cascaded adaptation mechanism that progressively aligns expressive instruction semantics with SAM3's existing vision-language representations, enabling direct instruction-following segmentation without sacrificing its original concept-driven capabilities. Furthermore, we design a structured instruction taxonomy spanning concept, simple, and complex levels, and develop a scalable data engine to construct a dataset with diverse instruction-mask pairs. Experiments show that SAM3-I delivers appealing performance, demonstrating that SAM3 can be effectively extended to follow natural-language instructions while preserving its strong concept grounding. We open-source SAM3-I and provide practical fine-tuning workflows, enabling researchers to adapt it to domain-specific applications. The source code is available here.


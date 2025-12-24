---
layout: default
title: Generative Digital Twins: Vision-Language Simulation Models for Executable Industrial Systems
---

# Generative Digital Twins: Vision-Language Simulation Models for Executable Industrial Systems
**arXiv**：[2512.20387v1](https://arxiv.org/abs/2512.20387) · [PDF](https://arxiv.org/pdf/2512.20387.pdf)  
**作者**：YuChe Hsu, AnJui Wang, TsaiChing Ni, YuanFu Yang  

**一句话要点**：提出视觉-语言仿真模型以从布局草图和自然语言提示生成可执行工业仿真代码

**关键词**：生成式数字孪生, 视觉-语言模型, 工业仿真, 跨模态推理, 可执行代码生成, 多模态数据集

## 3 点简述
- 核心问题：工业仿真系统需跨模态理解视觉布局与文本描述以生成可执行代码
- 方法要点：构建大规模数据集并设计模型统一视觉与语言理解，实现草图到代码的转换
- 实验或效果：通过新评估指标验证模型在结构准确性和执行稳健性方面表现优异

## 摘要（原文）

> We propose a Vision-Language Simulation Model (VLSM) that unifies visual and textual understanding to synthesize executable FlexScript from layout sketches and natural-language prompts, enabling cross-modal reasoning for industrial simulation systems. To support this new paradigm, the study constructs the first large-scale dataset for generative digital twins, comprising over 120,000 prompt-sketch-code triplets that enable multimodal learning between textual descriptions, spatial structures, and simulation logic. In parallel, three novel evaluation metrics, Structural Validity Rate (SVR), Parameter Match Rate (PMR), and Execution Success Rate (ESR), are proposed specifically for this task to comprehensively evaluate structural integrity, parameter fidelity, and simulator executability. Through systematic ablation across vision encoders, connectors, and code-pretrained language backbones, the proposed models achieve near-perfect structural accuracy and high execution robustness. This work establishes a foundation for generative digital twins that integrate visual reasoning and language understanding into executable industrial simulation systems.


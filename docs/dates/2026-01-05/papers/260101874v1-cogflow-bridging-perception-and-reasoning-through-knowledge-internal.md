---
layout: default
title: CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving
---

# CogFlow: Bridging Perception and Reasoning through Knowledge Internalization for Visual Mathematical Problem Solving
**arXiv**：[2601.01874v1](https://arxiv.org/abs/2601.01874) · [PDF](https://arxiv.org/pdf/2601.01874.pdf)  
**作者**：Shuhang Chen, Yunqiu Xu, Junjie Xie, Aojun Lu, Tao Feng, Zeying Huang, Ning Zhang, Yi Sun, Yi Yang, Hangjie Yuan  

**一句话要点**：提出CogFlow框架，通过知识内化阶段桥接感知与推理，以解决视觉数学问题求解中的瓶颈。

**关键词**：视觉数学推理, 知识内化, 多模态大语言模型, 认知启发框架, 数据集构建

## 3 点简述
- 核心问题：现有模型在视觉数学推理中，感知提取的视觉线索未能忠实整合到后续推理中，导致性能受限。
- 方法要点：设计三阶段认知启发框架，包括感知、知识内化和推理，引入协同视觉奖励、知识内化奖励模型和视觉门控策略优化算法。
- 实验或效果：在常用视觉数学推理基准上验证了CogFlow的优越性，并贡献了包含12万高质量标注的MathCog数据集。

## 摘要（原文）

> Despite significant progress, multimodal large language models continue to struggle with visual mathematical problem solving. Some recent works recognize that visual perception is a bottleneck in visual mathematical reasoning, but their solutions are limited to improving the extraction and interpretation of visual inputs. Notably, they all ignore the key issue of whether the extracted visual cues are faithfully integrated and properly utilized in subsequent reasoning. Motivated by this, we present CogFlow, a novel cognitive-inspired three-stage framework that incorporates a knowledge internalization stage, explicitly simulating the hierarchical flow of human reasoning: perception$\Rightarrow$internalization$\Rightarrow$reasoning. Inline with this hierarchical flow, we holistically enhance all its stages. We devise Synergistic Visual Rewards to boost perception capabilities in parametric and semantic spaces, jointly improving visual information extraction from symbols and diagrams. To guarantee faithful integration of extracted visual cues into subsequent reasoning, we introduce a Knowledge Internalization Reward model in the internalization stage, bridging perception and reasoning. Moreover, we design a Visual-Gated Policy Optimization algorithm to further enforce the reasoning is grounded with the visual knowledge, preventing models seeking shortcuts that appear coherent but are visually ungrounded reasoning chains. Moreover, we contribute a new dataset MathCog for model training, which contains samples with over 120K high-quality perception-reasoning aligned annotations. Comprehensive experiments and analysis on commonly used visual mathematical reasoning benchmarks validate the superiority of the proposed CogFlow.


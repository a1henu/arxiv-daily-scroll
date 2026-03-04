---
layout: default
title: iGVLM: Dynamic Instruction-Guided Vision Encoding for Question-Aware Multimodal Understanding
---

# iGVLM: Dynamic Instruction-Guided Vision Encoding for Question-Aware Multimodal Understanding
**arXiv**：[2603.02748v1](https://arxiv.org/abs/2603.02748) · [PDF](https://arxiv.org/pdf/2603.02748.pdf)  
**作者**：HanZpeng Liu, Yaqian Li, Zidan Wang, Shuoxi Zhang, Zihao Bo, Rinyoichi Takezoe, Kaiwen Long, Kun He  

**一句话要点**：提出iGVLM框架，通过指令引导视觉编码解决多模态理解中的表示瓶颈问题。

**关键词**：指令引导视觉编码, 多模态理解, 自适应层归一化, 表示瓶颈, 逻辑一致性评估, 插件式框架

## 3 点简述
- 现有大型视觉-语言模型依赖静态视觉编码器，导致任务特定视觉线索利用不足。
- iGVLM采用解耦双分支架构，结合冻结表示分支和动态条件分支进行特征调制。
- 实验引入MM4诊断探针，显示iGVLM能增强指令敏感性，提升多查询多指令下的逻辑一致性。

## 摘要（原文）

> Despite the success of Large Vision--Language Models (LVLMs), most existing architectures suffer from a representation bottleneck: they rely on static, instruction-agnostic vision encoders whose visual representations are utilized in an invariant manner across different textual tasks. This rigidity hinders fine-grained reasoning where task-specific visual cues are critical. To address this issue, we propose iGVLM, a general framework for instruction-guided visual modulation. iGVLM introduces a decoupled dual-branch architecture: a frozen representation branch that preserves task-agnostic visual representations learned during pre-training, and a dynamic conditioning branch that performs affine feature modulation via Adaptive Layer Normalization (AdaLN). This design enables a smooth transition from general-purpose perception to instruction-aware reasoning while maintaining the structural integrity and stability of pre-trained visual priors. Beyond standard benchmarks, we introduce MM4, a controlled diagnostic probe for quantifying logical consistency under multi-query, multi-instruction settings. Extensive results show that iGVLM consistently enhances instruction sensitivity across diverse language backbones, offering a plug-and-play paradigm for bridging passive perception and active reasoning.


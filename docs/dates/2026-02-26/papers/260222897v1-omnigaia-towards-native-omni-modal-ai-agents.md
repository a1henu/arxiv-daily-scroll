---
layout: default
title: OmniGAIA: Towards Native Omni-Modal AI Agents
---

# OmniGAIA: Towards Native Omni-Modal AI Agents
**arXiv**：[2602.22897v1](https://arxiv.org/abs/2602.22897) · [PDF](https://arxiv.org/pdf/2602.22897.pdf)  
**作者**：Xiaoxi Li, Wenxiang Jiao, Jiarui Jin, Shijian Wang, Guanting Dong, Jiajie Jin, Hao Wang, Yinuo Wang, Ji-Rong Wen, Yuan Lu, Zhicheng Dou  

**一句话要点**：提出OmniGAIA基准和OmniAtlas代理，以评估和增强全模态AI助手在跨模态推理与工具使用中的能力。

**关键词**：全模态AI代理, 跨模态推理, 工具集成, 基准评估, 后见引导训练, 多模态事件图

## 3 点简述
- 当前多模态大模型局限于双模态交互，缺乏全模态统一认知能力，阻碍通用AI助手发展。
- 通过全模态事件图构建OmniGAIA基准，合成复杂多跳查询，支持视频、音频和图像跨模态推理与工具执行评估。
- 提出OmniAtlas原生全模态基础代理，采用工具集成推理范式，通过后见引导树探索和OmniDPO训练，提升开源模型的工具使用能力。

## 摘要（原文）

> Human intelligence naturally intertwines omni-modal perception -- spanning vision, audio, and language -- with complex reasoning and tool usage to interact with the world. However, current multi-modal LLMs are primarily confined to bi-modal interactions (e.g., vision-language), lacking the unified cognitive capabilities required for general AI assistants. To bridge this gap, we introduce OmniGAIA, a comprehensive benchmark designed to evaluate omni-modal agents on tasks necessitating deep reasoning and multi-turn tool execution across video, audio, and image modalities. Constructed via a novel omni-modal event graph approach, OmniGAIA synthesizes complex, multi-hop queries derived from real-world data that require cross-modal reasoning and external tool integration. Furthermore, we propose OmniAtlas, a native omni-modal foundation agent under tool-integrated reasoning paradigm with active omni-modal perception. Trained on trajectories synthesized via a hindsight-guided tree exploration strategy and OmniDPO for fine-grained error correction, OmniAtlas effectively enhances the tool-use capabilities of existing open-source models. This work marks a step towards next-generation native omni-modal AI assistants for real-world scenarios.


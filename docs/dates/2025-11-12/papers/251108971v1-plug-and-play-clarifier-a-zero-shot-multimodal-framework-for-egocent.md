---
layout: default
title: Plug-and-Play Clarifier: A Zero-Shot Multimodal Framework for Egocentric Intent Disambiguation
---

# Plug-and-Play Clarifier: A Zero-Shot Multimodal Framework for Egocentric Intent Disambiguation
**arXiv**：[2511.08971v1](https://arxiv.org/abs/2511.08971) · [PDF](https://arxiv.org/pdf/2511.08971.pdf)  
**作者**：Sicheng Yang, Yukai Huang, Weitong Cai, Shitong Sun, You He, Jiankang Deng, Hang Zhang, Jifei Song, Zhensong Zhang  

**一句话要点**：提出即插即用澄清框架以解决第一人称多模态意图歧义问题

**关键词**：第一人称交互, 多模态意图澄清, 零样本框架, 模块化设计, 视觉语言模型, 指示手势理解

## 3 点简述
- 核心问题：第一人称AI代理因语言不明确、视觉数据不完美和指示手势导致多模态意图歧义，常引发任务失败
- 方法要点：框架包含文本、视觉和跨模态澄清模块，通过零样本模块化分解歧义问题
- 实验或效果：实验显示框架提升小模型意图澄清性能约30%，视觉和跨模态澄清准确率分别提高超20%和5%

## 摘要（原文）

> The performance of egocentric AI agents is fundamentally limited by multimodal intent ambiguity. This challenge arises from a combination of underspecified language, imperfect visual data, and deictic gestures, which frequently leads to task failure. Existing monolithic Vision-Language Models (VLMs) struggle to resolve these multimodal ambiguous inputs, often failing silently or hallucinating responses. To address these ambiguities, we introduce the Plug-and-Play Clarifier, a zero-shot and modular framework that decomposes the problem into discrete, solvable sub-tasks. Specifically, our framework consists of three synergistic modules: (1) a text clarifier that uses dialogue-driven reasoning to interactively disambiguate linguistic intent, (2) a vision clarifier that delivers real-time guidance feedback, instructing users to adjust their positioning for improved capture quality, and (3) a cross-modal clarifier with grounding mechanism that robustly interprets 3D pointing gestures and identifies the specific objects users are pointing to. Extensive experiments demonstrate that our framework improves the intent clarification performance of small language models (4--8B) by approximately 30%, making them competitive with significantly larger counterparts. We also observe consistent gains when applying our framework to these larger models. Furthermore, our vision clarifier increases corrective guidance accuracy by over 20%, and our cross-modal clarifier improves semantic answer accuracy for referential grounding by 5%. Overall, our method provides a plug-and-play framework that effectively resolves multimodal ambiguity and significantly enhances user experience in egocentric interaction.


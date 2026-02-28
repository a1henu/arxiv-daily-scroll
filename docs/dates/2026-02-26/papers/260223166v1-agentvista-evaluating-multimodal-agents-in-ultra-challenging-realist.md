---
layout: default
title: AgentVista: Evaluating Multimodal Agents in Ultra-Challenging Realistic Visual Scenarios
---

# AgentVista: Evaluating Multimodal Agents in Ultra-Challenging Realistic Visual Scenarios
**arXiv**：[2602.23166v1](https://arxiv.org/abs/2602.23166) · [PDF](https://arxiv.org/pdf/2602.23166.pdf)  
**作者**：Zhaochen Su, Jincheng Gao, Hangyu Guo, Zhenhua Liu, Lueyang Zhang, Xinyu Geng, Shijue Huang, Peng Xia, Guanyu Jiang, Cheng Wang, Yue Zhang, Yi R. Fung, Junxian He  

**一句话要点**：提出AgentVista基准以评估多模态智能体在超挑战现实视觉场景中的表现

**关键词**：多模态智能体评估, 长时程工具使用, 现实视觉场景, 混合工具交互, 基准测试

## 3 点简述
- 现有基准未能充分捕捉现实性、视觉细节和长时程工具使用，限制了多模态智能体评估
- AgentVista涵盖7个类别25个子领域，结合真实视觉场景与混合工具使用，要求跨模态长时程交互
- 评估显示最先进模型在长时程多模态工具使用上存在显著差距，最高准确率仅27.3%

## 摘要（原文）

> Real-world multimodal agents solve multi-step workflows grounded in visual evidence. For example, an agent can troubleshoot a device by linking a wiring photo to a schematic and validating the fix with online documentation, or plan a trip by interpreting a transit map and checking schedules under routing constraints. However, existing multimodal benchmarks mainly evaluate single-turn visual reasoning or specific tool skills, and they do not fully capture the realism, visual subtlety, and long-horizon tool use that practical agents require. We introduce AgentVista, a benchmark for generalist multimodal agents that spans 25 sub-domains across 7 categories, pairing realistic and detail-rich visual scenarios with natural hybrid tool use. Tasks require long-horizon tool interactions across modalities, including web search, image search, page navigation, and code-based operations for both image processing and general programming. Comprehensive evaluation of state-of-the-art models exposes significant gaps in their ability to carry out long-horizon multimodal tool use. Even the best model in our evaluation, Gemini-3-Pro with tools, achieves only 27.3% overall accuracy, and hard instances can require more than 25 tool-calling turns. We expect AgentVista to accelerate the development of more capable and reliable multimodal agents for realistic and ultra-challenging problem solving.


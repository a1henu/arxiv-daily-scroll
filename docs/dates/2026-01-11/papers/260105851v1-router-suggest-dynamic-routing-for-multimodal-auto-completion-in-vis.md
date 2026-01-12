---
layout: default
title: Router-Suggest: Dynamic Routing for Multimodal Auto-Completion in Visually-Grounded Dialogs
---

# Router-Suggest: Dynamic Routing for Multimodal Auto-Completion in Visually-Grounded Dialogs
**arXiv**：[2601.05851v1](https://arxiv.org/abs/2601.05851) · [PDF](https://arxiv.org/pdf/2601.05851.pdf)  
**作者**：Sandeep Mishra, Devichand Budagam, Anubhab Mandal, Bishal Santra, Pawan Goyal, Manish Gupta  

**一句话要点**：提出Router-Suggest框架，通过动态路由在视觉对话中实现高效多模态自动补全。

**关键词**：多模态自动补全, 视觉对话, 动态路由, 视觉语言模型, 用户意图预测, 实时聊天辅助

## 3 点简述
- 核心问题：传统文本自动补全在视觉对话中难以准确捕捉用户意图，需结合多模态上下文。
- 方法要点：引入多模态自动补全任务，基于Router-Suggest动态选择文本模型或视觉语言模型以平衡精度与效率。
- 实验或效果：在基准数据集上，Router-Suggest比最佳视觉语言模型提速2.3至10倍，用户研究显示多模态模型显著提升满意度和补全质量。

## 摘要（原文）

> Real-time multimodal auto-completion is essential for digital assistants, chatbots, design tools, and healthcare consultations, where user inputs rely on shared visual context. We introduce Multimodal Auto-Completion (MAC), a task that predicts upcoming characters in live chats using partially typed text and visual cues. Unlike traditional text-only auto-completion (TAC), MAC grounds predictions in multimodal context to better capture user intent. To enable this task, we adapt MMDialog and ImageChat to create benchmark datasets. We evaluate leading vision-language models (VLMs) against strong textual baselines, highlighting trade-offs in accuracy and efficiency. We present Router-Suggest, a router framework that dynamically selects between textual models and VLMs based on dialog context, along with a lightweight variant for resource-constrained environments. Router-Suggest achieves a 2.3x to 10x speedup over the best-performing VLM. A user study shows that VLMs significantly excel over textual models on user satisfaction, notably saving user typing effort and improving the quality of completions in multi-turn conversations. These findings underscore the need for multimodal context in auto-completions, leading to smarter, user-aware assistants.


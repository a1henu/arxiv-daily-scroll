---
layout: default
title: See2Refine: Vision-Language Feedback Improves LLM-Based eHMI Action Designers
---

# See2Refine: Vision-Language Feedback Improves LLM-Based eHMI Action Designers
**arXiv**：[2602.02063v1](https://arxiv.org/abs/2602.02063) · [PDF](https://arxiv.org/pdf/2602.02063.pdf)  
**作者**：Ding Xia, Xinyue Gui, Mark Colley, Fan Gao, Zhongyi Zhou, Dongyuan Li, Renhe Jiang, Takeo Igarashi  

**一句话要点**：提出See2Refine框架，利用视觉语言模型反馈改进基于大语言模型的eHMI动作设计

**关键词**：自动驾驶通信, 外部人机界面, 视觉语言模型, 大语言模型, 动作设计, 闭环框架

## 3 点简述
- 核心问题：自动驾驶车辆缺乏自然通信渠道，现有eHMI设计依赖人工或固定提示，难以适应动态交通环境。
- 方法要点：采用视觉语言模型作为感知评估器，提供自动化视觉反馈，迭代优化大语言模型生成的eHMI动作。
- 实验或效果：在多种eHMI模态和LLM模型大小下，框架性能优于仅提示的LLM设计和人工基线，VLM评估与人类偏好一致。

## 摘要（原文）

> Automated vehicles lack natural communication channels with other road users, making external Human-Machine Interfaces (eHMIs) essential for conveying intent and maintaining trust in shared environments. However, most eHMI studies rely on developer-crafted message-action pairs, which are difficult to adapt to diverse and dynamic traffic contexts. A promising alternative is to use Large Language Models (LLMs) as action designers that generate context-conditioned eHMI actions, yet such designers lack perceptual verification and typically depend on fixed prompts or costly human-annotated feedback for improvement. We present See2Refine, a human-free, closed-loop framework that uses vision-language model (VLM) perceptual evaluation as automated visual feedback to improve an LLM-based eHMI action designer. Given a driving context and a candidate eHMI action, the VLM evaluates the perceived appropriateness of the action, and this feedback is used to iteratively revise the designer's outputs, enabling systematic refinement without human supervision. We evaluate our framework across three eHMI modalities (lightbar, eyes, and arm) and multiple LLM model sizes. Across settings, our framework consistently outperforms prompt-only LLM designers and manually specified baselines in both VLM-based metrics and human-subject evaluations. Results further indicate that the improvements generalize across modalities and that VLM evaluations are well aligned with human preferences, supporting the robustness and effectiveness of See2Refine for scalable action design.


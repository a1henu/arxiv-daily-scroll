---
layout: default
title: Lightweight Visual Reasoning for Socially-Aware Robots
---

# Lightweight Visual Reasoning for Socially-Aware Robots
**arXiv**：[2603.03942v1](https://arxiv.org/abs/2603.03942) · [PDF](https://arxiv.org/pdf/2603.03942.pdf)  
**作者**：Alessio Galatolo, Ronald Cumbal, Alexandros Rouchitsas, Katie Winkle, Didem Gürdür Broo, Ginevra Castellano  

**一句话要点**：提出轻量级语言到视觉反馈模块，以增强视觉语言模型在机器人任务中的推理能力。

**关键词**：视觉语言模型, 人机交互, 轻量级模块, 反馈机制, 机器人推理

## 3 点简述
- 核心问题：现有视觉语言模型难以处理多模态人机交互的复杂性。
- 方法要点：通过门控多层感知机将图像令牌隐藏状态反馈到编码器输入，实现二次场景解读。
- 实验或效果：在导航、场景描述和意图识别任务中提升性能，额外参数少于3%。

## 摘要（原文）

> Robots operating in shared human environments must not only navigate, interact, and detect their surroundings, they must also interpret and respond to dynamic, and often unpredictable, human behaviours. Although recent advances have shown promise in enhancing robotic perception and instruction-following using Vision-Language Models (VLMs), they remain limited in addressing the complexities of multimodal human-robot interactions (HRI). Motivated by this challenge, we introduce a lightweight language-to-vision feedback module that closes the loop between an LLM and the vision encoder in VLMs. The module projects image-token hidden states through a gated Multi-Layer Perceptron (MLP) back into the encoder input, prompting a second pass that reinterprets the scene under text context. We evaluate this approach on three robotics-centred tasks: navigation in a simulated environment (Habitat), sequential scene description (Mementos-Robotics), and human-intention recognition (our HRI dataset). Results show that our method improves Qwen 2.5 (7B) by $3.3\%$ (less distance), $+0.057$ description score, and $+2.93\%$ accuracy, with less than $3\%$ extra parameters; Gemma 3 (4B) and LLaVA OV 1.5 (4B) show mixed navigation results but gains $+0.111,+0.055$ and $+10.81\%,+4.79\%$ on the latter two tasks. Code is available at https://github.com/alessioGalatolo/VLM-Reasoning-for-Robotics


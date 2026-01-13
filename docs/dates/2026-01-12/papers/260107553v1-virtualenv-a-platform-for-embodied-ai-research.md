---
layout: default
title: VirtualEnv: A Platform for Embodied AI Research
---

# VirtualEnv: A Platform for Embodied AI Research
**arXiv**：[2601.07553v1](https://arxiv.org/abs/2601.07553) · [PDF](https://arxiv.org/pdf/2601.07553.pdf)  
**作者**：Kabir Swain, Sijie Han, Ayush Raina, Jin Zhang, Shuang Li, Michael Stopa, Antonio Torralba  

**一句话要点**：提出VirtualEnv仿真平台，基于Unreal Engine 5，用于具身AI中LLMs的精细评估与交互研究。

**关键词**：具身AI, 仿真平台, 大语言模型评估, 多智能体协作, 程序化任务生成, 交互式环境

## 3 点简述
- 核心问题：LLMs在具身和交互场景中缺乏现实、可评估的环境，需标准化测试平台。
- 方法要点：构建用户友好API，支持自然语言控制、多模态输入生成任务，集成LLMs和VLMs。
- 实验或效果：通过复杂度递增任务，基准测试LLMs的适应性、规划与多智能体协作性能。

## 摘要（原文）

> As large language models (LLMs) continue to improve in reasoning and decision-making, there is a growing need for realistic and interactive environments where their abilities can be rigorously evaluated. We present VirtualEnv, a next-generation simulation platform built on Unreal Engine 5 that enables fine-grained benchmarking of LLMs in embodied and interactive scenarios. VirtualEnv supports rich agent-environment interactions, including object manipulation, navigation, and adaptive multi-agent collaboration, as well as game-inspired mechanics like escape rooms and procedurally generated environments. We provide a user-friendly API built on top of Unreal Engine, allowing researchers to deploy and control LLM-driven agents using natural language instructions. We integrate large-scale LLMs and vision-language models (VLMs), such as GPT-based models, to generate novel environments and structured tasks from multimodal inputs. Our experiments benchmark the performance of several popular LLMs across tasks of increasing complexity, analyzing differences in adaptability, planning, and multi-agent coordination. We also describe our methodology for procedural task generation, task validation, and real-time environment control. VirtualEnv is released as an open-source platform, we aim to advance research at the intersection of AI and gaming, enable standardized evaluation of LLMs in embodied AI settings, and pave the way for future developments in immersive simulations and interactive entertainment.


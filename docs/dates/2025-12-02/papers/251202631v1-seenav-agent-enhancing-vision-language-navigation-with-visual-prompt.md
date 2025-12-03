---
layout: default
title: SeeNav-Agent: Enhancing Vision-Language Navigation with Visual Prompt and Step-Level Policy Optimization
---

# SeeNav-Agent: Enhancing Vision-Language Navigation with Visual Prompt and Step-Level Policy Optimization
**arXiv**：[2512.02631v1](https://arxiv.org/abs/2512.02631) · [PDF](https://arxiv.org/pdf/2512.02631.pdf)  
**作者**：Zhengcheng Wang, Zichuan Lin, Yijun Yang, Haobo Fu, Deheng Ye  

**一句话要点**：提出SeeNav-Agent框架，通过视觉提示和步级策略优化增强视觉语言导航性能

**关键词**：视觉语言导航, 视觉提示, 强化微调, 步级策略优化, 导航成功率

## 3 点简述
- 现有基于大视觉语言模型的导航代理存在感知、推理和规划错误，影响导航成功率
- 引入双视图视觉提示减少感知幻觉，设计步级强化微调方法SRGPO提升规划能力
- 在EmbodiedBench基准上，视觉提示使GPT-4.1成功率提升约20pp，SRGPO使Qwen2.5-VL-3B模型超越现有最佳模型5.6pp

## 摘要（原文）

> Existing Vision-Language Navigation (VLN) agents based on Large Vision-Language Models (LVLMs) often suffer from perception errors, reasoning errors, and planning errors, which significantly hinder their navigation performance. To address these limitations, a novel VLN agent framework, named SeeNav-Agent, is proposed in this work. First, to reduce perception hallucinations of the visual module of the VLN agent, a dual-view Visual Prompt (VP) technique is introduced in the input space, which can also improve the agent's understanding of current spatial states. Subsequently, a novel step-level Reinforcement Fine-Tuning (RFT) method, Step Reward Group Policy Optimization (SRGPO), is designed for the post-training of VLN agents. In SRGPO, we first define verifiable process rewards for the navigation task, and then perform efficient step-level advantage estimation by randomly grouping different navigation steps. SRGPO provides dense reward signals for the reinforcement learning process of the VLN agent and enhances its planning capability. Experimental results on the EmbodiedBench Navigation benchmark indicate that by introducing the zero-shot VP module, the GPT-4.1 achieves a navigation success rate of 86.7%, surpassing the current best LVLM by approximately 20 percentage points (pp). Through post-training based on SRGPO, the Qwen2.5-VL-3B model reaches a navigation success rate of 72.3%, outperforming the best existing LVLM model by 5.6 pp. Moreover, compared to RFT algorithms such as GRPO and GiGPO, the proposed SRGPO demonstrates significant improvements in training stability, convergence efficiency, and generalization capability.


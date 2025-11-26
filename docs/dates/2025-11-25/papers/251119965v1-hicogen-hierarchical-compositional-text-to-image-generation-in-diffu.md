---
layout: default
title: HiCoGen: Hierarchical Compositional Text-to-Image Generation in Diffusion Models via Reinforcement Learning
---

# HiCoGen: Hierarchical Compositional Text-to-Image Generation in Diffusion Models via Reinforcement Learning
**arXiv**：[2511.19965v1](https://arxiv.org/abs/2511.19965) · [PDF](https://arxiv.org/pdf/2511.19965.pdf)  
**作者**：Hongji Yang, Yucheng Zhou, Wencheng Han, Runzhou Tao, Zhongying Qiu, Jianfei Yang, Jianbing Shen  

**一句话要点**：提出HiCoGen框架以解决复杂提示下图像生成的概念遗漏与组合性问题

**关键词**：文本到图像生成, 扩散模型, 强化学习, 层次组合, 概念合成, 基准评估

## 3 点简述
- 核心问题：现有扩散模型在复杂多对象提示下易出现概念遗漏、混淆和组合性差
- 方法要点：使用LLM分解提示并迭代合成，结合强化学习优化生成过程
- 实验或效果：在HiCoPrompt基准上显著提升概念覆盖率和组合准确性

## 摘要（原文）

> Recent advances in diffusion models have demonstrated impressive capability in generating high-quality images for simple prompts. However, when confronted with complex prompts involving multiple objects and hierarchical structures, existing models struggle to accurately follow instructions, leading to issues such as concept omission, confusion, and poor compositionality. To address these limitations, we propose a Hierarchical Compositional Generative framework (HiCoGen) built upon a novel Chain of Synthesis (CoS) paradigm. Instead of monolithic generation, HiCoGen first leverages a Large Language Model (LLM) to decompose complex prompts into minimal semantic units. It then synthesizes these units iteratively, where the image generated in each step provides crucial visual context for the next, ensuring all textual concepts are faithfully constructed into the final scene. To further optimize this process, we introduce a reinforcement learning (RL) framework. Crucially, we identify that the limited exploration of standard diffusion samplers hinders effective RL. We theoretically prove that sample diversity is maximized by concentrating stochasticity in the early generation stages and, based on this insight, propose a novel Decaying Stochasticity Schedule to enhance exploration. Our RL algorithm is then guided by a hierarchical reward mechanism that jointly evaluates the image at the global, subject, and relationship levels. We also construct HiCoPrompt, a new text-to-image benchmark with hierarchical prompts for rigorous evaluation. Experiments show our approach significantly outperforms existing methods in both concept coverage and compositional accuracy.

